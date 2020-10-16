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

    # Create comment folder if not exists
    if not os.path.isdir(COMMENT_FOLDER):
        os.mkdir(COMMENT_FOLDER)
    assert os.path.isdir(COMMENT_FOLDER)

    status = []
    downloadNow = True
    fileNames = []

    with open('{}/exportcomments_uniqueIds/{}.csv'.format(PAGE_GROUP_PATH, DATE_RANGE)) as f:
        uniqueIds = [l.strip() for l in f]
    t = EX.exports.check(uniqueId=uniqueIds[-1])
    s = t.body[0]['status']

    postsdf = pd.read_csv(POST_FILE, sep=SEP)

    #assert s, 'Data download is not ready. Wait 15 minutes and run again.'
    for _id in tqdm(uniqueIds): # if reloaded unique ids from file
        try:
            t = EX.exports.check(uniqueId=_id)
            s = t.body[0]['status']
            status.append(s)
            if s: # download
                url = BASE_URL + t.body[0]['downloadUrl']
                r = requests.get(url)
                
                filename = '{}/comments_{}.xlsx'.format(COMMENT_FOLDER, current_milli_time())
                with open(filename, 'wb') as f:
                    f.write(r.content)
                fileNames.append(filename)
            else:
                fileNames.append('error')
        except:
            fileNames.append('error')

    postsdf['commentsFile'] = fileNames + ['error']*(postsdf.shape[0]-len(fileNames))
    postsdf.to_csv(
        '{}/processed_{}.csv'.format(PAGE_GROUP_PATH, DATE_RANGE),
        sep=SEP,
        index=False)
    if not os.path.isdir(COMMENT_FOLDER + '/processed'):
        os.mkdir(COMMENT_FOLDER + '/processed')
