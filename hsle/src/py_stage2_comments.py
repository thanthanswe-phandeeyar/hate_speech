import warnings
warnings.filterwarnings('ignore')
from CrowdTangleExportCommentsTools.CommentsProcessing import CommentsProcessing
import json

if __name__=='__main__':
    with open('_current_data_.json') as f:
        CURRENT_DATA = json.load(f)
    print('============================================')
    print(CURRENT_DATA['pages_groups'], CURRENT_DATA['daterange'])
    print('============================================')
    POSTFILE = '../data/crowdtangle-{}/processed_{}.csv'.format(
        CURRENT_DATA['pages_groups'],
        CURRENT_DATA['daterange']
    )
    print(POSTFILE)
    CommentsProcessing(POSTFILE, do_segmentation=True, sep='~').Run()
