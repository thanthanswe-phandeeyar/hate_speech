import os
import pandas as pd
import calendar
import sys
with open('MyanmarNLPTools') as f:
    sys.path.append(f.read().strip())
from MMCleaner import MMCleaner
CLN = MMCleaner()

LEX_FILE = '../data/lexicon.csv'

# def uniNorm(msgList):
#     '''
#     This function calls a `go` program to do the dirty work.
#     Temp files positions are at /home/bupi/Documents/pdy/hs/tmp/
#     '''
#     # msgList = [m.replace('\n', '<newline>') for m in msgList]
#     with open(INPUT_TMP, 'w') as f:
#         f.write('\n'.join(msgList))
#     os.system('{} {} {}'.format(GO_FILTER, INPUT_TMP, OUTPUT_TMP))
#     with open(OUTPUT_TMP) as f:
#         # return [l.strip().replace('<newline>', '\n') for l in f]
#         return [l.strip() for l in f]


def GeneratePostIds(postFileName, noOfPosts, zfillN=4):
    '''
    returns as list of str in the form <dateOfPostFile>_<serialNo>
    '''
    date = postFileName.split('_')[1].split('.')[0]
    return ['{}_{}'.format(date,str(k).zfill(zfillN)) for k in range(noOfPosts)]


def GenerateCommentIds(postId, df_cnid, zfillN=4):
    '''
    postId: ID of the post the comment xlsx comes from
    df_cnid: A dataframe with only `cid` and `nid`
    '''
    df_cnid['nId'] = df_cnid.nId.fillna('0') # nested id is empty for head comments
    df_cnid['nId'] = df_cnid.nId.astype(str)
    df_cnid['cId'] = [
        str(cid).zfill(zfillN) if nid=='0' else str(nid.split('-')[0]).zfill(zfillN)
        for cid,nid in zip(df_cnid.cId,df_cnid.nId)
    ]
    df_cnid['nId'] = [
        str(nid).zfill(zfillN) if nid=='0' else str(nid.split('-')[1]).zfill(zfillN)
        for nid in df_cnid.nId
    ]
    return df_cnid

# def LoadLexiconSet(hasDownloaded=False):
#     # load lexicon 
#     # download this again before running
#     assert hasDownloaded, 'Download the lexicon file first.'
#     lexdf = pd.read_csv(LEX_FILE, sep=',')
#     l1 = lexdf.label
#     l1 = list(l1.dropna())
#     l2 = lexdf.labelAlternativeSpelling
#     l2 = list(l2.dropna())
#     lexset = set([l.strip() for l in l1+l2])
#     return lexset

def LoadLexiconSet(take_last_ndates=False, n=None, has_downloaded=False):
    assert has_downloaded, 'Download the lexicon file first.'
    if take_last_ndates:
        assert isinstance(n, int) and n > 0, 'If `take_last_ndates` is True, please choose an integer `n>0`.'
    
    df = pd.read_csv(LEX_FILE)
    if take_last_ndates:
        df['date_added'] = df.date_added.fillna(df.date_added.values[-1])
        df['date_added'] = pd.to_datetime(df.date_added)
        dates = df.date_added.unique()
        dates.sort()
        lastndates = dates[-1*n:]
        lexdf = df.loc[df.date_added.isin(lastndates),:]
    else:
        lexdf = df
    l1 = lexdf.label
    l1 = list(l1.dropna())
    l2 = lexdf.label_alternative_spelling
    l2 = list(l2.dropna())
    lexset = set([CLN.web_clean(l.strip()) for l in l1+l2])
    if 'ခွေး' in lexset:
        lexset.remove('ခွေး')
    if 'ခေွး' in lexset:
        lexset.remove('ခေွး')
    return lexset

def LoadLexiconNorm():
    df = pd.read_csv(LEX_FILE)
    df['label'] = [l.strip() for l in df.label.astype(str)]
    df['label_alternative_spelling'] = [str(a).strip() for a in df.label_alternative_spelling]
    norm_dict = {l:l if a=='nan' or len(a)==0 else a for l,a in zip(df.label, df.label_alternative_spelling)}
    norm_dict.update({a:a for a in df.label_alternative_spelling.dropna().unique()})
    return norm_dict

def FindLexicons(textList, lexset):
    '''
    textList: list of strings, word segmented and tokenizable by space
    returns: a list of '~' separated strings containing found lexicon
    '''
    return [
        '~'.join(lexset.intersection(set(str(msg).split())))
        for msg in textList
    ]


def LoadLexTopicDict():
    dx = pd.read_csv(LEX_FILE)
    tmp = dx.dropna(subset=['label','type'])

    tmp['label'] = [CLN.web_clean(l) for l in tmp.label]
    tmp['type'] = [CLN.web_clean(l) for l in tmp.type]

    type_dict = {k:v for k,v in zip(tmp.label, tmp.type)}
    
    tmp = dx.dropna(subset=['label_alternative_spelling'])
    tmp['label_alternative_spelling'] = [
        CLN.web_clean(l) for l in tmp.label_alternative_spelling]
    type_dict.update({
        k:v for k,v in zip(tmp.label_alternative_spelling, tmp.type)})
    type_dict.update({'nan':'Unknown'})
    return type_dict


def CreateFileName4ProcessedCommentFile(originalFileName):
    '''
    originalFileName looks like this
    '../data/exportcomments-outputs/23_25032020/comments_1585130715642.xlsx'
    '''
    ofn = originalFileName.split('/')
    path = '/'.join(ofn[:-1]) + '/processed'
    newfilename = ofn[-1].split('.')[0] + '.csv'
    if not os.path.isdir(path):
        os.mkdir(path)
    return '{}/{}'.format(path, newfilename)
