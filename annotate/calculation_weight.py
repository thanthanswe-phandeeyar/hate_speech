import calculate_weight_func as weight 
import pandas as pd 
from importlib import reload
from tqdm import tqdm
import numpy as np
import re 
from glob import glob 
from collections import defaultdict 
import math 
import os 
import gspread 
from oauth2client.service_account import ServiceAccountCredentials


o_str=AAသူပုန်=ကုလားတွေ=ကျောင်းနွား=ကြံ့ဖွတ်=ကြံ့ဖွတ်ပါတီ=ခိုးဝင်=ခွေးတပ်မတော်=ခွေးတရုတ်=ခွေးဝဲစား=ခွေးသတ်မတော်=ခွေးသား=ခွေးဦးနှောက်=ငလူး=ငှက်နီ=စစ်ခွေး=စစ်အာဏာရှင်=စောက်တရုတ်=တရုတ်ခွေး=တောသား=ထမီခြုံ=ထောင်ထွက်=ဒီမိုခွေးတွေ=ဒေါ်လာစား=နယ်ချဲ့ဗမာအကြမ်းဖက်တပ်=နီပိန်း=နီပေါ=ပြည်ထိုင်ခိုး=ဖင်ယား=ဖွတ်=ဖွတ်ပါတီ=ဖွတ်သူခိုး=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာတွေ=ဗမာစစ်တပ်=ဗမာအကြမ်းဖက်=ဗမာေတွ=ဗလီတွေ=ဘင်ဂါလီ=ဘိန်းစား=မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်=မူစလင်ကုလား=မူဆလင်=မူဆလင်ကုလားတွေ=မျိုးဖြုတ်=မြို့သား=မြေသြဇာ=မွတ်=မွတ်ကုလား=မွတ်ကုလားတွေ=မွတ်ဒေါင်း=မွတ်ပါတီ=ရခိုင်အကြမ်းဖက်သမား=ရခိုင်တပ်တော်AA=ရခိုင်သူပုန်aaအကြမ်းဖက်=ရခိုင်အစွန်းရောက်=ရခိုင်ကုလားတွေ=ရခိုင်တပ်တော်AA=ရခီး=ရခီးတွေ=ရွာသား=လီးကြံ့ဖွတ်=လူရိုင်း=ဝူဟန်=ဝူဟန်တရုတ်=သတ်မတော်=သူခိုး=သူပုန်=သူပုန်မ=သူပုန်လော်ဘီ=သောင်းကျမ်းသူ=အကြမ်းဖက်=အစွန်းရောက်=အဆိပ်သားတွေ=အနီကြောင်=အပြုတ်တိုက်=အမျိုးယုတ်=အမျိုးယုတ်ရှမ်း=အာနာရူးတွေ=အိမ်စောင့်ခွေး=အောက်တန်းကျ=အောက်တန်းစား=ဖွတ်တွေလဒတွေ=string_786 =အဘAA=အမြစ်ပြတ်ရှင်း=ခွေး =Thaiပြန်=gwi=ကမ္ဘာ့ကပ်ရောဂါကြီး=ကုလားပြည်နယ်=ကြံ့ဖွတ်သခိုး=ကြံ့ဖွတ်သူခိုးကောင်=ခွေးဝဲစခွေးသူတောင်းစားခွေး =ခွေးသူတောင်းစားခွေး=ခွေးသူတောင်းစားမီဒီညာ=ငပွေး=ငလူးပဲ=စစ်သူခိုးကြံ့ဖွတ်=စစ်ဦးဘီလူး=စောက်သုံးမကျအစိုးရ=စောင်ကုလား=တရုပ်စုပ်=ထန်းတောသားတွေ=ထမိန်ခြုံနဲ့ဘောမ=နပီဗမာစစ်ခွေးတပ်=နွားကျောင်းသား=ပလောင်တွေ=ပြည်ခိုင်ဖြိုးသူခိုး=ဖင်ကုံး=ဖာသေမစု=ဗမာစစ်အာဏာရှင်အုပ်စု=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာအစိုးရစစ်တပ်=ဗမာအစောရနှင့်ဗမာစစ်တပ်=ဗလီတွေ=မအေလိုးကြံ့ဖွတ်=စောင်ကုလား=0
လီးဆူး=သုတ်ကြောင်မ=မာမွတ်စူလတန်=မုဒိန်းစစ်တပ်=လူသားစိတ္ကင္းမဲ့=အစွန်းရောက်=အစွန်းရောက်ရခိုင်=အဖျက်သမားaa=ရခိး =အကြမ်းဖက်ကုလားတွေ=အစိမ်းရောင်ခွေး=ရခိုင်နဲ့မပွေး=မွတ်ဒေါင်းခွေ=တစ်မတ်သား=အရိုးကိုက်ဖွတ်ခွေး=ခွေးသူတောင်းစားမီဒီယာ=0


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']

