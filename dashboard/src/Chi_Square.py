''''

Retrieve HSFIRST_COMMENT_EFFECT and HSPOST_EFFECT tables from bigquery.
Import scipy library to find out chi square value and save as a csv file

'''
#modules
import pandas as pd 
import google.cloud
from google.cloud import bigquery
from google.oauth2 import service_account
from scipy.stats import chi2_contingency
import csv
from glob import glob
import os 



credentials = service_account.Credentials.from_service_account_file(
    'hatespeech-dashboard-fb27494d50bb.json')


#variables
project_id='hatespeech-dashboard'
bq_dataset = "HS_DATASET"

client = bigquery.Client(credentials= credentials,project=project_id)
dataset_ref= client.dataset(bq_dataset)


# HSFIRST_COMMENT_EFFECT Function and Query
def bq_chi2_hsfirst_comment_effect(sql):
	query = client.query(sql)
	results = query.result()
	return results.to_dataframe()

bq_chi_hsfirst = """
					SELECT first_comment_has_lex,reply_has_lex,SUM(COUNT) as COMMENT_COUNT 
					FROM `hatespeech-dashboard.HS_DATASET.HSFIRST_COMMENT_EFFECT` 
					Group by first_comment_has_lex,reply_has_lex
	
				"""

df_hsfirst_comment_effect = bq_chi2_hsfirst_comment_effect(bq_chi_hsfirst)

# HSPOST EFFECT Function And Query 
def bq_chi2_hspost_effect(sql):
	query = client.query(sql)
	results = query.result()
	return results.to_dataframe()

bq_chi_hspost = """
						SELECT post_has_lex,comment_has_lex,SUM(COUNT) AS POST_COUNT
						FROM `hatespeech-dashboard.HS_DATASET.HSPOST_EFFECT`
						Group by post_has_lex,comment_has_lex
			
				"""

df_hspost_effect = bq_chi2_hspost_effect(bq_chi_hspost)

# #Calculate CHI_SQUARE Value 
chi2_comment = list(chi2_contingency(pd.pivot_table(data = df_hsfirst_comment_effect,index=['first_comment_has_lex','reply_has_lex'])['COMMENT_COUNT'].unstack())[:3])[:2]

chi2_post = list(chi2_contingency(pd.pivot_table(data = df_hspost_effect,index=['post_has_lex','comment_has_lex'])['POST_COUNT'].unstack())[:3])[:2]
		    
chi_square  = chi2_comment+chi2_post

aggregated_folder =sorted(glob('../../dashboard/clean-data/aggregated/*'))
final_aggregated_folder = max(aggregated_folder, key=os.path.getmtime)
chi_square = pd.DataFrame([chi_square], columns=['chi2', 'p','chi2_nested','p_nested'])
chi_square.to_csv(final_aggregated_folder+'/cleaned-aggregated/'+'chi_square.csv',mode='w',index=False)

print("Done")