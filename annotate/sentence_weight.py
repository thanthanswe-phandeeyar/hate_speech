import pandas as pd
import numpy as np
import re 
from glob import glob 
from collections import defaultdict 
# from math import isnan
import math 
import gspread 
import os 
from oauth2client.service_account import ServiceAccountCredentials


AAသူပုန်=ကုလားတွေ=ကျောင်းနွား=ကြံ့ဖွတ်=ကြံ့ဖွတ်ပါတီ=ခိုးဝင်=ခွေးတပ်မတော်=ခွေးတရုတ်=ခွေးဝဲစား=ခွေးသတ်မတော်=ခွေးသား=ခွေးဦးနှောက်=ငလူး=ငှက်နီ=စစ်ခွေး=စစ်အာဏာရှင်=စောက်တရုတ်=တရုတ်ခွေး=တောသား=ထမီခြုံ=ထောင်ထွက်=ဒီမိုခွေးတွေ=ဒေါ်လာစား=နယ်ချဲ့ဗမာအကြမ်းဖက်တပ်=နီပိန်း=နီပေါ=ပြည်ထိုင်ခိုး=ဖင်ယား=ဖွတ်=ဖွတ်ပါတီ=ဖွတ်သူခိုး=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာတွေ=ဗမာစစ်တပ်=ဗမာအကြမ်းဖက်=ဗမာေတွ=ဗလီတွေ=ဘင်ဂါလီ=ဘိန်းစား=မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်=မူစလင်ကုလား=မူဆလင်=မူဆလင်ကုလားတွေ=မျိုးဖြုတ်=မြို့သား=မြေသြဇာ=မွတ်=မွတ်ကုလား=မွတ်ကုလားတွေ=မွတ်ဒေါင်း=မွတ်ပါတီ=ရခိုင်အကြမ်းဖက်သမား=ရခိုင်တပ်တော်AA=ရခိုင်သူပုန်aaအကြမ်းဖက်=ရခိုင်အစွန်းရောက်=ရခိုင်ကုလားတွေ=ရခိုင်တပ်တော်AA=ရခီး=ရခီးတွေ=ရွာသား=လီးကြံ့ဖွတ်=လူရိုင်း=ဝူဟန်=ဝူဟန်တရုတ်=သတ်မတော်=သူခိုး=သူပုန်=သူပုန်မ=သူပုန်လော်ဘီ=သောင်းကျမ်းသူ=အကြမ်းဖက်=အစွန်းရောက်=အဆိပ်သားတွေ=အနီကြောင်=အပြုတ်တိုက်=အမျိုးယုတ်=အမျိုးယုတ်ရှမ်း=အာနာရူးတွေ=အိမ်စောင့်ခွေး=အောက်တန်းကျ=အောက်တန်းစား=ဖွတ်တွေလဒတွေ=string_786 =အဘAA=အမြစ်ပြတ်ရှင်း=ခွေး =Thaiပြန်=gwi=ကမ္ဘာ့ကပ်ရောဂါကြီး=ကုလားပြည်နယ်=ကြံ့ဖွတ်သခိုး=ကြံ့ဖွတ်သူခိုးကောင်=ခွေးဝဲစခွေးသူတောင်းစားခွေး =ခွေးသူတောင်းစားခွေး=ခွေးသူတောင်းစားမီဒီညာ=ငပွေး=ငလူးပဲ=စစ်သူခိုးကြံ့ဖွတ်=စစ်ဦးဘီလူး=စောက်သုံးမကျအစိုးရ=စောင်ကုလား=တရုပ်စုပ်=ထန်းတောသားတွေ=ထမိန်ခြုံနဲ့ဘောမ=နပီဗမာစစ်ခွေးတပ်=နွားကျောင်းသား=ပလောင်တွေ=ပြည်ခိုင်ဖြိုးသူခိုး=ဖင်ကုံး=ဖာသေမစု=ဗမာစစ်အာဏာရှင်အုပ်စု=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာအစိုးရစစ်တပ်=ဗမာအစောရနှင့်ဗမာစစ်တပ်=ဗလီတွေ=မအေလိုးကြံ့ဖွတ်=စောင်ကုလား=0.0
လီးဆူး=သုတ်ကြောင်မ=မာမွတ်စူလတန်=မုဒိန်းစစ်တပ်=လူသားစိတ္ကင္းမဲ့=အစွန်းရောက်=အစွန်းရောက်ရခိုင်=အဖျက်သမားaa=ရခိး =အကြမ်းဖက်ကုလားတွေ=အစိမ်းရောင်ခွေး=ရခိုင်နဲ့မပွေး=မွတ်ဒေါင်းခွေ=တစ်မတ်သား=အရိုးကိုက်ဖွတ်ခွေး=ခွေးသူတောင်းစားမီဒီယာ=0.0