creds= ServiceAccountCredentials.from_json_keyfile_name('hs_data_sheet.json',scope)
client = gspread.authorize(creds)
annotate =client.open('HSLE Data Sheet')

annotate_here = annotate.get_worksheet(0)   #annotate_here

annotate_here_val=annotate_here.get_all_records()
annotate_here_list=[]
for index in range(len(annotate_here_val)):
    for key in annotate_here_val[index]:
        if key=='LexFound':
            LexFound_key=annotate_here_val[index][key]
        elif key=='MsgUniSeg':
            MsgUniSeg_key=annotate_here_val[index][key]
        elif key=='NewHSWordInSentence':
            NewHSWordInSentence_key=annotate_here_val[index][key]
        elif key=='IsHS':
            IsHS=annotate_here_val[index][key]
        else:pass
    annotate_here_list.append([LexFound_key,MsgUniSeg_key,NewHSWordInSentence_key,IsHS])

#Create annotate_here dataframe 
annotate_here_df = pd.DataFrame(annotate_here_list, columns=['LexFound','MsgUniSeg','NewHSWordInSentence','IsHS'])

# Annotate_here_2
annotate_here_two = annotate.get_worksheet(1)   
annotate_here_two_val=annotate_here_two.get_all_records()
annotate_here_two_list=[]
for index in range(len(annotate_here_two_val)):
    for key in annotate_here_two_val[index]:
        if key=='LexFound':
            LexFound_key=annotate_here_two_val[index][key]
        elif key=='MsgUniSeg':
            MsgUniSeg_key=annotate_here_two_val[index][key]
        elif key=='NewHSWordInSentence':
            NewHSWordInSentence_key=annotate_here_two_val[index][key]
        elif key=='IsHS':
            IsHS=annotate_here_two_val[index][key]
        else:pass
    annotate_here_two_list.append([LexFound_key,MsgUniSeg_key,NewHSWordInSentence_key,IsHS])
    
#Create annotate_here dataframe 
annotate_here_two_df = pd.DataFrame(annotate_here_two_list, columns=['LexFound','MsgUniSeg','NewHSWordInSentence','IsHS'])


# Annotate_here_3
annotate_here_three = annotate.get_worksheet(2)   #
annotate_here_threeval=annotate_here_three.get_all_records()
annotate_here_three_list=[]
for index in range(len(annotate_here_threeval)):
    for key in annotate_here_threeval[index]:
        if key=='LexFound':
            LexFound_key=annotate_here_threeval[index][key]
        elif key=='MsgUniSeg':
            MsgUniSeg_key=annotate_here_threeval[index][key]
        elif key=='NewHSWordInSentence':
            NewHSWordInSentence_key=annotate_here_threeval[index][key]
        elif key=='IsHS':
            IsHS=annotate_here_threeval[index][key]
        else:pass
    annotate_here_three_list.append([LexFound_key,MsgUniSeg_key,NewHSWordInSentence_key,IsHS])

#Create annotate_here dataframe 
annotate_here_three_df = pd.DataFrame(annotate_here_three_list, columns=['LexFound','MsgUniSeg','NewHSWordInSentence','IsHS'])
weighted=annotate_here_df.append((annotate_here_two_df,annotate_here_three_df),ignore_index=True)


weight_value_list = word_weight =weight_val= []
weight_value=lex_value=Seg_value=0


weight_cols =['LexFound','MsgUniSeg','NewHSWordInSentence','Weighted_Value']

reload(weight);

lexicon_weight = weight.weight_calculation(weighted)

weight_pd =pd.DataFrame(lexicon_weight,columns=weight_cols)
weight_pd =weight_pd.to_csv('weight.csv')
