from importlib import reload
from tqdm import tqdm
import HateSpeechAggregator as hsa
from glob import glob
from datetime import datetime
import json
import os
import pandas as pd


reload(hsa);


'''
	Comments files
'''


"""
Get date range from current_data json file , check its value with ((comments file) date value.

"""

with open('../../hsle/src/_current_data_.json') as f:
	data = json.load(f)

	daterange =data['daterange']

files = glob('../clean-data/comments/*.csv')
files.sort()

for f in tqdm(files):
	split_file = str(f).split('/')[3]
	date_file=split_file.split(".")[0]
	if date_file.split("_")[0]=="group":
		date_file =date_file.split('_')[1]+'_'+date_file.split('_')[2]
		if date_file==daterange:
				file_check =glob(f)
				hsa.run(file_check)
	else:
		date_file =date_file
		if date_file==daterange:
				file_check =glob(f)
				hsa.run(file_check)