AAသူပုန်_acc=ကုလားတွေ_acc=ကျောင်းနွား_acc=ကြံ့ဖွတ်_acc=ကြံ့ဖွတ်ပါတီ_acc=ခိုးဝင်_acc=ခွေးတပ်မတော်_acc=ခွေးတရုတ်_acc=ခွေးဝဲစား_acc=ခွေးသတ်မတော်_acc=ခွေးသား_acc=ခွေးဦးနှောက်_acc=ငလူး_acc=ငှက်နီ_acc=စစ်ခွေး_acc=စစ်အာဏာရှင်_acc=စောက်တရုတ်_acc=တရုတ်ခွေး_acc=တောသား_acc=ထမီခြုံ_acc=ထောင်ထွက်_acc=ဒီမိုခွေးတွေ_acc=ဒေါ်လာစား_acc=နယ်ချဲ့ဗမာအကြမ်းဖက်တပ်_acc=နီပိန်း_acc=နီပေါ_acc=ပြည်ထိုင်ခိုး_acc=ဖင်ယား_acc=ဖွတ်_acc=ဖွတ်ပါတီ_acc=ဖွတ်သူခိုး_acc=ဗမာသောင်းကြမ်းသူအဖွဲ့_acc=ဗမာတွေ_acc=ဗမာစစ်တပ်_acc=ဗမာအကြမ်းဖက်_acc=ဗမာေတွ_acc=ဗလီတွေ_acc=ဘင်ဂါလီ_acc=ဘိန်းစား_acc=မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_acc=မူစလင်ကုလား_acc=မူဆလင်_acc=မူဆလင်ကုလားတွေ_acc=မျိုးဖြုတ်_acc=မြို့သား_acc=မြေသြဇာ_acc=မွတ်_acc=မွတ်ကုလား_acc=မွတ်ကုလားတွေ_acc=မွတ်ဒေါင်း_acc=မွတ်ပါတီ_acc=ရခိုင်အကြမ်းဖက်သမား_acc=ရခိုင်တပ်တော်AA_acc=ရခိုင်သူပုန်aaအကြမ်းဖက်_acc=ရခိုင်အစွန်းရောက်_acc=ရခိုင်ကုလားတွေ_acc=ရခိုင်တပ်တော်AA_acc=ရခီး_acc=ရခီးတွေ_acc=ရွာသား_acc=လီးကြံ့ဖွတ်_acc=လူရိုင်း_acc=ဝူဟန်_acc=ဝူဟန်တရုတ်_acc=သတ်မတော်_acc=သူခိုး_acc=သူပုန်_acc=သူပုန်မ_acc=သူပုန်လော်ဘီ_acc=သောင်းကျမ်းသူ_acc=အကြမ်းဖက်_acc=အစွန်းရောက်_acc=အဆိပ်သားတွေ_acc=အနီကြောင်_acc=အပြုတ်တိုက်_acc=အမျိုးယုတ်_acc=အမျိုးယုတ်ရှမ်း_acc=အာနာရူးတွေ_acc=အိမ်စောင့်ခွေး_acc=အောက်တန်းကျ_acc=အောက်တန်းစား_acc=ဖွတ်တွေလဒတွေ_acc=string_786_acc =အဘAA_acc=အမြစ်ပြတ်ရှင်း_acc=ခွေး_acc =Thaiပြန်_acc=gwi_acc=ကမ္ဘာ့ကပ်ရောဂါကြီး_acc=ကုလားပြည်နယ်_acc=ကြံ့ဖွတ်သခိုး_acc=ကြံ့ဖွတ်သူခိုးကောင်_acc=ခွေးဝဲစခွေးသူတောင်းစားခွေး_acc =ခွေးသူတောင်းစားခွေး_acc=ခွေးသူတောင်းစားမီဒီညာ_acc=ငပွေး_acc=ငလူးပဲ_acc=စစ်သူခိုးကြံ့ဖွတ်_acc=စစ်ဦးဘီလူး_acc=စောက်သုံးမကျအစိုးရ_acc=စောင်ကုလား_acc=တရုပ်စုပ်_acc=ထန်းတောသားတွေ_acc=ထမိန်ခြုံနဲ့ဘောမ_acc=နပီဗမာစစ်ခွေးတပ်_acc=နွားကျောင်းသား_acc=ပလောင်တွေ_acc=ပြည်ခိုင်ဖြိုးသူခိုး_acc=ဖင်ကုံး_acc=ဖာသေမစု_acc=ဗမာစစ်အာဏာရှင်အုပ်စု_acc=ဗမာသောင်းကြမ်းသူအဖွဲ့_acc=ဗမာအစိုးရစစ်တပ်_acc=ဗမာအစောရနှင့်ဗမာစစ်တပ်_acc=ဗလီတွေ_acc=မအေလိုးကြံ့ဖွတ်_acc=စောင်ကုလား_acc=လီးဆူး_acc=သုတ်ကြောင်မ_acc=မာမွတ်စူလတန်_acc=မုဒိန်းစစ်တပ်_acc=လူသားစိတ္ကင္းမဲ့_acc=အစွန်းရောက်_acc=အစွန်းရောက်ရခိုင်_acc=အဖျက်သမားaa_acc=ရခိး_acc =အကြမ်းဖက်ကုလားတွေ_acc=အစိမ်းရောင်ခွေး_acc=ရခိုင်နဲ့မပွေး_acc=မွတ်ဒေါင်းခွေ_acc=တစ်မတ်သား_acc=အရိုးကိုက်ဖွတ်ခွေး_acc=ခွေးသူတောင်းစားမီဒီယာ_acc=ရခီး_acc=လူသားစိတ်ကင်းမဲ့_acc=အောက်တန်းကြ_acc=ဘင်္ဂါလီ_acc=0.0
    

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']

creds= ServiceAccountCredentials.from_json_keyfile_name('hs_data_sheet.json',scope)
client = gspread.authorize(creds)
annotate =client.open('HSLE Data Sheet')

annotate_here = annotate.get_worksheet(0)   #annotate_here

annotate_here_val=annotate_here.get_all_records()
annotate_here_list=[]
for index in range(len(annotate_here_val)):
    for key in annotate_here_val[index]:
        if key=='MsgUniSeg':
            MsgUniSeg_key=annotate_here_val[index][key]
        elif key=='IsHS':
            IsHS=annotate_here_val[index][key]
        else:pass
    annotate_here_list.append([MsgUniSeg_key,IsHS])

#Create annotate_here dataframe 
annotate_here_df = pd.DataFrame(annotate_here_list, columns=['MsgUniSeg','IsHS'])

# Annotate_here_2
annotate_here_two = annotate.get_worksheet(1)   
annotate_here_two_val=annotate_here_two.get_all_records()
annotate_here_two_list=[]
for index in range(len(annotate_here_two_val)):
    for key in annotate_here_two_val[index]:
        if key=='MsgUniSeg':
            MsgUniSeg_key=annotate_here_two_val[index][key]
        elif key=='IsHS':
            IsHS=annotate_here_two_val[index][key]
        else:pass
    annotate_here_two_list.append([MsgUniSeg_key,IsHS])
    
#Create annotate_here dataframe 
annotate_here_two_df = pd.DataFrame(annotate_here_two_list, columns=['MsgUniSeg','IsHS'])

# Annotate_here_3
annotate_here_three = annotate.get_worksheet(2)   #
annotate_here_threeval=annotate_here_three.get_all_records()
annotate_here_three_list=[]
for index in range(len(annotate_here_threeval)):
    for key in annotate_here_threeval[index]:
        if key=='MsgUniSeg':
            MsgUniSeg_key=annotate_here_threeval[index][key]
        elif key=='IsHS':
            IsHS=annotate_here_threeval[index][key]
        else:pass
    annotate_here_three_list.append([MsgUniSeg_key,IsHS])

#Create annotate_here dataframe 
annotate_here_three_df = pd.DataFrame(annotate_here_three_list, columns=['MsgUniSeg','IsHS'])
# annotate_here_three_df.tail()

weighted=annotate_here_df.append((annotate_here_two_df,annotate_here_three_df),ignore_index=True)


weight_cols =['MsgUniSeg','Weighted_Value','IsHS']

weight_value_list = word_weight =weight_val= []
weight_value=lex_value=Seg_value=0

weight_value_list = word_weight =weight_val= []
weight_value=0


lexicon_pd =pd.read_csv('accuracy-folder/accuracy.csv',sep='~')


