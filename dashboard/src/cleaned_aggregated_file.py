import os
import pandas as pd 
import numpy as np 
from glob import glob
from tqdm import tqdm
import csv
from pathlib import Path



def clean_aggregated_data(split_csv_path,split_file_name):
    cleaned_aggregated =final_aggregated_folder+'/cleaned-aggregated/'
    if not os.path.exists(cleaned_aggregated): 
        cleaned_path =os.makedirs(cleaned_aggregated)
        csv_file=Path(str(cleaned_path)+split_file_name)
    csv_file=Path(cleaned_aggregated+split_file_name)
    data_store =[]
    with open(split_csv_path, "r") as f:
        reader = csv.reader(f, delimiter="~")
        for i, line in enumerate(reader):
            str_line=line[0]
            if not "Offical Close Group" in str_line:
                data_store.append(line)
                df = pd.DataFrame(data_store)
                # Saved updated file instead of old file in the same directory
                df.to_csv(csv_file,index=False, header=False,sep='~')

    return df
    
aggregated_folder =sorted(glob('../../dashboard/clean-data/aggregated/*'))
final_aggregated_folder = max(aggregated_folder, key=os.path.getmtime)
files = glob(final_aggregated_folder+'/*.csv')

for f in tqdm(files):
    split_csv_file = str(f).split('/')[6]
    if split_csv_file=='page-hs-ratio-stage.csv': 
        clean_aggregated_data(f,split_csv_file)
    elif split_csv_file=='hsfirst-comment-effect.csv':
        clean_aggregated_data(f,split_csv_file)
    elif split_csv_file=='hspost-effect.csv':
        clean_aggregated_data(f,split_csv_file)
    elif split_csv_file=='lex-topic-page-time.csv':
        clean_aggregated_data(f,split_csv_file)
    else:
        clean_aggregated_data(f,split_csv_file)