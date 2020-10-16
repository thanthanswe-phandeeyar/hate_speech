import pandas as pd
import numpy as np
from tqdm import tqdm

PATH_TO_HSLE = '../../hsle'
from CrowdTangleExportCommentsTools import HsleCandidateGenerationUtils as hsle
from MyanmarNLPTools import MMTools
from MyanmarNLPTools.MMCleaner import MMCleaner
CLN = MMCleaner()

class HateSpeechData:
	
	# class variables
	LEX = hsle.LoadLexiconSet(False, None, True)
	if 'ခွေး' in LEX:
		LEX.remove('ခွေး')
	if 'ေခွး' in LEX:
		LEX.remove('ေခွး')
	LEX_NORM_DICT = hsle.LoadLexiconNorm()
	
	POST_REL_PATH = PATH_TO_HSLE + '/data/crowdtangle-pages'
	GROUP_REL_PATH = PATH_TO_HSLE + '/data/crowdtangle-groups'
	POST_PREFIX = 'processed'
	POST_SEP = '~'
	CLEAN_PATH = '../clean-data'
	COMMENT_COLS2LOAD = [
		'postId',
		'cId',
		'nId',
		'Name (click to view profile)',
		'Profile ID',
		'Date',
		'Likes',
		'MsgUniSeg',
		'LexFound',
		'PostURL'
	]
	COMMENT_COLS2LOAD_X = [
		'postId',
		'cId',
		'nId',
		'Name (click to view profile)',
		'Profile ID',
		'Date',
		'Likes',
		'MsgUni',
		'LexFound',
		'PostURL'
	]
	COMMENT_COL_NAMES = [
		'post_id',
		'c_id',
		'n_id',
		'name',
		'profile_id',
		'datetime',
		'likes',
		'comment_message',
		'lex_found',
		'post_url'
	]
	PAGE_COLS2LOAD = [
		'Page Name',
		'URL',
		'Likes',
		'Type',
		'Comments',
		'Shares',
		'Love',
		'Wow',
		'Haha',
		'Sad',
		'Angry',
		'MsgUniCleanSeg'
	]
	GROUPS_COLS2LOAD = [
		'Group Name',
		'URL',
		'Likes',
		'Type',
		'Comments',
		'Shares',
		'Love',
		'Wow',
		'Haha',
		'Sad',
		'Angry',
		'MsgUniCleanSeg'
	]
	POST_COL_NAMES = 'page_group_name	post_url	 comments	type shares	love	wow	haha	sad	angry likes post_message'.split()
	

	def __init__(self, comment_files):
		self.COMMENT_FILES = comment_files

		# debug variables
		self.POST_FILES = []

	def run1(self, comment_file):
		
		comment_df, post_df = self.prepare_dataframe(comment_file)
		comment_df, post_df = self.update_lex_found(comment_df, post_df)
		self.save(comment_file, comment_df, post_df)
	
	def run(self):
		for comment_file in tqdm(self.COMMENT_FILES):
			print('Processing:', comment_file)
			self.run1(comment_file)

	def extract_date_range(self, comment_file):
		return comment_file.split('/')[-3].lstrip('groups_')

	def prepare_dataframe(self, comment_file):
		# load comment dataframe
		# try:
		comment_df = pd.read_csv(
			comment_file,
			usecols=HateSpeechData.COMMENT_COLS2LOAD)
		# except:
		#     comment_df = pd.read_csv(
		#         comment_file,
		#         usecols=HateSpeechData.COMMENT_COLS2LOAD_X)
		# standardize column names
		comment_df = comment_df[HateSpeechData.COMMENT_COLS2LOAD]
		comment_df.columns = HateSpeechData.COMMENT_COL_NAMES
		comment_df['profile_id'] = comment_df.profile_id.apply(
			lambda x: str(x).split()[-1])
		comment_df['name'] = comment_df.name.astype(str).apply(
			CLN.web_clean).apply(
				MMTools.normalize_unicode)

		# load posts dataframe
		if 'groups' in comment_file: # group
			post_file = '{}/{}_{}.csv'.format(
				HateSpeechData.GROUP_REL_PATH,
				HateSpeechData.POST_PREFIX,
				self.extract_date_range(comment_file))
			try:
				post_df = pd.read_csv(
					post_file,
					sep=HateSpeechData.POST_SEP,
					usecols=HateSpeechData.GROUPS_COLS2LOAD)
			except:
				post_df = pd.read_csv(
					post_file,
					sep=',',
					usecols=HateSpeechData.GROUPS_COLS2LOAD)
			# standardize column names
			post_df = post_df[HateSpeechData.GROUPS_COLS2LOAD]
		else: # page
			post_file = '{}/{}_{}.csv'.format(
				HateSpeechData.POST_REL_PATH,
				HateSpeechData.POST_PREFIX,
				self.extract_date_range(comment_file) # gives datetime id, eg. 20200323_2020325
				)
			try:
				post_df = pd.read_csv(
					post_file,
					sep=HateSpeechData.POST_SEP,
					usecols=HateSpeechData.PAGE_COLS2LOAD)
			except:
				post_df = pd.read_csv(
					post_file,
					sep=',',
					usecols=HateSpeechData.PAGE_COLS2LOAD)
			# standardize column names
			post_df = post_df[HateSpeechData.PAGE_COLS2LOAD]
		# save for debugging
		self.POST_FILES.append(post_file)
		post_df.columns = HateSpeechData.POST_COL_NAMES # column name change
		# uninorm
		post_df['page_group_name'] = [MMTools.normalize_unicode(l) for l in post_df.page_group_name]
		return comment_df, post_df

	def update_lex_found(self, comment_df, post_df):
		# lex_found is replaced with results from new lexicon
		# this is needed because the lexicon is always changing
		comment_df['lex_found'] = [
			set(str(l).split()).intersection(HateSpeechData.LEX)
			for l in comment_df.comment_message]
		# standardize format with ~ separator
		comment_df['lex_found'] = [
			np.nan if len(l)==0 else '~'.join(
				HateSpeechData.LEX_NORM_DICT[m] if m in HateSpeechData.LEX_NORM_DICT.keys() else m for m in l)
			for l in comment_df.lex_found]

		# same as comments, for posts
		post_df['lex_found'] = [
			set(str(l).split()).intersection(HateSpeechData.LEX)
			for l in post_df.post_message]
		post_df['lex_found'] = [
			np.nan if len(l)==0 else '~'.join(l)
			for l in post_df.lex_found]
		return comment_df, post_df
	
	def save(self, comment_file, comment_df, post_df):
		# try:
		date_range = self.extract_date_range(comment_file)
		file_name = 'group_{}'.format(date_range) if 'group' in comment_file else date_range
		comment_df.to_csv(
			'{}/comments/{}.csv'.format(HateSpeechData.CLEAN_PATH, file_name),
			index=False)
		post_df.to_csv(
			'{}/posts/{}.csv'.format(HateSpeechData.CLEAN_PATH, file_name),
			index=False)
		print('Files saved for {}.'.format(file_name))
		# except:
			# print('error: Files probably not saved for {}.'.format(file_name))
