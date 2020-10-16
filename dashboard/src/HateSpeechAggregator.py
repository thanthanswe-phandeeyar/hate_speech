import pandas as pd
import numpy as np
from tqdm import tqdm
from datetime import datetime
import os
from CrowdTangleExportCommentsTools import HsleCandidateGenerationUtils as hsle
from MyanmarNLPTools import MMTools
from MyanmarNLPTools.MMCleaner import MMCleaner



'''
`name_core`: core names of aggregated files (sometimes partially)
	lex-time, etc.
'''
def datetime_suffix():
	now = datetime.now()

	return '{}{:02}{:02}{:02}{:02}{:02}'.format(
		now.year, now.month, now.day, now.hour, now.minute, now.second)

	
# Constants
EXT = 'csv'
OUTPUT_PATH = '../clean-data/aggregated/{}'.format(datetime_suffix()) # create a new folder with a respective path.
TYPE_DICT = hsle.LoadLexTopicDict()

def save_dataframe(dataframe, name_core, index=False, sep='~'):

	'''
	dataframe: pd.DataFrame to be saved.
	name_core: name of the file without the suffix.
	Append if file exists, write otherwise.
	'''

	output_file = '{}/{}.csv'.format(OUTPUT_PATH, name_core)
	if os.path.isfile(output_file):
		print('Appending {} lines...'.format(dataframe.shape[0]))
		dataframe.to_csv(output_file, mode='a', index=index, header=None, sep=sep)
	else:
		print('Writing {} lines...'.format(dataframe.shape[0]))
		dataframe.to_csv(output_file, mode='w', index=index, sep=sep)
	print('Done.')


def run(comment_files):
	os.mkdir(OUTPUT_PATH)
	comment_files.sort()
	if comment_files[0].split('/')[-1].split('_')[0]=="group":
		date_from = comment_files[0].split('/')[-1].split('_')[1]
		date_to = comment_files[0].split('/')[-1].rstrip('.csv').split('_')[-1]
	else:
		date_from = comment_files[0].split('/')[-1].split('_')[0]
		date_to = comment_files[0].split('/')[-1].rstrip('.csv').split('_')[-1]
	print('Current date range:', date_from, date_to)
	date_from, date_to = str2datetime(date_from), str2datetime(date_to)
	for comment_file in comment_files:
		print('=========================================')
		print('Processing:', comment_file.split('/')[-1])
		comment_df = load_df(comment_file, date_from, date_to)
		lex_topic_page_time(comment_df.loc[
			~comment_df.lex_found.isna(), # only rows with lex_found
			['profile_id','name','datetime','lex_found','topics_found','page_group_name']])
		page_hs_ratio(comment_df)
		hspage_effect_on_comments(comment_df)
		hsfirst_comment_effect_on_replies(comment_df)
		page_reach(comment_df)


	# tmp = [f for f in comment_files if 'group' not in f]
	# tmp.sort()
	# date_from = tmp[0].split('/')[-1].split('_')[0]
	# date_to = tmp[-1].split('/')[-1].rstrip('.csv').split('_')[-1]
	# print('Current date range:', date_from, date_to)
	# date_from, date_to = str2datetime(date_from), str2datetime(date_to)
	# for comment_file in comment_files:
	# 	print('=========================================')
	# 	print('Processing:', comment_file.split('/')[-1])
	# 	comment_df = load_df(comment_file, date_from, date_to)
	# 	lex_topic_page_time(comment_df.loc[
	# 		~comment_df.lex_found.isna(), # only rows with lex_found
	# 		['profile_id','name','datetime','lex_found','topics_found','page_group_name']])
	# 	page_hs_ratio(comment_df)
	# 	hspage_effect_on_comments(comment_df)
	# 	hsfirst_comment_effect_on_replies(comment_df)
	# 	page_reach(comment_df)

def load_df(comment_file, date_from, date_to):
	'''
	- Read comment file
	- Fix datetime column
	- Filter by date range to avoid comments beyond the date range
		- This happens when the data is downloaded after the date of posting
	'''
	# comment file
	comment_df = pd.read_csv(comment_file)
	comment_df['datetime'] = pd.to_datetime(comment_df.datetime)
	comment_df = comment_df.loc[np.logical_and(comment_df.datetime>date_from, comment_df.datetime<date_to), :]
	comment_df['likes'] = comment_df.likes.astype(int)
	comment_df['topics_found'] = [
		[] if na else [TYPE_DICT[a] for a in str(l).split('~')]
		for l, na in zip(comment_df.lex_found, comment_df.lex_found.isna())]

	# post file
	post_file = comment_file.split('/')
	post_file[-2] = 'posts'
	post_file = '/'.join(post_file)
	post_df = pd.read_csv(post_file, usecols=['page_group_name','post_url','lex_found','type'])
	# join
	comment_df = comment_df.merge(post_df, on='post_url', how='left', suffixes=('','_post'))
	comment_df = comment_df.merge(post_df, on='post_url', how='left', suffixes=('','_type'))
	comment_df['date'] = [pd.datetime(d.year, d.month, d.day) for d in comment_df.datetime]
	return comment_df


