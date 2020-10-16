import pandas as pd
from exportcomments import ExportComments
from tqdm import tqdm
import requests
import time
import os
import json



current_milli_time = lambda: int(round(time.time() * 1000))

with open('exportcomments_api_key.txt') as f:
    APIKEY = f.read().strip()
EX = ExportComments(APIKEY)

with open('_current_data_.json') as f:
    CURRENT_DATA = json.load(f)


SEP = CURRENT_DATA['sep']
PAGE_GROUP_PATH = '../data/crowdtangle-{}'.format(CURRENT_DATA['pages_groups'])
DATE_RANGE = CURRENT_DATA['daterange']
POST_FILE = '{}/{}.csv'.format(PAGE_GROUP_PATH, DATE_RANGE)
PREFIX = 'groups_' if 'groups' in POST_FILE else ''

COMMENT_FOLDER = '../data/exportcomments-outputs/{}{}'.format(
    PREFIX,
    DATE_RANGE)
print(COMMENT_FOLDER)
BASE_URL = 'https://exportcomments.com'


if __name__=='__main__':
    postsdf = pd.read_csv(POST_FILE, sep=SEP)
    print('Post DF Shape:', postsdf.shape)

    print('Calling API...')
    responseList = []
    error_urls = {}
    for k, url in tqdm(enumerate(postsdf.URL)):
        try:
            responseList.append(EX.exports.create(url=url, replies='true', twitterType=None))
        except:
            print('error')
            responseList.append('error')
            error_urls[k] = url
    with open('{}/exportcomments_uniqueIds/{}.csv'.format(PAGE_GROUP_PATH, DATE_RANGE) , 'w') as f:
        f.write('\n'.join('error' if isinstance(r, str) else r.body['uniqueId'] for r in responseList))
    print('ExportComments Unique IDs saved at {}'.format(
        '{}/exportcomments_uniqueIds/{}.csv'.format(PAGE_GROUP_PATH, DATE_RANGE)))
