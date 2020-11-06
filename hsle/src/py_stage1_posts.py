import json
import pandas as pd
from tqdm import tqdm
from time import time
from MyanmarNLPTools import MMTools
from MyanmarNLPTools.MMSegmentor import MMSegmentor
from MyanmarNLPTools.MMCleaner import MMCleaner
CLN = MMCleaner()
SEG = MMSegmentor()

import CrowdTangleExportCommentsTools.HsleCandidateGenerationUtils as hsle
from CrowdTangleExportCommentsTools.ProcessTexts import generate_post_ids

with open('_current_data_.json') as f:
    CURRENT_DATA = json.load(f)

SEP = CURRENT_DATA['sep']
PAGE_GROUP_PATH = '../data/crowdtangle-{}'.format(CURRENT_DATA['pages_groups'])
DATE_RANGE = CURRENT_DATA['daterange']
POST_FILE = '{}/processed_{}.csv'.format(PAGE_GROUP_PATH, DATE_RANGE)
PREFIX = 'groups_' if 'groups' in PAGE_GROUP_PATH else ''

if __name__=='__main__':
    postdf = pd.read_csv(POST_FILE, sep=SEP)
    print('Post DF Shape:', postdf.shape)
    postdf['PostId'] = generate_post_ids(
        postFileName=POST_FILE,
        noOfPosts=postdf.shape[0],
        zfillN=4)
    postdf['MessageUni'] = postdf.Message.astype(str).apply(MMTools.normalize_unicode)
    lexset = hsle.LoadLexiconSet(False, None, True)
    print('Number of HS lexicon:', len(lexset))
    print('Running word segmentation...')
    x = [
        SEG.word_segment(
            CLN.web_clean(t), additionalWordList=list(lexset)
        ) for t in tqdm(postdf.MessageUni)
    ]
    postdf['MsgUniCleanSeg'] = [' '.join(i) for i in x]
    postdf.to_csv(POST_FILE, sep=SEP, index=False)
    print('File saved at {}'.format(POST_FILE))
