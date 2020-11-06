import pandas as pd
import numpy as np
from glob import glob
from tqdm import tqdm
import json
import CrowdTangleExportCommentsTools.HsleCandidateGenerationUtils as hsle

with open('_current_data_.json') as f:
    CURRENT_DATA = json.load(f)

SEP = CURRENT_DATA['sep']
DESIREDN = int(CURRENT_DATA['desired_number_of_comments'])
DATE_RANGE = CURRENT_DATA['daterange']

if CURRENT_DATA['pages_groups']=='groups':
    COMMENT_FILES_FOLDER = '../data/exportcomments-outputs/groups_{}'.format(DATE_RANGE)
    POST_FILE = '../data/crowdtangle-groups/processed_{}.csv'.format(DATE_RANGE)
else:
    COMMENT_FILES_FOLDER = '../data/exportcomments-outputs/{}'.format(DATE_RANGE)
    POST_FILE = '../data/crowdtangle-pages/processed_{}.csv'.format(DATE_RANGE)
URL_PREFIX = 'https://www.facebook.com/profile.php?id='
print('Comment Folder:', COMMENT_FILES_FOLDER)
MERGED_FILE = COMMENT_FILES_FOLDER + '/processed/merged.csv'

# Read Keywords
with open('../data/covid.csv') as f:
    COVLEX = list(set([''.join(l.strip().split()).lower() for l in f]))
print('#Covid Keywords:', len(COVLEX))

LEXSET = hsle.LoadLexiconSet(take_last_ndates=False, n=None, has_downloaded=True)
print('#HS Lexicon:', len(LEXSET))

# Read Priority FB Pages
with open('../data/fbpage_priority.csv') as f:
    FBPAGES = tuple([l.strip() for l in f])
print('#Priority FB Pages:', len(FBPAGES))

msg_col = 'MsgUni'

