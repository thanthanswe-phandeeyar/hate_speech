import pandas as pd
import numpy as np
from time import time
import re
from MyanmarNLPTools.MMSegmentor import MMSegmentor
from MyanmarNLPTools.MMCleaner import MMCleaner
from MyanmarNLPTools import MMTools
import CrowdTangleExportCommentsTools.HsleCandidateGenerationUtils as hsle
from tqdm import tqdm

class CommentsProcessing:
  '''
  cdf: Dataframe of comment file
  '''
  def __init__(self, postFile, sep=',', cmtFileColName='commentsFile'):
    '''
    cmtFileColName: Name of the column with comment files
    '''
    self.SEP = sep

    self.POSTFILE = postFile
    self.POSTDF = pd.read_csv(self.POSTFILE, sep=self.SEP)
    print('Shape of postFile:', self.POSTDF.shape)
    self.CMTCOL = cmtFileColName
    self.LEXSET = hsle.LoadLexiconSet(take_last_ndates=False, n=None, has_downloaded=True)
    print('Number of terms in current lexicon:', len(self.LEXSET))
    self.NUMBER_OF_CHARACTERS_MINIMUM = np.array([
      len(''.join(t.split())) for t in self.LEXSET
    ]).mean()
    print('Current character threshold for filtering:',
      self.NUMBER_OF_CHARACTERS_MINIMUM)

    self.FIND_MM = re.compile(r'[\u1000-\u109F]+')

    self.SEGMENTOR = MMSegmentor()
    self.CLEANER = MMCleaner()

    self.erredCommentFiles = []

  def Run(self):
    '''
    This function loops through all xlsx files in postFile and calls everything
    to process all comments.
    Run posts `i` through `j`
    '''
    for k, (postId, commentFile) in tqdm(enumerate(zip(self.POSTDF.PostId, self.POSTDF[self.CMTCOL]))):
      try:
        cdf = pd.read_excel(commentFile)
        print('pd.read_excel done')
        print('----- LINES:', cdf.shape[0], '-----')
        cdf = self.StructureAndGiveIds(cdf, postId)
        print('StructureAndGiveIds done')
        cdf = self.NCharsPass(cdf)
        print('NCharsPass done')
        cdf = self.UnicodeNormalize(cdf)
        print('UnicodeNormalize done')
        cdf = self.MatchMMChar(cdf)
        print('MatchMMChar done')
        # This step saves the file because this step takes a while and in case next step raises exceptions.
        cdf = self.Segment(cdf, commentFile, DEBUG=False)
        print('Segment done')
        # This step saves the file too.
        self.FindLexicon(cdf, commentFile)
      except Exception as ex:
        print(k, ex)
        self.erredCommentFiles.append((postId, commentFile))
        continue

  def Debug(self):
    '''
    This function loops through all xlsx files in postFile and calls everything
    to process all comments.
    '''
    for postId, commentFile in tqdm(zip(self.POSTDF.PostId, self.POSTDF[self.CMTCOL])):
      try:
        cdf = pd.read_excel(commentFile)
        print('pd.read_excel done')
        cdf = self.StructureAndGiveIds(cdf, postId)
        print('StructureAndGiveIds done')
        cdf = self.NCharsPass(cdf)
        print('NCharsPass done')
        cdf = self.UnicodeNormalize(cdf)
        print('UnicodeNormalize done')
        cdf = self.MatchMMChar(cdf)
        print('MatchMMChar done')
        # This step saves the file because this step takes a while and in case next step raises exceptions.
        cdf = self.Segment(cdf, commentFile, DEBUG=True)
        print('Segment done')
        # This step saves the file too.
        self.FindLexicon(cdf, commentFile)
        print('FindLexicon done')
      except:
        self.erredCommentFiles.append((postId, commentFile))
        continue

  def StructureAndGiveIds(self, cdf, postId):
    cdf.columns = ['cId','nId'] + list(cdf.iloc[4,2:]) #comment id, nested id
    cdf = cdf.loc[5:,:]
    cniddf = hsle.GenerateCommentIds(postId, cdf.loc[:,['cId','nId']])
    cdf['postId'] = postId
    cdf[['cId','nId']] = cniddf
    cdf['Comment'] = cdf.Comment.astype(str)
    return cdf

  def NCharsPass(self, cdf):
    # TODO: Be careful with column names
    cdf['char_pass'] = [
      len(''.join(str(t).split()))>self.NUMBER_OF_CHARACTERS_MINIMUM
      for t in cdf.Comment]
    return cdf

  def UnicodeNormalize(self, cdf):
    t0 = time()
    cdf['MsgUni'] = [MMTools.normalize_unicode(l) for l in cdf.Comment]
    print('Time taken for unicode normalization:', time()-t0, 'seconds')
    return cdf

  def MatchMMChar(self, cdf):
    '''
    This function only adds a new column with boolean values
    Filtering will be done at word association steps in the next STAGE (STAGE 3)
    '''
    cdf['atleast1MM'] = [True if self.FIND_MM.findall(t) else False for t in cdf.MsgUni]
    return cdf

  def Segment(self, cdf, commentFile, DEBUG):
    print('Doing word segmentation...')
    print('DEBUG:', DEBUG)
    print('This will take a few minutes to a couple of hours...')
    if DEBUG:
      cdf = cdf.iloc[:5, :]
    x = [
      self.SEGMENTOR.word_segment(
        self.CLEANER.web_clean(t), additionalWordList=list(self.LEXSET)
      ) for t in cdf.MsgUni
    ]
    cdf['MsgUniSeg'] = [' '.join(t) for t in x]
    print('Word segmentation done!')
    self.SaveCsv(cdf, commentFile)
    return cdf

  def FindLexicon(self, cdf, commentFile):
    cdf['LexFound'] = hsle.FindLexicons(cdf.MsgUniSeg, self.LEXSET)
    saveTo = hsle.CreateFileName4ProcessedCommentFile(commentFile)
    cdf.to_csv(saveTo, sep=self.SEP, index=False)
    print('Lexicon finding done!')
    self.SaveCsv(cdf, commentFile)

  def SaveCsv(self, cdf, commentFile):
    saveTo = hsle.CreateFileName4ProcessedCommentFile(commentFile)
    cdf.to_csv(saveTo, sep=self.SEP, index=False)
    print('File saved to', saveTo)
    