for index,weight in enumerate(weighted.values):
    AAသူပုန်=ကုလားတွေ=ကျောင်းနွား=ကြံ့ဖွတ်=ကြံ့ဖွတ်ပါတီ=ခိုးဝင်=ခွေးတပ်မတော်=ခွေးတရုတ်=ခွေးဝဲစား=ခွေးသတ်မတော်=ခွေးသား=ခွေးဦးနှောက်=ငလူး=ငှက်နီ=စစ်ခွေး=စစ်အာဏာရှင်=စောက်တရုတ်=တရုတ်ခွေး=တောသား=ထမီခြုံ=ထောင်ထွက်=ဒီမိုခွေးတွေ=ဒေါ်လာစား=နယ်ချဲ့ဗမာအကြမ်းဖက်တပ်=နီပိန်း=နီပေါ=ပြည်ထိုင်ခိုး=ဖင်ယား=ဖွတ်=ဖွတ်ပါတီ=ဖွတ်သူခိုး=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာတွေ=ဗမာစစ်တပ်=ဗမာအကြမ်းဖက်=ဗမာေတွ=ဗလီတွေ=ဘင်ဂါလီ=ဘိန်းစား=မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်=မူစလင်ကုလား=မူဆလင်=မူဆလင်ကုလားတွေ=မျိုးဖြုတ်=မြို့သား=မြေသြဇာ=မွတ်=မွတ်ကုလား=မွတ်ကုလားတွေ=မွတ်ဒေါင်း=မွတ်ပါတီ=ရခိုင်အကြမ်းဖက်သမား=ရခိုင်တပ်တော်AA=ရခိုင်သူပုန်aaအကြမ်းဖက်=ရခိုင်အစွန်းရောက်=ရခိုင်ကုလားတွေ=ရခိုင်တပ်တော်AA=ရခီး=ရခီးတွေ=ရွာသား=လီးကြံ့ဖွတ်=လူရိုင်း=ဝူဟန်=ဝူဟန်တရုတ်=သတ်မတော်=သူခိုး=သူပုန်=သူပုန်မ=သူပုန်လော်ဘီ=သောင်းကျမ်းသူ=အကြမ်းဖက်=အစွန်းရောက်=အဆိပ်သားတွေ=အနီကြောင်=အပြုတ်တိုက်=အမျိုးယုတ်=အမျိုးယုတ်ရှမ်း=အာနာရူးတွေ=အိမ်စောင့်ခွေး=အောက်တန်းကျ=အောက်တန်းစား=ဖွတ်တွေလဒတွေ=string_786 =အဘAA=အမြစ်ပြတ်ရှင်း=ခွေး =Thaiပြန်=gwi=ကမ္ဘာ့ကပ်ရောဂါကြီး=ကုလားပြည်နယ်=ကြံ့ဖွတ်သခိုး=ကြံ့ဖွတ်သူခိုးကောင်=ခွေးဝဲစခွေးသူတောင်းစားခွေး =ခွေးသူတောင်းစားခွေး=ခွေးသူတောင်းစားမီဒီညာ=ငပွေး=ငလူးပဲ=စစ်သူခိုးကြံ့ဖွတ်=စစ်ဦးဘီလူး=စောက်သုံးမကျအစိုးရ=စောင်ကုလား=တရုပ်စုပ်=ထန်းတောသားတွေ=ထမိန်ခြုံနဲ့ဘောမ=နပီဗမာစစ်ခွေးတပ်=နွားကျောင်းသား=ပလောင်တွေ=ပြည်ခိုင်ဖြိုးသူခိုး=ဖင်ကုံး=ဖာသေမစု=ဗမာစစ်အာဏာရှင်အုပ်စု=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာအစိုးရစစ်တပ်=ဗမာအစောရနှင့်ဗမာစစ်တပ်=ဗလီတွေ=မအေလိုးကြံ့ဖွတ်=စောင်ကုလား=0.0
    လီးဆူး=သုတ်ကြောင်မ=မာမွတ်စူလတန်=မုဒိန်းစစ်တပ်=လူသားစိတ္ကင္းမဲ့=အစွန်းရောက်=အစွန်းရောက်ရခိုင်=အဖျက်သမားaa=ရခိး =အကြမ်းဖက်ကုလားတွေ=အစိမ်းရောင်ခွေး=ရခိုင်နဲ့မပွေး=မွတ်ဒေါင်းခွေ=တစ်မတ်သား=အရိုးကိုက်ဖွတ်ခွေး=ခွေးသူတောင်းစားမီဒီယာ=ရခီး=လူသားစိတ်ကင်းမဲ့=အောက်တန်းကြ=ဘင်္ဂါလီ=0.0
    

    MsgUniSeg= str(weight[0]).replace(" ","")
    IsHS=weight[1]
    AAသူပုန်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='AAသူပုန်','Accuracy'].reset_index()
    ကုလားတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားတွေ','Accuracy'].reset_index()
    ကျောင်းနွား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ကျောင်းနွား','Accuracy'].reset_index()
    ကြံ့ဖွတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်','Accuracy'].reset_index()
    ကြံ့ဖွတ်ပါတီ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်ပါတီ','Accuracy'].reset_index()
    ခိုးဝင်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခိုးဝင်','Accuracy'].reset_index()
    ခွေးတပ်မတော်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတပ်မတော်','Accuracy'].reset_index()
    ခွေးတရုတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတရုတ်','Accuracy'].reset_index()
    ခွေးဝဲစား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဝဲစား','Accuracy'].reset_index()
    ခွေးသတ်မတော်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသတ်မတော်','Accuracy'].reset_index()
    ခွေးသား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသား','Accuracy'].reset_index()
    ခွေးဦးနှောက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဦးနှောက်','Accuracy'].reset_index()
    ငလူး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူး','Accuracy'].reset_index()
    ငှက်နီ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ငှက်နီ','Accuracy'].reset_index()
    စစ်ခွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ခွေး','Accuracy'].reset_index()
    စစ်အာဏာရှင်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်အာဏာရှင်','Accuracy'].reset_index()
    စောက်တရုတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်တရုတ်','Accuracy'].reset_index()
    တရုတ်ခွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုတ်ခွေး','Accuracy'].reset_index()
    တောသား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='တောသား','Accuracy'].reset_index()
    ထမီခြုံ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမီခြုံ','Accuracy'].reset_index()
    ထောင်ထွက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ထောင်ထွက်','Accuracy'].reset_index()
    ဒီမိုခွေးတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒီမိုခွေးတွေ','Accuracy'].reset_index()
    ဒေါ်လာစား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒေါ်လာစား','Accuracy'].reset_index()
    နယ်ချဲ့ဗမာအကြမ်းဖက်တပ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='နယ်ချဲ့ဗမာအကြမ်းဖက်တပ်','Accuracy'].reset_index()
    နီပိန်း_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပိန်း','Accuracy'].reset_index()
    နီပေါ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပေါ','Accuracy'].reset_index()
    ပြည်ထိုင်ခိုး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ထိုင်ခိုး','Accuracy'].reset_index()
    ဖင်ယား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ယား','Accuracy'].reset_index()
    ဖွတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်','Accuracy'].reset_index()
    ဖွတ်ပါတီ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်ပါတီ','Accuracy'].reset_index()
    ဖွတ်သူခိုး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်သူခိုး','Accuracy'].reset_index()
    ဗမာသောင်းကြမ်းသူအဖွဲ့_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာသောင်းကြမ်းသူအဖွဲ့','Accuracy'].reset_index()
    ဗမာတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာတွေ','Accuracy'].reset_index()
    ဗမာစစ်တပ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်တပ်','Accuracy'].reset_index()
    ဗမာအကြမ်းဖက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအကြမ်းဖက်','Accuracy'].reset_index()
    ဗမာေတွ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာေတွ','Accuracy'].reset_index()
    ဗလီတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗလီတွေ','Accuracy'].reset_index()
    ဘင်ဂါလီ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘင်ဂါလီ','Accuracy'].reset_index()
    ဘိန်းစား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘိန်းစား','Accuracy'].reset_index()
    မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်','Accuracy'].reset_index()
    မူစလင်ကုလား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မူစလင်ကုလား','Accuracy'].reset_index()
    မူဆလင်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်','Accuracy'].reset_index()
    မူဆလင်ကုလားတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်ကုလားတွေ','Accuracy'].reset_index()
    မျိုးဖြုတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မျိုးဖြုတ်','Accuracy'].reset_index()
    မြို့သား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြို့သား','Accuracy'].reset_index()
    မြေသြဇာ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြေသြဇာ','Accuracy'].reset_index()
    မွတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်','Accuracy'].reset_index()
    မွတ်ကုလား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလား','Accuracy'].reset_index()
    မွတ်ကုလားတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလားတွေ','Accuracy'].reset_index()
    မွတ်ဒေါင်း_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်း','Accuracy'].reset_index()
    မွတ်ဒေါင်းခွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်းခွေ','Accuracy'].reset_index()
    မွတ်ပါတီ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ပါတီ','Accuracy'].reset_index()
    ရခိုင်အကြမ်းဖက်သမား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အကြမ်းဖက်သမား','Accuracy'].reset_index()
    ရခိုင်တပ်တော်AA_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်တပ်တော်AA','Accuracy'].reset_index()
    ရခိုင်သူပုန်aaအကြမ်းဖက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်သူပုန်aaအကြမ်းဖက်','Accuracy'].reset_index()
    ရခိုင်အစွန်းရောက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အစွန်းရောက်','Accuracy'].reset_index()
    ရခိုင်ကုလားတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်ကုလားတွေ','Accuracy'].reset_index()
    ရခိုင်တပ်တော်AA_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်တပ်တော်AA','Accuracy'].reset_index()
    ရခီး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိး','Accuracy'].reset_index()
    ရခီးတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခီးတွေ','Accuracy'].reset_index()
    ရွာသား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရွာသား','Accuracy'].reset_index()
    လီးကြံ့ဖွတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးကြံ့ဖွတ်','Accuracy'].reset_index()
    လူရိုင်း_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='လူရိုင်း','Accuracy'].reset_index()
    ဝူဟန်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်','Accuracy'].reset_index()
    ဝူဟန်တရုတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်တရုတ်','Accuracy'].reset_index()
    သတ်မတော်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='သတ်မတော်','Accuracy'].reset_index()
    သူခိုး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='သူခိုး','Accuracy'].reset_index()
    သူပုန်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်','Accuracy'].reset_index()
    သူပုန်မ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်မ','Accuracy'].reset_index()
    သူပုန်လော်ဘီ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်လော်ဘီ','Accuracy'].reset_index()
    သောင်းကျမ်းသူ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='သောင်းကျမ်းသူ','Accuracy'].reset_index()
    အကြမ်းဖက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်','Accuracy'].reset_index()
    အစွန်းရောက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်','Accuracy'].reset_index()
    အဆိပ်သားတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အဆိပ်သားတွေ','Accuracy'].reset_index()
    အနီကြောင်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အနီကြောင်','Accuracy'].reset_index()
    အပြုတ်တိုက်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အပြုတ်တိုက်','Accuracy'].reset_index()
    အမျိုးယုတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်','Accuracy'].reset_index()
    အမျိုးယုတ်ရှမ်း_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်ရှမ်း','Accuracy'].reset_index()
    အာနာရူးတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အာနာရူးတွေ','Accuracy'].reset_index()
    အိမ်စောင့်ခွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အိမ်စောင့်ခွေး','Accuracy'].reset_index()
    အောက်တန်းကျ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းကျ','Accuracy'].reset_index()
    အောက်တန်းစား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းစား','Accuracy'].reset_index()
    ဖွတ်တွေလဒတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်တွေလဒတွေ','Accuracy'].reset_index()
    string_786_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='string_786','Accuracy'].reset_index()
    အဘAA_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အဘAA','Accuracy'].reset_index()
    အမြစ်ပြတ်ရှင်း_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အမြစ်ပြတ်ရှင်း','Accuracy'].reset_index()
    ခွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေး','Accuracy'].reset_index()
    Thaiပြန်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='Thaiပြန်','Accuracy'].reset_index()
    gwi_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='gwi','Accuracy'].reset_index()
    ကမ္ဘာ့ကပ်ရောဂါကြီး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ကမ္ဘာ့ကပ်ရောဂါကြီး','Accuracy'].reset_index()
    ကုလားပြည်နယ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားပြည်နယ်','Accuracy'].reset_index()
    ကြံ့ဖွတ်သခိုး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သခိုး','Accuracy'].reset_index()
    ကြံ့ဖွတ်သူခိုးကောင်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သူခိုးကောင်','Accuracy'].reset_index()
    ခွေးဝဲစခွေးသူတောင်းစားခွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဝဲစခွေးသူတောင်းစားခွေး','Accuracy'].reset_index()
    ခွေးသူတောင်းစားခွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားခွေး','Accuracy'].reset_index()
    ခွေးသူတောင်းစားမီဒီညာ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီညာ','Accuracy'].reset_index()
    ငပွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ငပွေး','Accuracy'].reset_index()
    ငလူးပဲ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူးပဲ','Accuracy'].reset_index()
    စစ်သူခိုးကြံ့ဖွတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်သူခိုးကြံ့ဖွတ်','Accuracy'].reset_index()
    စစ်ဦးဘီလူး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ဦးဘီလူး','Accuracy'].reset_index()
    စောက်သုံးမကျအစိုးရ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်သုံးမကျအစိုးရ','Accuracy'].reset_index()
    စောင်ကုလား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='စောင်ကုလား','Accuracy'].reset_index()
    တရုပ်စုပ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုပ်စုပ်','Accuracy'].reset_index()
    ထန်းတောသားတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ထန်းတောသားတွေ','Accuracy'].reset_index()
    ထမိန်ခြုံနဲ့ဘောမ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမိန်ခြုံနဲ့ဘောမ','Accuracy'].reset_index()
    နပီဗမာစစ်ခွေးတပ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='နပီဗမာစစ်ခွေးတပ်','Accuracy'].reset_index()
    နွားကျောင်းသား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='နွားကျောင်းသား','Accuracy'].reset_index()
    ပလောင်တွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ပလောင်တွေ','Accuracy'].reset_index()
    ပြည်ခိုင်ဖြိုးသူခိုး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ခိုင်ဖြိုးသူခိုး','Accuracy'].reset_index()
    ဖင်ကုံး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ကုံး','Accuracy'].reset_index()
    ဖာသေမစု_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖာသေမစု','Accuracy'].reset_index()
    ဗမာစစ်အာဏာရှင်အုပ်စု_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်အာဏာရှင်အုပ်စု','Accuracy'].reset_index()
    ဗမာသောင်းကြမ်းသူအဖွဲ့_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာသောင်းကြမ်းသူအဖွဲ့','Accuracy'].reset_index()
    ဗမာအစိုးရစစ်တပ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစိုးရစစ်တပ်','Accuracy'].reset_index()
    ဗမာအစောရနှင့်ဗမာစစ်တပ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစောရနှင့်ဗမာစစ်တပ်','Accuracy'].reset_index()
    ဗလီတွေ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗလီတွေ','Accuracy'].reset_index()
    မအေလိုးကြံ့ဖွတ်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='မအေလိုးကြံ့ဖွတ်','Accuracy'].reset_index()
    စောင်ကုလား_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='စောင်ကုလား','Accuracy'].reset_index()
    ရခိုင်နဲ့မပွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်နဲ့မပွေး','Accuracy'].reset_index()
    လီးဆူး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးဆူး','Accuracy'].reset_index()
    လူသားစိတ္ကင္းမဲ့_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='လူသားစိတ္ကင္းမဲ့','Accuracy'].reset_index()
    သုတ်ကြောင်မ_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='သုတ်ကြောင်မ','Accuracy'].reset_index()
    အစိမ်းရောင်ခွေး_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အစိမ်းရောင်ခွေး','Accuracy'].reset_index()
    အစွန်းရောက်ရခိုင်_acc =lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်ရခိုင်','Accuracy'].reset_index()
    string_786_acc=lexicon_pd.loc[lexicon_pd['Lexicon']=='၇၈၆','Accuracy'].reset_index()
    အဖျက်သမားaa_acc=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဖျက်သမားaa','Accuracy'].reset_index()
    မာမွတ်စူလတန်_acc=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာမွတ်စူလတန်','Accuracy'].reset_index()
    မုဒိန်းစစ်တပ်_acc=lexicon_pd.loc[lexicon_pd['Lexicon']=='မုဒိန်းစစ်တပ်','Accuracy'].reset_index()
    တစ်မတ်သား_acc=lexicon_pd.loc[lexicon_pd['Lexicon']=='တစ်မတ်သား','Accuracy'].reset_index()
    အရိုးကိုက်ဖွတ်ခွေး_acc=lexicon_pd.loc[lexicon_pd['Lexicon']=='အရိုးကိုက်ဖွတ်ခွေး','Accuracy'].reset_index()
    ခွေးသူတောင်းစားမီဒီယာ_acc=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီယာ','Accuracy'].reset_index()
  
    AAသူပုန် = float(MsgUniSeg.count('AAသူပုန်'))*float(ကုလားတွေ_acc['Accuracy'])
    မြို့သား = float(MsgUniSeg.count('မြို့သား'))*float(မြို့သား_acc['Accuracy'])
    မြေသြဇာ = float(MsgUniSeg.count('မြေသြဇာ'))*float(မြေသြဇာ_acc['Accuracy'])
    မွတ် = float(MsgUniSeg.count('မွတ်'))*float(မွတ်_acc['Accuracy'])
    မွတ်ကုလားတွေ = float(MsgUniSeg.count('မွတ်ကုလားတွေ'))*float(မွတ်ကုလားတွေ_acc['Accuracy'])
    မွတ်ဒေါင်း = float(MsgUniSeg.count('မွတ်ဒေါင်း'))*float(မွတ်ဒေါင်း_acc['Accuracy'])
    မွတ်ဒေါင်းခွေ = float(MsgUniSeg.count('မွတ်ဒေါင်းခွေ'))*float(မွတ်ဒေါင်းခွေ_acc['Accuracy'])
    မွတ်ပါတီ = float(MsgUniSeg.count('မွတ်ပါတီ'))*float(မွတ်ပါတီ_acc['Accuracy'])
    ရခိုင်အကြမ်းဖက်သမား = float(MsgUniSeg.count('ရခိုင်အကြမ်းဖက်သမား'))*float(ရခိုင်အကြမ်းဖက်သမား_acc['Accuracy'])
    ရခီး = float(MsgUniSeg.count('ရခီး'))*float(ရခီး_acc['Accuracy'])
    ရခိုင်တပ်တော်AA = float(MsgUniSeg.count('ရခိုင်တပ်တော်AA'))*float(ရခိုင်တပ်တော်AA_acc['Accuracy'])
    ရခိုင်နဲ့မပွေး = float(MsgUniSeg.count('ရခိုင်နဲ့မပွေး'))*float(ရခိုင်နဲ့မပွေး_acc['Accuracy'])
    ရခိုင်သူပုန်aaအကြမ်းဖက် = float(MsgUniSeg.count('ရခိုင်သူပုန်aaအကြမ်းဖက်'))*float(ရခိုင်သူပုန်aaအကြမ်းဖက်_acc['Accuracy'])
    ရခိုင်အစွန်းရောက် = float(MsgUniSeg.count('ရခိုင်အစွန်းရောက်'))*float(ရခိုင်အစွန်းရောက်_acc['Accuracy'])
    ရခိုင်ကုလားတွေ = float(MsgUniSeg.count('ရခိုင်ကုလားတွေ'))*float(ရခိုင်ကုလားတွေ_acc['Accuracy'])
    ရခီးတွေ = float(MsgUniSeg.count('ရခီးတွေ'))*float(ရခီးတွေ_acc['Accuracy'])
    ရွာသား = float(MsgUniSeg.count('ရွာသား'))*float(ရွာသား_acc['Accuracy'])
    လီးကြံ့ဖွတ် = float(MsgUniSeg.count('လီးကြံ့ဖွတ်'))*float(လီးကြံ့ဖွတ်_acc['Accuracy'])
    လီးဆူး = float(MsgUniSeg.count('လီးဆူး'))*float(လီးဆူး_acc['Accuracy'])
    လူရိုင်း = float(MsgUniSeg.count('လူရိုင်း'))*float(လူရိုင်း_acc['Accuracy'])
    လူသားစိတ်ကင်းမဲ့ = float(MsgUniSeg.count('လူသားစိတ်ကင်းမဲ့'))*float(လူသားစိတ္ကင္းမဲ့_acc['Accuracy'])
    လူသားစိတ္ကင္းမဲ့ = float(MsgUniSeg.count('လူသားစိတ္ကင္းမဲ့'))*float(လူသားစိတ္ကင္းမဲ့_acc['Accuracy'])
    ဝူဟန် = float(MsgUniSeg.count('ဝူဟန်'))*float(ဝူဟန်_acc['Accuracy'])
    ဝူဟန်တရုတ် = float(MsgUniSeg.count('ဝူဟန်တရုတ်'))*float(ဝူဟန်တရုတ်_acc['Accuracy'])
    သတ်မတော် = float(MsgUniSeg.count('သတ်မတော်'))*float(သတ်မတော်_acc['Accuracy'])
    သုတ်ကြောင်မ = float(MsgUniSeg.count('သုတ်ကြောင်မ'))*float(သုတ်ကြောင်မ_acc['Accuracy'])
    သူခိုး = float(MsgUniSeg.count('သူခိုး'))*float(သူခိုး_acc['Accuracy'])
    သူပုန် = float(MsgUniSeg.count('သူပုန်'))*float(သူပုန်_acc['Accuracy'])
    သူပုန်မ = float(MsgUniSeg.count('သူပုန်မ'))*float(သူပုန်မ_acc['Accuracy'])
    သူပုန်လော်ဘီ = float(MsgUniSeg.count('သူပုန်လော်ဘီ'))*float(သူပုန်လော်ဘီ_acc['Accuracy'])
    သောင်းကျမ်းသူ = float(MsgUniSeg.count('သောင်းကျမ်းသူ'))*float(သောင်းကျမ်းသူ_acc['Accuracy'])
    အကြမ်းဖက် = float(MsgUniSeg.count('အကြမ်းဖက်'))*float(အကြမ်းဖက်_acc['Accuracy'])
    အစိမ်းရောင်ခွေး = float(MsgUniSeg.count('အစိမ်းရောင်ခွေး'))*float(အစိမ်းရောင်ခွေး_acc['Accuracy'])
    အစွန်းရောက် = float(MsgUniSeg.count('အစွန်းရောက်'))*float(အစွန်းရောက်_acc['Accuracy'])
    အစွန်းရောက်ရခိုင် = float(MsgUniSeg.count('အစွန်းရောက်ရခိုင်'))*float(အစွန်းရောက်ရခိုင်_acc['Accuracy'])
    အဆိပ်သားတွေ = float(MsgUniSeg.count('အဆိပ်သားတွေ'))*float(အဆိပ်သားတွေ_acc['Accuracy'])
    အနီကြောင် = float(MsgUniSeg.count('အနီကြောင်'))*float(အနီကြောင်_acc['Accuracy'])
    အပြုတ်တိုက် = float(MsgUniSeg.count('အပြုတ်တိုက်'))*float(အပြုတ်တိုက်_acc['Accuracy'])
    အဖျက်သမားaa = float(MsgUniSeg.count('အဖျက်သမားaa'))*float(အဖျက်သမားaa_acc['Accuracy'])
    အဘAA = float(MsgUniSeg.count('အဘAA'))*float(အဘAA_acc['Accuracy'])
    အမျိုးယုတ် = float(MsgUniSeg.count('အမျိုးယုတ်'))*float(အမျိုးယုတ်_acc['Accuracy'])
    အမျိုးယုတ်ရှမ်း = float(MsgUniSeg.count('အမျိုးယုတ်ရှမ်း'))*float(အမျိုးယုတ်ရှမ်း_acc['Accuracy'])
    အမြစ်ပြတ်ရှင်း = float(MsgUniSeg.count('အမြစ်ပြတ်ရှင်း'))*float(အမြစ်ပြတ်ရှင်း_acc['Accuracy'])
    အာနာရူးတွေ = float(MsgUniSeg.count('အာနာရူးတွေ'))*float(အာနာရူးတွေ_acc['Accuracy'])
    အိမ်စောင့်ခွေး = float(MsgUniSeg.count('အိမ်စောင့်ခွေး'))*float(အိမ်စောင့်ခွေး_acc['Accuracy'])
    အောက်တန်းကျ = float(MsgUniSeg.count('အောက်တန်းကျ'))*float(အောက်တန်းကျ_acc['Accuracy'])
    အောက်တန်းကြ = float(MsgUniSeg.count('အောက်တန်းကြ'))*float(အောက်တန်းကျ_acc['Accuracy'])
    အောက်တန်းစား = float(MsgUniSeg.count('အောက်တန်းစား'))*float(အောက်တန်းစား_acc['Accuracy'])
    ခွေး = float(MsgUniSeg.count('ခွေး'))*float(ခွေး_acc['Accuracy'])
    string_786 = float(MsgUniSeg.count('string_786'))*float(string_786_acc['Accuracy'])
    AAသူပုန် = float(MsgUniSeg.count('AAသူပုန်'))*float(AAသူပုန်_acc['Accuracy'])
    Thaiပြန် = float(MsgUniSeg.count('Thaiပြန်'))*float(Thaiပြန်_acc['Accuracy'])
    gwi = float(MsgUniSeg.count('gwi'))*float(gwi_acc['Accuracy'])
    ကမ္ဘာ့ကပ်ရောဂါကြီး = float(MsgUniSeg.count('ကမ္ဘာ့ကပ်ရောဂါကြီး'))*float(ကမ္ဘာ့ကပ်ရောဂါကြီး_acc['Accuracy'])
    ကုလားပြည်နယ် = float(MsgUniSeg.count('ကုလားပြည်နယ်'))*float(ကုလားပြည်နယ်_acc['Accuracy'])
    ကုလားတွေ= float(MsgUniSeg.count('ကုလားတွေ'))*float(ကုလားတွေ_acc['Accuracy'])
    ကျောင်းနွား = float(MsgUniSeg.count('ကျောင်းနွား'))*float(ကျောင်းနွား_acc['Accuracy'])
    ကြံ့ဖွတ် = float(MsgUniSeg.count('ကြံ့ဖွတ်'))*float(ကြံ့ဖွတ်_acc['Accuracy'])
    ကြံ့ဖွတ်သခိုး = float(MsgUniSeg.count('ကြံ့ဖွတ်သခိုး'))*float(ကြံ့ဖွတ်သခိုး_acc['Accuracy'])
    ကြံ့ဖွတ်သူခိုးကောင် = float(MsgUniSeg.count('ကြံ့ဖွတ်သူခိုးကောင်'))*float(ကြံ့ဖွတ်သူခိုးကောင်_acc['Accuracy'])
    ကြံ့ဖွတ်ပါတီ = float(MsgUniSeg.count('ကြံ့ဖွတ်ပါတီ'))*float(ကြံ့ဖွတ်ပါတီ_acc['Accuracy'])
    ခိုးဝင် = float(MsgUniSeg.count('ခိုးဝင်'))*float(ခိုးဝင်_acc['Accuracy'])
    ခွေးတပ်မတော် = float(MsgUniSeg.count('ခွေးတပ်မတော်'))*float(ခွေးတပ်မတော်_acc['Accuracy'])
    ခွေးတရုတ် = float(MsgUniSeg.count('ခွေးတရုတ်'))*float(ခွေးတရုတ်_acc['Accuracy'])
    ခွေးသား = float(MsgUniSeg.count('ခွေးသား'))*float(ခွေးသား_acc['Accuracy'])
    ခွေးသူတောင်းစားခွေး = float(MsgUniSeg.count('ခွေးသူတောင်းစားခွေး'))*float(ခွေးသူတောင်းစားခွေး_acc['Accuracy'])
    ခွေးသူတောင်းစားမီဒီညာ = float(MsgUniSeg.count('ခွေးသူတောင်းစားမီဒီညာ'))*float(ခွေးသူတောင်းစားမီဒီညာ_acc['Accuracy'])
    ခွေးဦးနှောက် = float(MsgUniSeg.count('ခွေးဦးနှောက်'))*float(ခွေးဦးနှောက်_acc['Accuracy'])
    ခွေးဝဲစား = float(MsgUniSeg.count('ခွေးဝဲစား'))*float(ခွေးဝဲစား_acc['Accuracy'])
    ခွေးသတ်မတော် = float(MsgUniSeg.count('ခွေးသတ်မတော်'))*float(ခွေးသတ်မတော်_acc['Accuracy'])
    ငပွေး = float(MsgUniSeg.count('ငပွေး'))*float(ငပွေး_acc['Accuracy'])
    ငလူး = float(MsgUniSeg.count('ငလူး'))*float(ငလူး_acc['Accuracy'])
    ငလူးပဲ = float(MsgUniSeg.count('ငလူးပဲ'))*float(ငလူးပဲ_acc['Accuracy'])
    ငှက်နီ = float(MsgUniSeg.count('ငှက်နီ'))*float(ငှက်နီ_acc['Accuracy'])
    စစ်သူခိုးကြံ့ဖွတ် = float(MsgUniSeg.count('စစ်သူခိုးကြံ့ဖွတ်'))*float(စစ်သူခိုးကြံ့ဖွတ်_acc['Accuracy'])
    စစ်အာဏာရှင် = float(MsgUniSeg.count('စစ်အာဏာရှင်'))*float(စစ်အာဏာရှင်_acc['Accuracy'])
    စစ်ခွေး = float(MsgUniSeg.count('စစ်ခွေး'))*float(စစ်ခွေး_acc['Accuracy'])
    စစ်ဦးဘီလူး = float(MsgUniSeg.count('စစ်ဦးဘီလူး'))*float(စစ်ဦးဘီလူး_acc['Accuracy'])
    စောက်တရုတ် = float(MsgUniSeg.count('စောက်တရုတ်'))*float(စောက်တရုတ်_acc['Accuracy'])
    စောက်သုံးမကျအစိုးရ = float(MsgUniSeg.count('စောက်သုံးမကျအစိုးရ'))*float(စောက်သုံးမကျအစိုးရ_acc['Accuracy'])
    စောင်ကုလား = float(MsgUniSeg.count('စောင်ကုလား'))*float(စောင်ကုလား_acc['Accuracy'])
    တရုပ်စုပ် = float(MsgUniSeg.count('တရုပ်စုပ်'))*float(တရုပ်စုပ်_acc['Accuracy'])
    တရုတ်ခွေး = float(MsgUniSeg.count('တရုတ်ခွေး'))*float(တရုတ်ခွေး_acc['Accuracy'])
    တောသား = float(MsgUniSeg.count('တောသား'))*float(တောသား_acc['Accuracy'])
    ထန်းတောသားတွေ = float(MsgUniSeg.count('ထန်းတောသားတွေ'))*float(ထန်းတောသားတွေ_acc['Accuracy'])
    ထမိန်ခြုံနဲ့ဘောမ = float(MsgUniSeg.count('ထမိန်ခြုံနဲ့ဘောမ'))*float(ထမိန်ခြုံနဲ့ဘောမ_acc['Accuracy'])
    ထမီခြုံ = float(MsgUniSeg.count('ထမီခြုံ'))*float(ထမီခြုံ_acc['Accuracy'])
    ထောင်ထွက် = float(MsgUniSeg.count('ထောင်ထွက်'))*float(ထောင်ထွက်_acc['Accuracy'])
    ဒီမိုခွေးတွေ = float(MsgUniSeg.count('ဒီမိုခွေးတွေ'))*float(ဒီမိုခွေးတွေ_acc['Accuracy'])
    ဒေါ်လာစား = float(MsgUniSeg.count('ဒေါ်လာစား'))*float(ဒေါ်လာစား_acc['Accuracy'])
    နပီဗမာစစ်ခွေးတပ် = float(MsgUniSeg.count('နပီဗမာစစ်ခွေးတပ်'))*float(နပီဗမာစစ်ခွေးတပ်_acc['Accuracy'])
    နီပိန်း = float(MsgUniSeg.count('နီပိန်း'))*float(နီပိန်း_acc['Accuracy'])
    နီပေါ = float(MsgUniSeg.count('နီပေါ'))*float(နီပေါ_acc['Accuracy'])
    နွားကျောင်းသား = float(MsgUniSeg.count('နွားကျောင်းသား'))*float(နွားကျောင်းသား_acc['Accuracy'])
    ပလောင်တွေ = float(MsgUniSeg.count('ပလောင်တွေ'))*float(ပလောင်တွေ_acc['Accuracy'])
    ပြည်ခိုင်ဖြိုးသူခိုး = float(MsgUniSeg.count('ပြည်ခိုင်ဖြိုးသူခိုး'))*float(ပြည်ခိုင်ဖြိုးသူခိုး_acc['Accuracy'])
    ပြည်ထိုင်ခိုး = float(MsgUniSeg.count('ပြည်ထိုင်ခိုး'))*float(ပြည်ထိုင်ခိုး_acc['Accuracy'])
    ဖင်ကုံး = float(MsgUniSeg.count('ဖင်ကုံး'))*float(ဖင်ကုံး_acc['Accuracy'])
    ဖင်ယား = float(MsgUniSeg.count('ဖင်ယား'))*float(ဖင်ယား_acc['Accuracy'])
    ဖာသေမစု = float(MsgUniSeg.count('ဖာသေမစု'))*float(ဖာသေမစု_acc['Accuracy'])
    ဖွတ်သူခိုး = float(MsgUniSeg.count('ဖွတ်သူခိုး'))*float(ဖွတ်သူခိုး_acc['Accuracy'])
    ဖွတ် = float(MsgUniSeg.count('ဖွတ်'))*float(ဖွတ်_acc['Accuracy'])
    ဖွတ်ပါတီ = float(MsgUniSeg.count('ဖွတ်ပါတီ'))*float(ဖွတ်ပါတီ_acc['Accuracy'])
    ဗမာတွေ = float(MsgUniSeg.count('ဗမာတွေ'))*float(ဗမာတွေ_acc['Accuracy'])
    ဗမာစစ်အာဏာရှင်အုပ်စု = float(MsgUniSeg.count('ဗမာစစ်အာဏာရှင်အုပ်စု'))*float(ဗမာစစ်အာဏာရှင်အုပ်စု_acc['Accuracy'])
    ဗမာသောင်းကြမ်းသူအဖွဲ့ = float(MsgUniSeg.count('ဗမာသောင်းကြမ်းသူအဖွဲ့'))*float(ဗမာသောင်းကြမ်းသူအဖွဲ့_acc['Accuracy'])
    ဗမာအစိုးရစစ်တပ် = float(MsgUniSeg.count('ဗမာအစိုးရစစ်တပ်'))*float(ဗမာအစိုးရစစ်တပ်_acc['Accuracy'])
    ဗမာအစောရနှင့်ဗမာစစ်တပ် = float(MsgUniSeg.count('ဗမာအစောရနှင့်ဗမာစစ်တပ်'))*float(ဗမာအစောရနှင့်ဗမာစစ်တပ်_acc['Accuracy'])
    ဗမာစစ်တပ် = float(MsgUniSeg.count('ဗမာစစ်တပ်'))*float(ဗမာစစ်တပ်_acc['Accuracy'])
    ဗမာအကြမ်းဖက် = float(MsgUniSeg.count('ဗမာအကြမ်းဖက်'))*float(ဗမာအကြမ်းဖက်_acc['Accuracy'])
    ဗလီတွေ = float(MsgUniSeg.count('ဗလီတွေ'))*float(ဗလီတွေ_acc['Accuracy'])
    ဘင်ဂါလီ = float(MsgUniSeg.count('ဘင်ဂါလီ'))*float(ဘင်ဂါလီ_acc['Accuracy'])
    ဘင်္ဂါလီ = float(MsgUniSeg.count('ဘင်္ဂါလီ'))*float(ဘင်ဂါလီ_acc['Accuracy'])
    ဘိန်းစား = float(MsgUniSeg.count('ဘိန်းစား'))*float(ဘိန်းစား_acc['Accuracy'])
    မအေလိုးကြံ့ဖွတ် = float(MsgUniSeg.count('မအေလိုးကြံ့ဖွတ်'))*float(မအေလိုးကြံ့ဖွတ်_acc['Accuracy'])
    မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက် = float(MsgUniSeg.count('မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်'))*float(မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_acc['Accuracy'])
    မာမွတ်စူလတန် = float(MsgUniSeg.count('မာမွတ်စူလတန်'))*float(မာမွတ်စူလတန်_acc['Accuracy'])
    မုဒိန်းစစ်တပ် = float(MsgUniSeg.count('မုဒိန်းစစ်တပ်'))*float(မုဒိန်းစစ်တပ်_acc['Accuracy'])
    မူစလင်ကုလား = float(MsgUniSeg.count('မူစလင်ကုလား'))*float(မူစလင်ကုလား_acc['Accuracy'])
    မူဆလင် = float(MsgUniSeg.count('မူဆလင်'))*float(မူဆလင်_acc['Accuracy'])
    မူဆလင်ကုလားတွေ = float(MsgUniSeg.count('မူဆလင်ကုလားတွေ'))*float(မူဆလင်ကုလားတွေ_acc['Accuracy'])
    မျိုးဖြုတ် = float(MsgUniSeg.count('မျိုးဖြုတ်'))*float(မျိုးဖြုတ်_acc['Accuracy'])
    တစ်မတ်သား = float(MsgUniSeg.count('တစ်မတ်သား'))*float(တစ်မတ်သား_acc['Accuracy'])
    အရိုးကိုက်ဖွတ်ခွေး = float(MsgUniSeg.count('အရိုးကိုက်ဖွတ်ခွေး'))*float(အရိုးကိုက်ဖွတ်ခွေး_acc['Accuracy'])
    ခွေးသူတောင်းစားမီဒီယာ = float(MsgUniSeg.count('ခွေးသူတောင်းစားမီဒီယာ'))*float(ခွေးသူတောင်းစားမီဒီယာ_acc['Accuracy'])
    
    weight_value = AAသူပုန်+မွတ်ကုလား+မြို့သား+မြေသြဇာ+မွတ်+မွတ်ကုလားတွေ+မွတ်ဒေါင်း+မွတ်ဒေါင်းခွေ+မွတ်ပါတီ+ရခိုင်အကြမ်းဖက်သမား+ရခိး+ရခီးတွေ+ရွာသား+လီးကြံ့ဖွတ်+လီးဆူး+လူရိုင်း+လူသားစိတ္ကင္းမဲ့+ဝူဟန်+ဝူဟန်တရုတ်+သတ်မတော်+သုတ်ကြောင်မ+သူခိုး+သူပုန်+သူပုန်မ+သူပုန်လော်ဘီ+သောင်းကျမ်းသူ+အကြမ်းဖက်+အကြမ်းဖက်ကုလားတွေ+အစိမ်းရောင်ခွေး+အစွန်းရောက်+အစွန်းရောက်ရခိုင်+အဆိပ်သားတွေ+အနီကြောင်+အပြုတ်တိုက်+အဖျက်သမားaa+အဘAA+အမျိုးယုတ်+အမျိုးယုတ်ရှမ်း+အမြစ်ပြတ်ရှင်း+အာနာရူးတွေ+အာနာရူးတွေ+အိမ်စောင့်ခွေး+အောက်တန်းကျ+အောက်တန်းစား+ဖွတ်တွေလဒတွေ+ခွေး+string_786+AAသူပုန်+Thaiပြန်+gwi+ကမ္ဘာ့ကပ်ရောဂါကြီး+ကုလားပြည်နယ်+ကုလားတွေ+ရခိုင်ကုလားတွေ+ကျောင်းနွား+ကြံ့ဖွတ်+ကြံ့ဖွတ်သခိုး+ကြံ့ဖွတ်သူခိုးကောင်+ကြံ့ဖွတ်ပါတီ+ခိုးဝင်+ခွေးတပ်မတော်+ခွေးတရုတ်+ခွေးသား+ခွေးသူတောင်းစားခွေး+ခွေးသူတောင်းစားမီဒီညာ+ခွေးဦးနှောက်+ခွေးဝဲစား+ခွေးသတ်မတော်+ငပွေး+ငလူး+ငလူးပဲ+ငှက်နီ+စစ်သူခိုးကြံ့ဖွတ်+စစ်အာဏာရှင်+စစ်ခွေး+စစ်ဦးဘီလူး+စောက်တရုတ်+စောက်သုံးမကျအစိုးရ+စောင်ကုလား+တရုပ်စုပ်+တရုတ်ခွေး+တောသား+ထန်းတောသားတွေ+ထမိန်ခြုံနဲ့ဘောမ+ထမီခြုံ+ထောင်ထွက်+ဒီမိုခွေးတွေ+ဒေါ်လာစား+နပီဗမာစစ်ခွေးတပ်+နီပိန်း+နီပေါ+နွားကျောင်းသား+ပလောင်တွေ+ပြည်ခိုင်ဖြိုးသူခိုး+ပြည်ထိုင်ခိုး+ဖင်ကုံး+ဖင်ယား+ဖာသေမစု+ဖွတ်သူခိုး+ဖွတ်+ဖွတ်ပါတီ+ဗမာတွေ+ဗမာစစ်အာဏာရှင်အုပ်စု+ဗမာသောင်းကြမ်းသူအဖွဲ့+ဗမာအစိုးရစစ်တပ်+ဗမာအစောရနှင့်ဗမာစစ်တပ်+ဗမာစစ်တပ်+ဗမာအကြမ်းဖက်+ဗလီတွေ+ဘင်ဂါလီ+ဘိန်းစား+မအေလိုးကြံ့ဖွတ်+မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်+မာမွတ်စူလတန်+မုဒိန်းစစ်တပ်+မူစလင်ကုလား+မူဆလင်+မူဆလင်ကုလားတွေ+မျိုးဖြုတ်+တစ်မတ်သား+အရိုးကိုက်ဖွတ်ခွေး+ခွေးသူတောင်းစားမီဒီယာ
    word_weight.append([MsgUniSeg,weight_value,IsHS])

weight_pd =pd.DataFrame(word_weight,columns=weight_cols)
weight_pd =weight_pd.to_csv('/home/swift/Documents/hate-speech-new/annotate/sentence_weight.csv')