if __name__=='__main__':
    all_files =  glob(COMMENT_FILES_FOLDER+'/processed/comments_*.csv')
    print('#Comment Files:', len(all_files))

    postdf = pd.read_csv(POST_FILE, sep=SEP)
    # postdf = pd.read_csv(POST_FILE)
    print('Post DF Shape:', postdf.shape)

    print('Add PostURL to Comment csv by matching `commentsFile` field in `postdf` ...')
    for f in tqdm(all_files):
        commentFileId = f.split('/')[-1].split('.')[0]
        commentFile = '{}/{}.xlsx'.format(COMMENT_FILES_FOLDER, commentFileId)
        tmp = pd.read_csv(f, sep=SEP)
        tmp['PostURL'] = postdf.loc[postdf.commentsFile==commentFile,'URL'].values[0]
        tmp.to_csv(f, index=False, sep=SEP)

    print('Merge all csvs ...')
    df_from_each_file = (pd.read_csv(f, sep=SEP) for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index=True)
    df_merged.to_csv(MERGED_FILE, index=False)

    print('Load merged df ...')
    df = pd.read_csv(COMMENT_FILES_FOLDER+'/processed/merged.csv')
    # df['atleast1MM'] = df.atleast1MM.bool() # TODO?
    print('Merged DF Shape before filters:', df.shape)
    df = df.loc[df.atleast1MM]
    df = df.loc[df.char_pass]
    df.drop_duplicates(msg_col, inplace=True)
    print('Merged DF Shape after dropping duplicates and filters:', df.shape)
    print('Merged DF Columns:')
    print(df.columns)

    print('Finding Covid Keywords in Comments ...')
    x = ['~'.join(set([c for c in COVLEX if c in m.lower()])) for m in tqdm(df[msg_col])]
    df['CovFound'] = [l if len(l)>0 else np.NaN for l in x]
    print('#Comments w/ COVLEX:', sum(~df.CovFound.isna()))
    dfwcov = df.loc[~df.CovFound.isna(),:]

    print('Finding Comments from Priority FB Pages ...')
    mask = [str(url).startswith(FBPAGES) for url in tqdm(df.PostURL)]
    print('#Comments from Priority FB Pages:', sum(mask))
    dfwpg = df.loc[mask, :]

    print('Finding Commments w/ HS Lex ...')
    dfwlex = df.loc[~df.LexFound.isna(),:]
    del df
    # Not sure the purpose of the following line lolz.
    dfwlex = dfwlex.loc[[any(l in lf for l in LEXSET) for lf in dfwlex.LexFound],:]
    print('#Comments w/ HS Lex:', dfwlex.shape)
    
    dfj = dfwlex.merge(dfwcov, on=['postId','cId','nId'], how='inner')
    print('Len of intersection of HS comments & Covid comments:', dfj.shape[0])
    # fix col names after merging
    dfj = dfj[[c for c in dfj.columns if not c.endswith('_y')]]
    dfj.columns = [c.rstrip('_x') for c in dfj.columns]

    print('Getting more data from HS comments if there is not enough ...')
    # remove already selected
    # `bigId` is to join
    dfwlex['bigId'] = ['{}-{}-{}'.format(p,c,n) for p,c,n in zip(dfwlex.postId,dfwlex.cId,dfwlex.nId)]
    dfj['bigId'] = ['{}-{}-{}'.format(p,c,n) for p,c,n in zip(dfj.postId,dfj.cId,dfj.nId)]
    dfdiff = dfwlex.loc[~dfwlex.bigId.isin(dfj.bigId),:] # only dfwlex items that are not in dfj
    print('#HS Comments not in Intersection above:', dfdiff.shape)

    print('Sort them by #HS found ...')
    dfdiff['lex_count'] = [l.count('~')+1 for l in dfdiff.LexFound]
    dfdiff.sort_values('lex_count', ascending=False, inplace=True)

    dfdiff = dfdiff[dfj.columns]
    # dfj_ = dfj
    dfj = pd.concat([dfj, dfdiff.iloc[:DESIREDN-dfj.shape[0],:]])
    print('Total #Lines after Combining Intersection with Added Lex:', dfj.shape)

    print('Fixing date and time columns ...')
    cols = ['LexFound','postId','cId','nId',msg_col,'Profile ID','PostURL','Date','CovFound']
    dfx = dfj.loc[:,cols]
    dfx['date'] = [d.split()[0] for d in dfx.Date]
    dfx['time'] = [d.split()[1] for d in dfx.Date]
    dfx.drop('Date', axis=1, inplace=True)
    dfx.drop_duplicates([msg_col], inplace=True)
    dfx['ProfileUrl'] = ['{}{}'.format(URL_PREFIX, i.split()[-1]) for i in dfx['Profile ID']]
    print('Shape after Fixing:', dfx.shape)

    print('Flattening the DF since lex_found is a "list" ...')
    dflat = pd.DataFrame(index=dfx.columns)
    dfextra = pd.DataFrame(index=dfx.columns)
    total = 0
    for k in tqdm(range(dfx.shape[0])):
        if '~' not in dfx.iloc[k,0]: # 0 is LexFound
            dflat[k] = dfx.iloc[k,:].values
            total += 1
        else:
            lexes = dfx.iloc[k,0].split('~')
            tmp = dfx.iloc[k,:]
            for lex in lexes:
                tmp['LexFound'] = lex
                K = dfextra.columns.max()+1
                K = 0 if np.isnan(K) else K
                dfextra[K] = tmp
                total += 1
            del tmp
    dflat = dflat.T
    dfextra = dfextra.T

    dflat = pd.concat([dflat,dfextra])
    print('Flattened DF Shape:', dflat.shape)
    print('Save All First at', '../data/to-annotate/{}_all.csv'.format(DATE_RANGE))
    dflat.to_csv(
        '../data/to-annotate/{}_all.csv'.format(DATE_RANGE),
        index=False)

    mask = [url.startswith(FBPAGES) for url in dflat.PostURL]

    print('Combining with Priority FB Pages ...')
    dfwpg = dfwpg[['LexFound','postId','cId','nId',msg_col,'Profile ID','PostURL','Date']]
    dfwpg['date'] = [d.split()[0] for d in dfwpg.Date]
    dfwpg['time'] = [d.split()[1] for d in dfwpg.Date]
    dfwpg['ProfileUrl'] = ['{}{}'.format(URL_PREFIX, i.split()[-1]) for i in dfwpg['Profile ID']]
    print('#Comments from Priority FB Pages:', dfwpg.shape)
    
    dffinal = pd.concat([dflat, dfwpg])
    print(dffinal.shape)
    dffinal.drop_duplicates(msg_col, inplace=True)
    print(dffinal.shape)

    dffinal.iloc[:DESIREDN,:].sort_values(['postId','cId','nId'], ascending=True).to_csv(
        '../data/to-annotate/{}_final.csv'.format(DATE_RANGE),
        index=False)
    print('===== Final File Saved At',
        '../data/to-annotate/{}_final.csv'.format(DATE_RANGE),
        '=====')