def lex_topic_page_time(comment_wlex):
	proflat, nameflat, dtflat, lexflat, topicsflat, hours, pages = [], [], [], [], [], [], []
	for pid, name, dt, lex, topics, page in zip(
		comment_wlex.profile_id, comment_wlex.name, comment_wlex.datetime, comment_wlex.lex_found,
		comment_wlex.topics_found, comment_wlex.page_group_name):
		lex = lex.split('~')
		for l, t in zip(lex, topics):
			proflat.append(pid)
			nameflat.append(name)
			dtflat.append(dt)
			hours.append(dt.hour)
			pages.append(page)
			lexflat.append(l)
			topicsflat.append(t)
	lex_topic_page_time_df = pd.DataFrame({
		'Profile ID': proflat,
		'Name': nameflat,
		'Hate Speech Phrase': lexflat,
		'Topic': topicsflat,
		'Page': pages,
		'DateTime': dtflat,
		'Hour': hours
	})
	lex_topic_page_time_df['Date'] = [
		pd.datetime(d.year, d.month, d.day)
		for d in lex_topic_page_time_df.DateTime]
	lex_topic_page_time_df['ISOWeek'] = lex_topic_page_time_df.Date
	save_dataframe(lex_topic_page_time_df, 'lex-topic-page-time')


 ######## Page HS Ratio ##################

def page_hs_ratio(comment_df):
	comment_df['has_lex'] = ~comment_df.lex_found.isna()
	lex_count = comment_df.groupby(['page_group_name','date','type'])['has_lex'].sum() 
	total = comment_df.groupby(['page_group_name','date','type'])['page_group_name'].count()
	total.name = 'total' 
	page_hs_ratio_df = pd.DataFrame([lex_count, total]).T
	page_hs_ratio_df['ratio'] = page_hs_ratio_df.has_lex / page_hs_ratio_df.total
	save_dataframe(page_hs_ratio_df, 'page-hs-ratio-stage', index=True)



def hspage_effect_on_comments(comment_df):
	'''
	Calculate the HS comments for posts with and without HS terms in it.
	w: with lex
	n: no lex
	'''
	posts_wlex = comment_df.loc[~comment_df.lex_found_post.isna(), :]
	posts_nlex = comment_df.loc[comment_df.lex_found_post.isna(), :]
	pwl_cwl = posts_wlex.lex_found.count()
	pwl_cnl = posts_wlex.shape[0] - pwl_cwl
	pnl_cwl = posts_nlex.lex_found.count()
	pnl_cnl = posts_nlex.shape[0] - pnl_cwl
	hspost_effect_df = pd.DataFrame({
		'post_has_lex': ['Post with HSL','Post with HSL','Post with no HSL','Post with no HSL'],
		'comment_has_lex': ['Comment with HSL','Comment with no HSL','Comment with HSL','Comment with no HSL'],
		'count': [pwl_cwl, pwl_cnl, pnl_cwl, pnl_cnl]
	})
	save_dataframe(hspost_effect_df, 'hspost-effect')


def hsfirst_comment_effect_on_replies(comment_df):
	'''
	This function might be written shorter. Not sure.
	'''
	# remove comments with no replies

	reply_df = comment_df.groupby(['post_id','c_id'])['c_id'].count()
	reply_df = reply_df[reply_df>1]
	# create new id for faster filters
	pc_ids = []
	for (post_id,c_id),_ in reply_df.iteritems():
		pc_ids.append(post_id + str(c_id).zfill(4))
	pc_ids = set(pc_ids)
	comment_df['pc_id'] = [p+str(c).zfill(4)
		for p,c in zip(comment_df.post_id, comment_df.c_id)]
	repdf = comment_df.loc[comment_df.pc_id.isin(pc_ids)]
	# get first comments & split them into 2 groups: with lex and with no lex
	nis0 = repdf.loc[repdf.n_id==0]
	first_comment_nl = nis0.loc[nis0.lex_found.isna()]
	first_comment_wl = nis0.loc[~nis0.lex_found.isna()]
	# grab replies data for calculations (this is actually what we want) 
	first_cwl = repdf.loc[np.logical_and(repdf.pc_id.isin(first_comment_wl.pc_id), repdf.n_id>0),:]
	first_cnl = repdf.loc[np.logical_and(~repdf.pc_id.isin(first_comment_wl.pc_id), repdf.n_id>0),:]
	# calculate stuff
	fcwl_nwl = first_cwl.lex_found.count()
	fcwl_nnl = first_cwl.shape[0] - fcwl_nwl
	fcnl_nwl = first_cnl.lex_found.count()
	fcnl_nnl = first_cnl.shape[0] - fcnl_nwl
	hsfirst_comment_effect = pd.DataFrame({
		'first_comment_has_lex': ['First Comment with HSL','First Comment with HSL','First Comment with no HSL','First Comment with no HSL'],
		'reply_has_lex': ['Reply with HSL','Reply with no HSL','Reply with HSL','Reply with no HSL'],
		'count': [fcwl_nwl, fcwl_nnl, fcnl_nwl, fcnl_nnl]
	})
	save_dataframe(hsfirst_comment_effect, 'hsfirst-comment-effect')


def page_reach(comment_df):
	page_reach_sr = comment_df.groupby(['page_group_name','date'])['profile_id'].nunique()
	page_reach_sr.name = 'count'
	save_dataframe(page_reach_sr, 'page-reach', index=True, sep='~')


def str2datetime(datetime_str):
	return pd.datetime(
		int(datetime_str[:4]), int(datetime_str[4:6]), int(datetime_str[6:]))










