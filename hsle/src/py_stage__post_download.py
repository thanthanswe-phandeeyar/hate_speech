import pandas as pd
import json
import requests
from tqdm import tqdm
import time
import sys
with open('MyanmarNLPTools') as f:
    sys.path.append(f.read().strip())
from MMSegmentor import MMSegmentor

seg = MMSegmentor('../../../lib/MyanmarNLPTools/')
with open('../data/covid.csv') as f:
    covid = set([l.strip() for l in f])

with open('../../hsmai/src/crowdtangle-apikey') as f:
    apikey = f.read().strip()
start_date = '2020-05-18'
end_date = '2020-05-21'

NUMBER_OF_API_CALLS = 10

if __name__=='__main__':
    k = 0

    offset = 100*k
    print('Current OFFSET:', offset)
    sort_by = 'overperforming'

    url = 'https://api.crowdtangle.com/posts?token={}&startDate={}&endDate={}&sortBy={}&count=100&offset={}'.format(
        apikey, start_date, end_date, sort_by, offset
    ) # count=100 is maximum
    res = requests.get(url)
    x = json.loads(res.text)
    x = pd.json_normalize(x['result']['posts'])

    k += 1
    errs = []
    dflist = []
    dflist.append(x)
    while k < 100:
        offset = 100*k
        print('Current OFFSET:', offset)
        url = 'https://api.crowdtangle.com/posts?token={}&startDate={}&sortBy={}&count=100&offset={}'.format(
            apikey, start_date, sort_by, offset
        )
        res = requests.get(url)
        if res.status_code==200:
            x = json.loads(res.text)
            x = pd.json_normalize(x['result']['posts'])
            if x.shape[0] > 0:
                dflist.append(x)
                k += 1
            else:
                break
        elif res.status_code==429:
            time.sleep(65) # Wait 1 minute (5s) due to CT API limit, and retry the call again
        else:
            errs.append((k, res))
            k += 1
