import pandas as pd
import sys
from tqdm import tqdm
import json

from CrowdTangleExportCommentsTools import HsleCandidateGenerationUtils as hsle
import HateSpeechData as hsd
from glob import glob


from pathlib import Path


files = glob('../../hsle/data/exportcomments-outputs/*/processed/merged.csv')
files.sort()

with open('../../hsle/src/_current_data_.json') as f:
  data = json.load(f)
  daterange=data['daterange']
  
for f in tqdm(files):
	split_file = str(f).split('/')[5]
	if split_file.split("_")[0]=="groups":
		split_file =split_file.split('_')[1]+'_'+split_file.split('_')[2]
		if split_file==daterange:
			file_check =glob(f)
			print("File Check : ", file_check)
			data = hsd.HateSpeechData(file_check)
			data.run()
	else:
		split_file =str(f).split('/')[5]
		if split_file==daterange:
			file_check =glob(f)
			print("File Check : ", file_check)
			data = hsd.HateSpeechData(file_check)
			data.run()
		


