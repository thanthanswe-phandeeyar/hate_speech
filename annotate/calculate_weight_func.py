import pandas as pd
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


weight_cols =['LexFound','MsgUniSeg','NewHSWordInSentence','Weighted_Value']

weight_value_list = word_weight =weight_val= []
weight_value=lex_value=Seg_value=0

lexicon_regex= re.compile('~') 
newword_regex=re.compile(',')


lexicon_pd =pd.read_csv('accuracy-folder/accuracy.csv',sep=',')

def weight_calculation(weighted):
    for index,weight in enumerate(weighted.values):
        o_str=AAသူပုန်=ကုလားတွေ=ကျောင်းနွား=ကြံ့ဖွတ်=ကြံ့ဖွတ်ပါတီ=ခိုးဝင်=ခွေးတပ်မတော်=ခွေးတရုတ်=ခွေးဝဲစား=ခွေးသတ်မတော်=ခွေးသား=ခွေးဦးနှောက်=ငလူး=ငှက်နီ=စစ်ခွေး=စစ်အာဏာရှင်=စောက်တရုတ်=တရုတ်ခွေး=တောသား=ထမီခြုံ=ထောင်ထွက်=ဒီမိုခွေးတွေ=ဒေါ်လာစား=နယ်ချဲ့ဗမာအကြမ်းဖက်တပ်=နီပိန်း=နီပေါ=ပြည်ထိုင်ခိုး=ဖင်ယား=ဖွတ်=ဖွတ်ပါတီ=ဖွတ်သူခိုး=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာတွေ=ဗမာစစ်တပ်=ဗမာအကြမ်းဖက်=ဗမာေတွ=ဗလီတွေ=ဘင်ဂါလီ=ဘိန်းစား=မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်=မူစလင်ကုလား=မူဆလင်=မူဆလင်ကုလားတွေ=မျိုးဖြုတ်=မြို့သား=မြေသြဇာ=မွတ်=မွတ်ကုလား=မွတ်ကုလားတွေ=မွတ်ဒေါင်း=မွတ်ပါတီ=ရခိုင်အကြမ်းဖက်သမား=ရခိုင်တပ်တော်AA=ရခိုင်သူပုန်aaအကြမ်းဖက်=ရခိုင်အစွန်းရောက်=ရခိုင်ကုလားတွေ=ရခိုင်တပ်တော်AA=ရခီး=ရခီးတွေ=ရွာသား=လီးကြံ့ဖွတ်=လူရိုင်း=ဝူဟန်=ဝူဟန်တရုတ်=သတ်မတော်=သူခိုး=သူပုန်=သူပုန်မ=သူပုန်လော်ဘီ=သောင်းကျမ်းသူ=အကြမ်းဖက်=အစွန်းရောက်=အဆိပ်သားတွေ=အနီကြောင်=အပြုတ်တိုက်=အမျိုးယုတ်=အမျိုးယုတ်ရှမ်း=အာနာရူးတွေ=အိမ်စောင့်ခွေး=အောက်တန်းကျ=အောက်တန်းစား=ဖွတ်တွေလဒတွေ=string_786 =အဘAA=အမြစ်ပြတ်ရှင်း=ခွေး =Thaiပြန်=gwi=ကမ္ဘာ့ကပ်ရောဂါကြီး=ကုလားပြည်နယ်=ကြံ့ဖွတ်သခိုး=ကြံ့ဖွတ်သူခိုးကောင်=ခွေးဝဲစခွေးသူတောင်းစားခွေး =ခွေးသူတောင်းစားခွေး=ခွေးသူတောင်းစားမီဒီညာ=ငပွေး=ငလူးပဲ=စစ်သူခိုးကြံ့ဖွတ်=စစ်ဦးဘီလူး=စောက်သုံးမကျအစိုးရ=စောင်ကုလား=တရုပ်စုပ်=ထန်းတောသားတွေ=ထမိန်ခြုံနဲ့ဘောမ=နပီဗမာစစ်ခွေးတပ်=နွားကျောင်းသား=ပလောင်တွေ=ပြည်ခိုင်ဖြိုးသူခိုး=ဖင်ကုံး=ဖာသေမစု=ဗမာစစ်အာဏာရှင်အုပ်စု=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာအစိုးရစစ်တပ်=ဗမာအစောရနှင့်ဗမာစစ်တပ်=ဗလီတွေ=မအေလိုးကြံ့ဖွတ်=စောင်ကုလား=0
        လီးဆူး=သုတ်ကြောင်မ=မာမွတ်စူလတန်=မုဒိန်းစစ်တပ်=လူသားစိတ္ကင္းမဲ့=အစွန်းရောက်=အစွန်းရောက်ရခိုင်=အဖျက်သမားaa=ရခိး =အကြမ်းဖက်ကုလားတွေ=အစိမ်းရောင်ခွေး=ရခိုင်နဲ့မပွေး=မွတ်ဒေါင်းခွေ=တစ်မတ်သား=အရိုးကိုက်ဖွတ်ခွေး=ခွေးသူတောင်းစားမီဒီယာ=လူသားစိတ်ကင်းမဲ့=0
        
        LexFound= weight[0]
        MsgUniSeg= weight[1]
        NewHSWordInSentence=weight[2]
        
        if (lexicon_regex.search(str(LexFound))!=None) and (newword_regex.search(str(NewHSWordInSentence))!=None): 
            Lex =LexFound.split("~")
            new =NewHSWordInSentence.split(",")
            new_lex=Lex+new
            for lex in new_lex:
                if lex=='မွတ်ကုလား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလား','Accuracy'].reset_index()
                    မွတ်ကုလား +=float(accuracy['Accuracy'])
                elif lex=='မြို့သား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြို့သား','Accuracy'].reset_index()
                    မြို့သား +=float(accuracy['Accuracy'])

                elif lex=='မြေသြဇာ':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြေသြဇာ','Accuracy'].reset_index()
                    မြေသြဇာ +=float(accuracy['Accuracy'])

                elif lex=='မွတ်':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်','Accuracy'].reset_index()
                    မွတ် +=float(accuracy['Accuracy'])

                elif lex=='မွတ်ကုလားတွေ':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလားတွေ','Accuracy'].reset_index()
                    မွတ်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='မွတ်ဒေါင်း':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်း','Accuracy'].reset_index()
                    မွတ်ဒေါင်း +=float(accuracy['Accuracy'])
                        
                elif lex=='မွတ်ဒေါင်းခွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်းခွေ','Accuracy'].reset_index()
                    မွတ်ဒေါင်းခွေ +=float(accuracy['Accuracy'])

                elif lex=='မွတ်ပါတီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ပါတီ','Accuracy'].reset_index()
                    မွတ်ပါတီ +=float(accuracy['Accuracy'])

                elif lex=='ရခိုင်အကြမ်းဖက်သမား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အကြမ်းဖက်သမား','Accuracy'].reset_index()
                    ရခိုင်အကြမ်းဖက်သမား +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိး' or lex=='ရခီး' or lex=='ရခီး' or lex=='ရခွီး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိး','Accuracy'].reset_index()
                    ရခိး +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်တပ်တော်AA':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်တပ်တော်AA','Accuracy'].reset_index()
                    ရခိုင်တပ်တော်AA +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်နဲ့မပွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်နဲ့မပွေး','Accuracy'].reset_index()
                    ရခိုင်နဲ့မပွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်သူပုန်aaအကြမ်းဖက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်သူပုန်aaအကြမ်းဖက်','Accuracy'].reset_index()
                    ရခိုင်သူပုန်aaအကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်အစွန်းရောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အစွန်းရောက်','Accuracy'].reset_index()
                    ရခိုင်အစွန်းရောက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်ကုလားတွေ','Accuracy'].reset_index()
                    ရခိုင်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခီးတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခီးတွေ','Accuracy'].reset_index()
                    ရခီးတွေ +=float(accuracy['Accuracy'])

                elif lex=='ရွာသား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရွာသား','Accuracy'].reset_index()
                    ရွာသား +=float(accuracy['Accuracy'])
                    
                elif lex=='လီးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးကြံ့ဖွတ်','Accuracy'].reset_index()
                    လီးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='လီးဆူး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးဆူး','Accuracy'].reset_index()
                    လီးဆူး +=float(accuracy['Accuracy'])
                    
                elif lex=='လူရိုင်း': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လူရိုင်း','Accuracy'].reset_index()
                    လူရိုင်း +=float(accuracy['Accuracy'])
                    
                elif lex=='လူသားစိတ္ ကင္းမဲ့' or lex=='လူသားစိတ်ကင်းမဲ့':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လူသားစိတ်ကင်းမဲ့','Accuracy'].reset_index()
                    လူသားစိတ်ကင်းမဲ့ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဝူဟန်':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်','Accuracy'].reset_index()
                    ဝူဟန် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဝူဟန်တရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်တရုတ်','Accuracy'].reset_index()
                    ဝူဟန်တရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='သတ်မတော်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သတ်မတော်','Accuracy'].reset_index()
                    သတ်မတော် +=float(accuracy['Accuracy'])
                    
                elif lex=='သုတ်ကြောင်မ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သုတ်ကြောင်မ','Accuracy'].reset_index()
                    သုတ်ကြောင်မ +=float(accuracy['Accuracy'])
                    
                elif lex=='သူခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူခိုး','Accuracy'].reset_index()
                    သူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်','Accuracy'].reset_index()
                    သူပုန် +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်မ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်မ','Accuracy'].reset_index()
                    သူပုန်မ +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်လော်ဘီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်လော်ဘီ','Accuracy'].reset_index()
                    သူပုန်လော်ဘီ +=float(accuracy['Accuracy'])
                    
                elif lex=='သောင်းကျမ်းသူ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သောင်းကျမ်းသူ','Accuracy'].reset_index()
                    သောင်းကျမ်းသူ +=float(accuracy['Accuracy'])
                    
                elif lex=='အကြမ်းဖက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်','Accuracy'].reset_index()
                    အကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex=='အကြမ်းဖက်ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်ကုလားတွေ','Accuracy'].reset_index()
                    အကြမ်းဖက်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='အစိမ်းရောင်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစိမ်းရောင်ခွေး','Accuracy'].reset_index()
                    အစိမ်းရောင်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='အစွန်းရောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်','Accuracy'].reset_index()
                    အစွန်းရောက် +=float(accuracy['Accuracy'])
                    
                elif lex=='အစွန်းရောက်ရခိုင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်ရခိုင်','Accuracy'].reset_index()
                    အစွန်းရောက်ရခိုင် +=float(accuracy['Accuracy'])
                    
                elif lex=='အဆိပ်သားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဆိပ်သားတွေ','Accuracy'].reset_index()
                    အဆိပ်သားတွေ +=float(accuracy['Accuracy'])
                
                elif lex=='အနီကြောင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အနီကြောင်','Accuracy'].reset_index()
                    အနီကြောင် +=float(accuracy['Accuracy'])
                    
                elif lex=='အပြုတ်တိုက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အပြုတ်တိုက်','Accuracy'].reset_index()
                    အပြုတ်တိုက် +=float(accuracy['Accuracy'])

                elif lex=='အဖျက်သမားaa':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဖျက်သမားaa','Accuracy'].reset_index()
                    အဖျက်သမားaa +=float(accuracy['Accuracy'])
                    
                elif lex=='အဘAA' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဘAA','Accuracy'].reset_index()
                    အဘAA +=float(accuracy['Accuracy'])
                    
                elif lex=='အမျိုးယုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်','Accuracy'].reset_index()
                    အမျိုးယုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='အမျိုးယုတ်ရှမ်း':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်ရှမ်း','Accuracy'].reset_index()
                    အမျိုးယုတ်ရှမ်း +=float(accuracy['Accuracy'])
                    
                elif lex=='အမြစ်ပြတ်ရှင်း':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမြစ်ပြတ်ရှင်း','Accuracy'].reset_index()
                    အမြစ်ပြတ်ရှင်း +=float(accuracy['Accuracy'])
                    
                elif lex=='အာနာရူးတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အာနာရူးတွေ','Accuracy'].reset_index()
                    အာနာရူးတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='အိမ်စောင့်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အိမ်စောင့်ခွေး','Accuracy'].reset_index()
                    အိမ်စောင့်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='အောက်တန်းကျ' or lex=='အောက်တန်းကြ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းကျ','Accuracy'].reset_index()
                    အောက်တန်းကျ +=float(accuracy['Accuracy'])
                    
                elif lex=='အောက်တန်းစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းစား','Accuracy'].reset_index()
                    အောက်တန်းစား +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်တွေလဒတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်တွေလဒတွေ','Accuracy'].reset_index()
                    ဖွတ်တွေလဒတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ေခွး' or lex=='ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေး','Accuracy'].reset_index()
                    ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='၇၈၆':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='၇၈၆','Accuracy'].reset_index()
                    string_786 +=float(accuracy['Accuracy'])
                    
                elif lex== 'AAသူပုန်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='AAသူပုန်','Accuracy'].reset_index()
                    AAသူပုန် +=float(accuracy['Accuracy'])
                    
                elif lex=='Thaiပြန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='Thaiပြန်','Accuracy'].reset_index()
                    Thaiပြန် +=float(accuracy['Accuracy'])
                    
                elif lex=='gwi': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='gwi','Accuracy'].reset_index()
                    gwi +=float(accuracy['Accuracy'])
                    
                elif lex=='ကမ္ဘာ့ကပ်ရောဂါကြီး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကမ္ဘာ့ကပ်ရောဂါကြီး','Accuracy'].reset_index()
                    ကမ္ဘာ့ကပ်ရောဂါကြီး +=float(accuracy['Accuracy'])
                    
                elif lex=='ကုလားပြည်နယ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားပြည်နယ်','Accuracy'].reset_index()
                    ကုလားပြည်နယ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားတွေ','Accuracy'].reset_index()
                    ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ကျောင်းနွား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကျောင်းနွား','Accuracy'].reset_index()
                    ကျောင်းနွား +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်','Accuracy'].reset_index()
                    ကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်သခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သခိုး','Accuracy'].reset_index()
                    ကြံ့ဖွတ်သခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်သူခိုးကောင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သူခိုးကောင်','Accuracy'].reset_index()
                    ကြံ့ဖွတ်သူခိုးကောင် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်ပါတီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်ပါတီ','Accuracy'].reset_index()
                    ကြံ့ဖွတ်ပါတီ +=float(accuracy['Accuracy'])
                    
                elif lex=='ခိုးဝင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခိုးဝင်','Accuracy'].reset_index()
                    ခိုးဝင် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးတပ်မတော်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတပ်မတော်','Accuracy'].reset_index()
                    ခွေးတပ်မတော် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးတရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတရုတ်','Accuracy'].reset_index()
                    ခွေးတရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသား','Accuracy'].reset_index()
                    ခွေးသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသူတောင်းစားခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားခွေး','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားခွေး +=float(accuracy['Accuracy'])
                    
                elif lex== 'ခွေးသူတောင်းစားမီဒီညာ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီညာ','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားမီဒီညာ +=float(accuracy['Accuracy'])
                
                elif lex=='ခွေးဦးနှောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဦးနှောက်','Accuracy'].reset_index()
                    ခွေးဦးနှောက် +=float(accuracy['Accuracy'])
                
                elif lex=='ခွေးဝဲစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဝဲစား','Accuracy'].reset_index()
                    ခွေးဝဲစား +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသတ်မတော်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသတ်မတော်','Accuracy'].reset_index()
                    ခွေးသတ်မတော် +=float(accuracy['Accuracy'])

                elif lex=='ငပွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငပွေး','Accuracy'].reset_index()
                    ငပွေး +=float(accuracy['Accuracy'])

                elif lex=='ငလူး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူး','Accuracy'].reset_index()
                    ငလူး +=float(accuracy['Accuracy'])
                    
                elif lex=='ငလူးပဲ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူးပဲ','Accuracy'].reset_index()
                    ငလူးပဲ +=float(accuracy['Accuracy'])
                
                elif lex=='ငှက်နီ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငှက်နီ','Accuracy'].reset_index()
                    ငှက်နီ +=float(accuracy['Accuracy'])
                    
                elif lex== 'စစ်သူခိုးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်သူခိုးကြံ့ဖွတ်','Accuracy'].reset_index()
                    စစ်သူခိုးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်အာဏာရှင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်အာဏာရှင်','Accuracy'].reset_index()
                    စစ်အာဏာရှင် +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ခွေး','Accuracy'].reset_index()
                    စစ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်ဦးဘီလူး': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ဦးဘီလူး','Accuracy'].reset_index()
                    စစ်ဦးဘီလူး +=float(accuracy['Accuracy'])
                    
                elif lex=='စောက်တရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်တရုတ်','Accuracy'].reset_index()
                    စောက်တရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='စောက်သုံးမကျအစိုးရ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်သုံးမကျအစိုးရ','Accuracy'].reset_index()
                    စောက်သုံးမကျအစိုးရ +=float(accuracy['Accuracy'])
                    
                elif lex=='စောင်ကုလား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောင်ကုလား','Accuracy'].reset_index()
                    စောင်ကုလား +=float(accuracy['Accuracy'])
                    
                elif lex=='တရုပ်စုပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုပ်စုပ်','Accuracy'].reset_index()
                    တရုပ်စုပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='တရုတ်ခွေး' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုတ်ခွေး','Accuracy'].reset_index()
                    တရုတ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='တောသား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တောသား','Accuracy'].reset_index()
                    တောသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ထန်းတောသားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထန်းတောသားတွေ','Accuracy'].reset_index()
                    ထန်းတောသားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထမိန်ခြုံနဲ့ဘောမ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမိန်ခြုံနဲ့ဘောမ','Accuracy'].reset_index()
                    ထမိန်ခြုံနဲ့ဘောမ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထမီခြုံ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမီခြုံ','Accuracy'].reset_index()
                    ထမီခြုံ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထောင်ထွက်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထောင်ထွက်','Accuracy'].reset_index()
                    ထောင်ထွက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဒီမိုခွေးတွေ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒီမိုခွေးတွေ','Accuracy'].reset_index()
                    ဒီမိုခွေးတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဒေါ်လာစား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒေါ်လာစား','Accuracy'].reset_index()
                    ဒေါ်လာစား +=float(accuracy['Accuracy'])
                
                elif lex== 'နပီဗမာစစ်\u200b\u200bခွေးတပ်' or lex=='နပီဗမာစစ်ခွေးတပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နပီဗမာစစ်ခွေးတပ်','Accuracy'].reset_index()
                    နပီဗမာစစ်ခွေးတပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='နီပိန်း' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပိန်း','Accuracy'].reset_index()
                    နီပိန်း +=float(accuracy['Accuracy'])
                    
                elif lex=='နီပေါ': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပေါ','Accuracy'].reset_index()
                    နီပေါ +=float(accuracy['Accuracy'])
                    
                elif lex=='နွားကျောင်းသား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နွားကျောင်းသား','Accuracy'].reset_index()
                    နွားကျောင်းသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ပလောင်တွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပလောင်တွေ','Accuracy'].reset_index()
                    ပလောင်တွေ +=float(accuracy['Accuracy'])

                elif lex=='ပြည်ခိုင်ဖြိုးသူခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ခိုင်ဖြိုးသူခိုး','Accuracy'].reset_index()
                    ပြည်ခိုင်ဖြိုးသူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ပြည်ထိုင်ခိုး' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ထိုင်ခိုး','Accuracy'].reset_index()
                    ပြည်ထိုင်ခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖင်ကုံး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ကုံး','Accuracy'].reset_index()
                    ဖင်ကုံး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖင်ယား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ယား','Accuracy'].reset_index()
                    ဖင်ယား +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖာသေမစု': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖာသေမစု','Accuracy'].reset_index()
                    ဖာသေမစု +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်သူခိုး': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်သူခိုး','Accuracy'].reset_index()
                    ဖွတ်သူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်','Accuracy'].reset_index()
                    ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်ပါတီ' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်ပါတီ','Accuracy'].reset_index()
                    ဖွတ်ပါတီ +=float(accuracy['Accuracy'])

                elif lex=='ဗမာတွေ' or lex=='ဗမာ' or lex=='ဗမာေတွ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာတွေ','Accuracy'].reset_index()
                    ဗမာတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာစစ်အာဏာရှင်အုပ်စု': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်အာဏာရှင်အုပ်စု','Accuracy'].reset_index()
                    ဗမာစစ်အာဏာရှင်အုပ်စု +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာသောင်းကြမ်းသူအဖွဲ့':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာသောင်းကြမ်းသူအဖွဲ့','Accuracy'].reset_index()
                    ဗမာသောင်းကြမ်းသူအဖွဲ့ +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာအစိုးရစစ်တပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစိုးရစစ်တပ်','Accuracy'].reset_index()
                    ဗမာအစိုးရစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာအစောရနှင့်ဗမာစစ်တပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစောရနှင့်ဗမာစစ်တပ်','Accuracy'].reset_index()
                    ဗမာအစောရနှင့်ဗမာစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာစစ်တပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်တပ်','Accuracy'].reset_index()
                    ဗမာစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာအကြမ်းဖက်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအကြမ်းဖက်','Accuracy'].reset_index()
                    ဗမာအကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗလီတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗလီတွေ','Accuracy'].reset_index()
                    ဗလီတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဘင်ဂါလီ' or lex=='ဘင်္ဂါလီ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘင်ဂါလီ','Accuracy'].reset_index()
                    ဘင်ဂါလီ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဘိန်းစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘိန်းစား','Accuracy'].reset_index()
                    ဘိန်းစား +=float(accuracy['Accuracy'])
                    
                elif lex== 'မအေလိုးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မအေလိုးကြံ့ဖွတ်','Accuracy'].reset_index()
                    မအေလိုးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်','Accuracy'].reset_index()
                    မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက် +=float(accuracy['Accuracy'])
                    
                elif lex== 'မာမွတ်စူလတန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာမွတ်စူလတန်','Accuracy'].reset_index()
                    မာမွတ်စူလတန် +=float(accuracy['Accuracy'])
                    
                elif lex=='မုဒိန်းစစ်တပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မုဒိန်းစစ်တပ်','Accuracy'].reset_index()
                    မုဒိန်းစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex== 'မူစလင်ကုလား' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူစလင်ကုလား','Accuracy'].reset_index()
                    မူစလင်ကုလား +=float(accuracy['Accuracy'])
                    
                elif lex=='မူဆလင်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်','Accuracy'].reset_index()
                    မူဆလင် +=float(accuracy['Accuracy'])
                    
                elif lex=='မူဆလင်ကုလားတွေ': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်ကုလားတွေ','Accuracy'].reset_index()
                    မူဆလင်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='မျိုးဖြုတ်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မျိုးဖြုတ်','Accuracy'].reset_index()
                    မျိုးဖြုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='တစ်မတ်သား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တစ်မတ်သား','Accuracy'].reset_index()
                    တစ်မတ်သား +=float(accuracy['Accuracy'])
                    
                elif lex=='အရိုးကိုက်ဖွတ်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အရိုးကိုက်ဖွတ်ခွေး','Accuracy'].reset_index()
                    အရိုးကိုက်ဖွတ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသူတောင်းစားမီဒီယာ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီယာ','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားမီဒီယာ +=float(accuracy['Accuracy'])
                    

            weight_value = မွတ်ကုလား+မြို့သား+မြေသြဇာ+မွတ်+မွတ်ကုလားတွေ+မွတ်ဒေါင်း+မွတ်ဒေါင်းခွေ+မွတ်ပါတီ+ရခိုင်အကြမ်းဖက်သမား+ရခိး+ရခီးတွေ+ရွာသား+လီးကြံ့ဖွတ်+လီးဆူး+လူရိုင်း+လူသားစိတ္ကင္းမဲ့+ဝူဟန်+ဝူဟန်တရုတ်+သတ်မတော်+သုတ်ကြောင်မ+သူခိုး+သူပုန်+သူပုန်မ+သူပုန်လော်ဘီ+သောင်းကျမ်းသူ+အကြမ်းဖက်+အကြမ်းဖက်ကုလားတွေ+အစိမ်းရောင်ခွေး+အစွန်းရောက်+အစွန်းရောက်ရခိုင်+အဆိပ်သားတွေ+အနီကြောင်+အပြုတ်တိုက်+အဖျက်သမားaa+အဘAA+အမျိုးယုတ်+အမျိုးယုတ်ရှမ်း+အမြစ်ပြတ်ရှင်း+အာနာရူးတွေ+အာနာရူးတွေ+အိမ်စောင့်ခွေး+အောက်တန်းကျ+အောက်တန်းစား+ဖွတ်တွေလဒတွေ+ခွေး+string_786+AAသူပုန်+Thaiပြန်+gwi+ကမ္ဘာ့ကပ်ရောဂါကြီး+ကုလားပြည်နယ်+ကုလားတွေ+ကျောင်းနွား+ကြံ့ဖွတ်+ကြံ့ဖွတ်သခိုး+ကြံ့ဖွတ်သူခိုးကောင်+ကြံ့ဖွတ်ပါတီ+ခိုးဝင်+ခွေးတပ်မတော်+ခွေးတရုတ်+ခွေးသား+ခွေးသူတောင်းစားခွေး+ခွေးသူတောင်းစားမီဒီညာ+ခွေးဦးနှောက်+ခွေးဝဲစား+ခွေးသတ်မတော်+ငပွေး+ငလူး+ငလူးပဲ+ငှက်နီ+စစ်သူခိုးကြံ့ဖွတ်+စစ်အာဏာရှင်+စစ်ခွေး+စစ်ဦးဘီလူး+စောက်တရုတ်+စောက်သုံးမကျအစိုးရ+စောင်ကုလား+တရုပ်စုပ်+တရုတ်ခွေး+တောသား+ထန်းတောသားတွေ+ထမိန်ခြုံနဲ့ဘောမ+ထမီခြုံ+ထောင်ထွက်+ဒီမိုခွေးတွေ+ဒေါ်လာစား+နပီဗမာစစ်ခွေးတပ်+နီပိန်း+နီပေါ+နွားကျောင်းသား+ပလောင်တွေ+ပြည်ခိုင်ဖြိုးသူခိုး+ပြည်ထိုင်ခိုး+ဖင်ကုံး+ဖင်ယား+ဖာသေမစု+ဖွတ်သူခိုး+ဖွတ်+ဖွတ်ပါတီ+ဗမာတွေ+ဗမာစစ်အာဏာရှင်အုပ်စု+ဗမာသောင်းကြမ်းသူအဖွဲ့+ဗမာအစိုးရစစ်တပ်+ဗမာအစောရနှင့်ဗမာစစ်တပ်+ဗမာစစ်တပ်+ဗမာအကြမ်းဖက်+ဗလီတွေ+ဘင်ဂါလီ+ဘိန်းစား+မအေလိုးကြံ့ဖွတ်+မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်+မာမွတ်စူလတန်+မုဒိန်းစစ်တပ်+မူစလင်ကုလား+မူဆလင်+မူဆလင်ကုလားတွေ+မျိုးဖြုတ်+တစ်မတ်သား+အရိုးကိုက်ဖွတ်ခွေး+ခွေးသူတောင်းစားမီဒီယာ

            word_weight.append([LexFound,MsgUniSeg,NewHSWordInSentence,weight_value])
        elif (lexicon_regex.search(str(LexFound))!=None) and (newword_regex.search(str(NewHSWordInSentence))==None): 
            lex=LexFound.replace(" ", "")
            if isinstance(lex,str)==False:pass
            
            else: 
                if isinstance(NewHSWordInSentence,str)==False:
                    Lex=lex.split("~")
                else:
                    Lex=lex+'~'+NewHSWordInSentence
                    Lex =lex.split("~")
            for lex in Lex:
                if lex=='မွတ်ကုလား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလား','Accuracy'].reset_index()
                    မွတ်ကုလား +=float(accuracy['Accuracy'])
                elif lex=='မြို့သား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြို့သား','Accuracy'].reset_index()
                    မြို့သား +=float(accuracy['Accuracy'])

                elif lex=='မြေသြဇာ':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြေသြဇာ','Accuracy'].reset_index()
                    မြေသြဇာ +=float(accuracy['Accuracy'])

                elif lex=='မွတ်':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်','Accuracy'].reset_index()
                    မွတ် +=float(accuracy['Accuracy'])

                elif lex=='မွတ်ကုလားတွေ':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလားတွေ','Accuracy'].reset_index()
                    မွတ်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='မွတ်ဒေါင်း':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်း','Accuracy'].reset_index()
                    မွတ်ဒေါင်း +=float(accuracy['Accuracy'])
                        
                elif lex=='မွတ်ဒေါင်းခွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်းခွေ','Accuracy'].reset_index()
                    မွတ်ဒေါင်းခွေ +=float(accuracy['Accuracy'])

                elif lex=='မွတ်ပါတီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ပါတီ','Accuracy'].reset_index()
                    မွတ်ပါတီ +=float(accuracy['Accuracy'])

                elif lex=='ရခိုင်အကြမ်းဖက်သမား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အကြမ်းဖက်သမား','Accuracy'].reset_index()
                    ရခိုင်အကြမ်းဖက်သမား +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိး' or lex=='ရခီး' or lex=='ရခီး' or lex=='ရခွီး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိး','Accuracy'].reset_index()
                    ရခိး +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်တပ်တော်AA':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်တပ်တော်AA','Accuracy'].reset_index()
                    ရခိုင်တပ်တော်AA +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်နဲ့မပွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်နဲ့မပွေး','Accuracy'].reset_index()
                    ရခိုင်နဲ့မပွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်သူပုန်aaအကြမ်းဖက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်သူပုန်aaအကြမ်းဖက်','Accuracy'].reset_index()
                    ရခိုင်သူပုန်aaအကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်အစွန်းရောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အစွန်းရောက်','Accuracy'].reset_index()
                    ရခိုင်အစွန်းရောက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်ကုလားတွေ','Accuracy'].reset_index()
                    ရခိုင်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခီးတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခီးတွေ','Accuracy'].reset_index()
                    ရခီးတွေ +=float(accuracy['Accuracy'])

                elif lex=='ရွာသား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရွာသား','Accuracy'].reset_index()
                    ရွာသား +=float(accuracy['Accuracy'])
                    
                elif lex=='လီးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးကြံ့ဖွတ်','Accuracy'].reset_index()
                    လီးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='လီးဆူး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးဆူး','Accuracy'].reset_index()
                    လီးဆူး +=float(accuracy['Accuracy'])
                    
                elif lex=='လူရိုင်း': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လူရိုင်း','Accuracy'].reset_index()
                    လူရိုင်း +=float(accuracy['Accuracy'])
                    
                elif lex=='လူသားစိတ္ ကင္းမဲ့' or lex=='လူသားစိတ်ကင်းမဲ့':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လူသားစိတ်ကင်းမဲ့','Accuracy'].reset_index()
                    လူသားစိတ်ကင်းမဲ့ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဝူဟန်':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်','Accuracy'].reset_index()
                    ဝူဟန် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဝူဟန်တရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်တရုတ်','Accuracy'].reset_index()
                    ဝူဟန်တရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='သတ်မတော်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သတ်မတော်','Accuracy'].reset_index()
                    သတ်မတော် +=float(accuracy['Accuracy'])
                    
                elif lex=='သုတ်ကြောင်မ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သုတ်ကြောင်မ','Accuracy'].reset_index()
                    သုတ်ကြောင်မ +=float(accuracy['Accuracy'])
                    
                elif lex=='သူခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူခိုး','Accuracy'].reset_index()
                    သူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်','Accuracy'].reset_index()
                    သူပုန် +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်မ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်မ','Accuracy'].reset_index()
                    သူပုန်မ +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်လော်ဘီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်လော်ဘီ','Accuracy'].reset_index()
                    သူပုန်လော်ဘီ +=float(accuracy['Accuracy'])
                    
                elif lex=='သောင်းကျမ်းသူ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သောင်းကျမ်းသူ','Accuracy'].reset_index()
                    သောင်းကျမ်းသူ +=float(accuracy['Accuracy'])
                    
                elif lex=='အကြမ်းဖက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်','Accuracy'].reset_index()
                    အကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex=='အကြမ်းဖက်ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်ကုလားတွေ','Accuracy'].reset_index()
                    အကြမ်းဖက်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='အစိမ်းရောင်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစိမ်းရောင်ခွေး','Accuracy'].reset_index()
                    အစိမ်းရောင်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='အစွန်းရောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်','Accuracy'].reset_index()
                    အစွန်းရောက် +=float(accuracy['Accuracy'])
                    
                elif lex=='အစွန်းရောက်ရခိုင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်ရခိုင်','Accuracy'].reset_index()
                    အစွန်းရောက်ရခိုင် +=float(accuracy['Accuracy'])
                    
                elif lex=='အဆိပ်သားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဆိပ်သားတွေ','Accuracy'].reset_index()
                    အဆိပ်သားတွေ +=float(accuracy['Accuracy'])
                
                elif lex=='အနီကြောင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အနီကြောင်','Accuracy'].reset_index()
                    အနီကြောင် +=float(accuracy['Accuracy'])
                    
                elif lex=='အပြုတ်တိုက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အပြုတ်တိုက်','Accuracy'].reset_index()
                    အပြုတ်တိုက် +=float(accuracy['Accuracy'])

                elif lex=='အဖျက်သမားaa':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဖျက်သမားaa','Accuracy'].reset_index()
                    အဖျက်သမားaa +=float(accuracy['Accuracy'])
                    
                elif lex=='အဘAA' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဘAA','Accuracy'].reset_index()
                    အဘAA +=float(accuracy['Accuracy'])
                    
                elif lex=='အမျိုးယုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်','Accuracy'].reset_index()
                    အမျိုးယုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='အမျိုးယုတ်ရှမ်း':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်ရှမ်း','Accuracy'].reset_index()
                    အမျိုးယုတ်ရှမ်း +=float(accuracy['Accuracy'])
                    
                elif lex=='အမြစ်ပြတ်ရှင်း':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမြစ်ပြတ်ရှင်း','Accuracy'].reset_index()
                    အမြစ်ပြတ်ရှင်း +=float(accuracy['Accuracy'])
                    
                elif lex=='အာနာရူးတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အာနာရူးတွေ','Accuracy'].reset_index()
                    အာနာရူးတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='အိမ်စောင့်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အိမ်စောင့်ခွေး','Accuracy'].reset_index()
                    အိမ်စောင့်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='အောက်တန်းကျ' or lex=='အောက်တန်းကြ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းကျ','Accuracy'].reset_index()
                    အောက်တန်းကျ +=float(accuracy['Accuracy'])
                    
                elif lex=='အောက်တန်းစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းစား','Accuracy'].reset_index()
                    အောက်တန်းစား +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်တွေလဒတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်တွေလဒတွေ','Accuracy'].reset_index()
                    ဖွတ်တွေလဒတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ေခွး' or lex=='ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေး','Accuracy'].reset_index()
                    ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='၇၈၆':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='၇၈၆','Accuracy'].reset_index()
                    string_786 +=float(accuracy['Accuracy'])
                    
                elif lex== 'AAသူပုန်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='AAသူပုန်','Accuracy'].reset_index()
                    AAသူပုန် +=float(accuracy['Accuracy'])
                    
                elif lex=='Thaiပြန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='Thaiပြန်','Accuracy'].reset_index()
                    Thaiပြန် +=float(accuracy['Accuracy'])
                    
                elif lex=='gwi': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='gwi','Accuracy'].reset_index()
                    gwi +=float(accuracy['Accuracy'])
                    
                elif lex=='ကမ္ဘာ့ကပ်ရောဂါကြီး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကမ္ဘာ့ကပ်ရောဂါကြီး','Accuracy'].reset_index()
                    ကမ္ဘာ့ကပ်ရောဂါကြီး +=float(accuracy['Accuracy'])
                    
                elif lex=='ကုလားပြည်နယ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားပြည်နယ်','Accuracy'].reset_index()
                    ကုလားပြည်နယ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားတွေ','Accuracy'].reset_index()
                    ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ကျောင်းနွား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကျောင်းနွား','Accuracy'].reset_index()
                    ကျောင်းနွား +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်','Accuracy'].reset_index()
                    ကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်သခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သခိုး','Accuracy'].reset_index()
                    ကြံ့ဖွတ်သခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်သူခိုးကောင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သူခိုးကောင်','Accuracy'].reset_index()
                    ကြံ့ဖွတ်သူခိုးကောင် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်ပါတီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်ပါတီ','Accuracy'].reset_index()
                    ကြံ့ဖွတ်ပါတီ +=float(accuracy['Accuracy'])
                    
                elif lex=='ခိုးဝင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခိုးဝင်','Accuracy'].reset_index()
                    ခိုးဝင် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးတပ်မတော်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတပ်မတော်','Accuracy'].reset_index()
                    ခွေးတပ်မတော် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးတရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတရုတ်','Accuracy'].reset_index()
                    ခွေးတရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသား','Accuracy'].reset_index()
                    ခွေးသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသူတောင်းစားခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားခွေး','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားခွေး +=float(accuracy['Accuracy'])
                    
                elif lex== 'ခွေးသူတောင်းစားမီဒီညာ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီညာ','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားမီဒီညာ +=float(accuracy['Accuracy'])
                
                elif lex=='ခွေးဦးနှောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဦးနှောက်','Accuracy'].reset_index()
                    ခွေးဦးနှောက် +=float(accuracy['Accuracy'])
                
                elif lex=='ခွေးဝဲစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဝဲစား','Accuracy'].reset_index()
                    ခွေးဝဲစား +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသတ်မတော်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသတ်မတော်','Accuracy'].reset_index()
                    ခွေးသတ်မတော် +=float(accuracy['Accuracy'])

                elif lex=='ငပွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငပွေး','Accuracy'].reset_index()
                    ငပွေး +=float(accuracy['Accuracy'])

                elif lex=='ငလူး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူး','Accuracy'].reset_index()
                    ငလူး +=float(accuracy['Accuracy'])
                    
                elif lex=='ငလူးပဲ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူးပဲ','Accuracy'].reset_index()
                    ငလူးပဲ +=float(accuracy['Accuracy'])
                
                elif lex=='ငှက်နီ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငှက်နီ','Accuracy'].reset_index()
                    ငှက်နီ +=float(accuracy['Accuracy'])
                    
                elif lex== 'စစ်သူခိုးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်သူခိုးကြံ့ဖွတ်','Accuracy'].reset_index()
                    စစ်သူခိုးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်အာဏာရှင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်အာဏာရှင်','Accuracy'].reset_index()
                    စစ်အာဏာရှင် +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ခွေး','Accuracy'].reset_index()
                    စစ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်ဦးဘီလူး': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ဦးဘီလူး','Accuracy'].reset_index()
                    စစ်ဦးဘီလူး +=float(accuracy['Accuracy'])
                    
                elif lex=='စောက်တရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်တရုတ်','Accuracy'].reset_index()
                    စောက်တရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='စောက်သုံးမကျအစိုးရ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်သုံးမကျအစိုးရ','Accuracy'].reset_index()
                    စောက်သုံးမကျအစိုးရ +=float(accuracy['Accuracy'])
                    
                elif lex=='စောင်ကုလား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောင်ကုလား','Accuracy'].reset_index()
                    စောင်ကုလား +=float(accuracy['Accuracy'])
                    
                elif lex=='တရုပ်စုပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုပ်စုပ်','Accuracy'].reset_index()
                    တရုပ်စုပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='တရုတ်ခွေး' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုတ်ခွေး','Accuracy'].reset_index()
                    တရုတ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='တောသား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တောသား','Accuracy'].reset_index()
                    တောသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ထန်းတောသားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထန်းတောသားတွေ','Accuracy'].reset_index()
                    ထန်းတောသားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထမိန်ခြုံနဲ့ဘောမ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမိန်ခြုံနဲ့ဘောမ','Accuracy'].reset_index()
                    ထမိန်ခြုံနဲ့ဘောမ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထမီခြုံ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမီခြုံ','Accuracy'].reset_index()
                    ထမီခြုံ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထောင်ထွက်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထောင်ထွက်','Accuracy'].reset_index()
                    ထောင်ထွက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဒီမိုခွေးတွေ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒီမိုခွေးတွေ','Accuracy'].reset_index()
                    ဒီမိုခွေးတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဒေါ်လာစား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒေါ်လာစား','Accuracy'].reset_index()
                    ဒေါ်လာစား +=float(accuracy['Accuracy'])
                
                elif lex== 'နပီဗမာစစ်\u200b\u200bခွေးတပ်' or lex=='နပီဗမာစစ်ခွေးတပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နပီဗမာစစ်ခွေးတပ်','Accuracy'].reset_index()
                    နပီဗမာစစ်ခွေးတပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='နီပိန်း' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပိန်း','Accuracy'].reset_index()
                    နီပိန်း +=float(accuracy['Accuracy'])
                    
                elif lex=='နီပေါ': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပေါ','Accuracy'].reset_index()
                    နီပေါ +=float(accuracy['Accuracy'])
                    
                elif lex=='နွားကျောင်းသား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နွားကျောင်းသား','Accuracy'].reset_index()
                    နွားကျောင်းသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ပလောင်တွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပလောင်တွေ','Accuracy'].reset_index()
                    ပလောင်တွေ +=float(accuracy['Accuracy'])

                elif lex=='ပြည်ခိုင်ဖြိုးသူခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ခိုင်ဖြိုးသူခိုး','Accuracy'].reset_index()
                    ပြည်ခိုင်ဖြိုးသူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ပြည်ထိုင်ခိုး' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ထိုင်ခိုး','Accuracy'].reset_index()
                    ပြည်ထိုင်ခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖင်ကုံး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ကုံး','Accuracy'].reset_index()
                    ဖင်ကုံး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖင်ယား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ယား','Accuracy'].reset_index()
                    ဖင်ယား +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖာသေမစု': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖာသေမစု','Accuracy'].reset_index()
                    ဖာသေမစု +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်သူခိုး': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်သူခိုး','Accuracy'].reset_index()
                    ဖွတ်သူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်','Accuracy'].reset_index()
                    ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်ပါတီ' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်ပါတီ','Accuracy'].reset_index()
                    ဖွတ်ပါတီ +=float(accuracy['Accuracy'])

                elif lex=='ဗမာတွေ' or lex=='ဗမာ' or lex=='ဗမာေတွ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာတွေ','Accuracy'].reset_index()
                    ဗမာတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာစစ်အာဏာရှင်အုပ်စု': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်အာဏာရှင်အုပ်စု','Accuracy'].reset_index()
                    ဗမာစစ်အာဏာရှင်အုပ်စု +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာသောင်းကြမ်းသူအဖွဲ့':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာသောင်းကြမ်းသူအဖွဲ့','Accuracy'].reset_index()
                    ဗမာသောင်းကြမ်းသူအဖွဲ့ +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာအစိုးရစစ်တပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစိုးရစစ်တပ်','Accuracy'].reset_index()
                    ဗမာအစိုးရစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာအစောရနှင့်ဗမာစစ်တပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစောရနှင့်ဗမာစစ်တပ်','Accuracy'].reset_index()
                    ဗမာအစောရနှင့်ဗမာစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာစစ်တပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်တပ်','Accuracy'].reset_index()
                    ဗမာစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာအကြမ်းဖက်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအကြမ်းဖက်','Accuracy'].reset_index()
                    ဗမာအကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗလီတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗလီတွေ','Accuracy'].reset_index()
                    ဗလီတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဘင်ဂါလီ' or lex=='ဘင်္ဂါလီ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘင်ဂါလီ','Accuracy'].reset_index()
                    ဘင်ဂါလီ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဘိန်းစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘိန်းစား','Accuracy'].reset_index()
                    ဘိန်းစား +=float(accuracy['Accuracy'])
                    
                elif lex== 'မအေလိုးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မအေလိုးကြံ့ဖွတ်','Accuracy'].reset_index()
                    မအေလိုးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်','Accuracy'].reset_index()
                    မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက် +=float(accuracy['Accuracy'])
                    
                elif lex== 'မာမွတ်စူလတန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာမွတ်စူလတန်','Accuracy'].reset_index()
                    မာမွတ်စူလတန် +=float(accuracy['Accuracy'])
                    
                elif lex=='မုဒိန်းစစ်တပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မုဒိန်းစစ်တပ်','Accuracy'].reset_index()
                    မုဒိန်းစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex== 'မူစလင်ကုလား' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူစလင်ကုလား','Accuracy'].reset_index()
                    မူစလင်ကုလား +=float(accuracy['Accuracy'])
                    
                elif lex=='မူဆလင်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်','Accuracy'].reset_index()
                    မူဆလင် +=float(accuracy['Accuracy'])
                    
                elif lex=='မူဆလင်ကုလားတွေ': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်ကုလားတွေ','Accuracy'].reset_index()
                    မူဆလင်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='မျိုးဖြုတ်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မျိုးဖြုတ်','Accuracy'].reset_index()
                    မျိုးဖြုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='တစ်မတ်သား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တစ်မတ်သား','Accuracy'].reset_index()
                    တစ်မတ်သား +=float(accuracy['Accuracy'])
                    
                elif lex=='အရိုးကိုက်ဖွတ်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အရိုးကိုက်ဖွတ်ခွေး','Accuracy'].reset_index()
                    အရိုးကိုက်ဖွတ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသူတောင်းစားမီဒီယာ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီယာ','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားမီဒီယာ +=float(accuracy['Accuracy'])
                    
            weight_value = မွတ်ကုလား+မြို့သား+မြေသြဇာ+မွတ်+မွတ်ကုလားတွေ+မွတ်ဒေါင်း+မွတ်ဒေါင်းခွေ+မွတ်ပါတီ+ရခိုင်အကြမ်းဖက်သမား+ရခိး+ရခီးတွေ+ရွာသား+လီးကြံ့ဖွတ်+လီးဆူး+လူရိုင်း+လူသားစိတ္ကင္းမဲ့+ဝူဟန်+ဝူဟန်တရုတ်+သတ်မတော်+သုတ်ကြောင်မ+သူခိုး+သူပုန်+သူပုန်မ+သူပုန်လော်ဘီ+သောင်းကျမ်းသူ+အကြမ်းဖက်+အကြမ်းဖက်ကုလားတွေ+အစိမ်းရောင်ခွေး+အစွန်းရောက်+အစွန်းရောက်ရခိုင်+အဆိပ်သားတွေ+အနီကြောင်+အပြုတ်တိုက်+အဖျက်သမားaa+အဘAA+အမျိုးယုတ်+အမျိုးယုတ်ရှမ်း+အမြစ်ပြတ်ရှင်း+အာနာရူးတွေ+အာနာရူးတွေ+အိမ်စောင့်ခွေး+အောက်တန်းကျ+အောက်တန်းစား+ဖွတ်တွေလဒတွေ+ခွေး+string_786+AAသူပုန်+Thaiပြန်+gwi+ကမ္ဘာ့ကပ်ရောဂါကြီး+ကုလားပြည်နယ်+ကုလားတွေ+ကျောင်းနွား+ကြံ့ဖွတ်+ကြံ့ဖွတ်သခိုး+ကြံ့ဖွတ်သူခိုးကောင်+ကြံ့ဖွတ်ပါတီ+ခိုးဝင်+ခွေးတပ်မတော်+ခွေးတရုတ်+ခွေးသား+ခွေးသူတောင်းစားခွေး+ခွေးသူတောင်းစားမီဒီညာ+ခွေးဦးနှောက်+ခွေးဝဲစား+ခွေးသတ်မတော်+ငပွေး+ငလူး+ငလူးပဲ+ငှက်နီ+စစ်သူခိုးကြံ့ဖွတ်+စစ်အာဏာရှင်+စစ်ခွေး+စစ်ဦးဘီလူး+စောက်တရုတ်+စောက်သုံးမကျအစိုးရ+စောင်ကုလား+တရုပ်စုပ်+တရုတ်ခွေး+တောသား+ထန်းတောသားတွေ+ထမိန်ခြုံနဲ့ဘောမ+ထမီခြုံ+ထောင်ထွက်+ဒီမိုခွေးတွေ+ဒေါ်လာစား+နပီဗမာစစ်ခွေးတပ်+နီပိန်း+နီပေါ+နွားကျောင်းသား+ပလောင်တွေ+ပြည်ခိုင်ဖြိုးသူခိုး+ပြည်ထိုင်ခိုး+ဖင်ကုံး+ဖင်ယား+ဖာသေမစု+ဖွတ်သူခိုး+ဖွတ်+ဖွတ်ပါတီ+ဗမာတွေ+ဗမာစစ်အာဏာရှင်အုပ်စု+ဗမာသောင်းကြမ်းသူအဖွဲ့+ဗမာအစိုးရစစ်တပ်+ဗမာအစောရနှင့်ဗမာစစ်တပ်+ဗမာစစ်တပ်+ဗမာအကြမ်းဖက်+ဗလီတွေ+ဘင်ဂါလီ+ဘိန်းစား+မအေလိုးကြံ့ဖွတ်+မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်+မာမွတ်စူလတန်+မုဒိန်းစစ်တပ်+မူစလင်ကုလား+မူဆလင်+မူဆလင်ကုလားတွေ+မျိုးဖြုတ်+တစ်မတ်သား+အရိုးကိုက်ဖွတ်ခွေး+ခွေးသူတောင်းစားမီဒီယာ
            word_weight.append([LexFound,MsgUniSeg,NewHSWordInSentence,weight_value])
            
        elif (lexicon_regex.search(str(LexFound))==None) and (newword_regex.search(str(NewHSWordInSentence))!=None): 
            lex=LexFound.replace(" ", "")
            NewHSWord=NewHSWordInSentence.replace(" ", "")
            NewHSWord=lex+','+NewHSWord
            new =NewHSWord.split(",")
            for lex in new:
                if lex=='မွတ်ကုလား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလား','Accuracy'].reset_index()
                    မွတ်ကုလား +=float(accuracy['Accuracy'])
                elif lex=='မြို့သား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြို့သား','Accuracy'].reset_index()
                    မြို့သား +=float(accuracy['Accuracy'])

                elif lex=='မြေသြဇာ':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြေသြဇာ','Accuracy'].reset_index()
                    မြေသြဇာ +=float(accuracy['Accuracy'])

                elif lex=='မွတ်':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်','Accuracy'].reset_index()
                    မွတ် +=float(accuracy['Accuracy'])

                elif lex=='မွတ်ကုလားတွေ':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလားတွေ','Accuracy'].reset_index()
                    မွတ်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='မွတ်ဒေါင်း':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်း','Accuracy'].reset_index()
                    မွတ်ဒေါင်း +=float(accuracy['Accuracy'])
                        
                elif lex=='မွတ်ဒေါင်းခွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်းခွေ','Accuracy'].reset_index()
                    မွတ်ဒေါင်းခွေ +=float(accuracy['Accuracy'])

                elif lex=='မွတ်ပါတီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ပါတီ','Accuracy'].reset_index()
                    မွတ်ပါတီ +=float(accuracy['Accuracy'])

                elif lex=='ရခိုင်အကြမ်းဖက်သမား':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အကြမ်းဖက်သမား','Accuracy'].reset_index()
                    ရခိုင်အကြမ်းဖက်သမား +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိး' or lex=='ရခီး' or lex=='ရခီး' or lex=='ရခွီး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိး','Accuracy'].reset_index()
                    ရခိး +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်တပ်တော်AA':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်တပ်တော်AA','Accuracy'].reset_index()
                    ရခိုင်တပ်တော်AA +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်နဲ့မပွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်နဲ့မပွေး','Accuracy'].reset_index()
                    ရခိုင်နဲ့မပွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်သူပုန်aaအကြမ်းဖက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်သူပုန်aaအကြမ်းဖက်','Accuracy'].reset_index()
                    ရခိုင်သူပုန်aaအကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်အစွန်းရောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အစွန်းရောက်','Accuracy'].reset_index()
                    ရခိုင်အစွန်းရောက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခိုင်ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်ကုလားတွေ','Accuracy'].reset_index()
                    ရခိုင်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ရခီးတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခီးတွေ','Accuracy'].reset_index()
                    ရခီးတွေ +=float(accuracy['Accuracy'])

                elif lex=='ရွာသား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရွာသား','Accuracy'].reset_index()
                    ရွာသား +=float(accuracy['Accuracy'])
                    
                elif lex=='လီးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးကြံ့ဖွတ်','Accuracy'].reset_index()
                    လီးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='လီးဆူး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးဆူး','Accuracy'].reset_index()
                    လီးဆူး +=float(accuracy['Accuracy'])
                    
                elif lex=='လူရိုင်း': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လူရိုင်း','Accuracy'].reset_index()
                    လူရိုင်း +=float(accuracy['Accuracy'])
                    
                elif lex=='လူသားစိတ္ ကင္းမဲ့' or lex=='လူသားစိတ်ကင်းမဲ့':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လူသားစိတ်ကင်းမဲ့','Accuracy'].reset_index()
                    လူသားစိတ်ကင်းမဲ့ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဝူဟန်':
                    accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်','Accuracy'].reset_index()
                    ဝူဟန် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဝူဟန်တရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်တရုတ်','Accuracy'].reset_index()
                    ဝူဟန်တရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='သတ်မတော်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သတ်မတော်','Accuracy'].reset_index()
                    သတ်မတော် +=float(accuracy['Accuracy'])
                    
                elif lex=='သုတ်ကြောင်မ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သုတ်ကြောင်မ','Accuracy'].reset_index()
                    သုတ်ကြောင်မ +=float(accuracy['Accuracy'])
                    
                elif lex=='သူခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူခိုး','Accuracy'].reset_index()
                    သူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်','Accuracy'].reset_index()
                    သူပုန် +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်မ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်မ','Accuracy'].reset_index()
                    သူပုန်မ +=float(accuracy['Accuracy'])
                    
                elif lex=='သူပုန်လော်ဘီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်လော်ဘီ','Accuracy'].reset_index()
                    သူပုန်လော်ဘီ +=float(accuracy['Accuracy'])
                    
                elif lex=='သောင်းကျမ်းသူ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သောင်းကျမ်းသူ','Accuracy'].reset_index()
                    သောင်းကျမ်းသူ +=float(accuracy['Accuracy'])
                    
                elif lex=='အကြမ်းဖက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်','Accuracy'].reset_index()
                    အကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex=='အကြမ်းဖက်ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်ကုလားတွေ','Accuracy'].reset_index()
                    အကြမ်းဖက်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='အစိမ်းရောင်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစိမ်းရောင်ခွေး','Accuracy'].reset_index()
                    အစိမ်းရောင်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='အစွန်းရောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်','Accuracy'].reset_index()
                    အစွန်းရောက် +=float(accuracy['Accuracy'])
                    
                elif lex=='အစွန်းရောက်ရခိုင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်ရခိုင်','Accuracy'].reset_index()
                    အစွန်းရောက်ရခိုင် +=float(accuracy['Accuracy'])
                    
                elif lex=='အဆိပ်သားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဆိပ်သားတွေ','Accuracy'].reset_index()
                    အဆိပ်သားတွေ +=float(accuracy['Accuracy'])
                
                elif lex=='အနီကြောင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အနီကြောင်','Accuracy'].reset_index()
                    အနီကြောင် +=float(accuracy['Accuracy'])
                    
                elif lex=='အပြုတ်တိုက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အပြုတ်တိုက်','Accuracy'].reset_index()
                    အပြုတ်တိုက် +=float(accuracy['Accuracy'])

                elif lex=='အဖျက်သမားaa':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဖျက်သမားaa','Accuracy'].reset_index()
                    အဖျက်သမားaa +=float(accuracy['Accuracy'])
                    
                elif lex=='အဘAA' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဘAA','Accuracy'].reset_index()
                    အဘAA +=float(accuracy['Accuracy'])
                    
                elif lex=='အမျိုးယုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်','Accuracy'].reset_index()
                    အမျိုးယုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='အမျိုးယုတ်ရှမ်း':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်ရှမ်း','Accuracy'].reset_index()
                    အမျိုးယုတ်ရှမ်း +=float(accuracy['Accuracy'])
                    
                elif lex=='အမြစ်ပြတ်ရှင်း':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမြစ်ပြတ်ရှင်း','Accuracy'].reset_index()
                    အမြစ်ပြတ်ရှင်း +=float(accuracy['Accuracy'])
                    
                elif lex=='အာနာရူးတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အာနာရူးတွေ','Accuracy'].reset_index()
                    အာနာရူးတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='အိမ်စောင့်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အိမ်စောင့်ခွေး','Accuracy'].reset_index()
                    အိမ်စောင့်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='အောက်တန်းကျ' or lex=='အောက်တန်းကြ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းကျ','Accuracy'].reset_index()
                    အောက်တန်းကျ +=float(accuracy['Accuracy'])
                    
                elif lex=='အောက်တန်းစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းစား','Accuracy'].reset_index()
                    အောက်တန်းစား +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်တွေလဒတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်တွေလဒတွေ','Accuracy'].reset_index()
                    ဖွတ်တွေလဒတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ေခွး' or lex=='ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေး','Accuracy'].reset_index()
                    ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='၇၈၆':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='၇၈၆','Accuracy'].reset_index()
                    string_786 +=float(accuracy['Accuracy'])
                    
                elif lex== 'AAသူပုန်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='AAသူပုန်','Accuracy'].reset_index()
                    AAသူပုန် +=float(accuracy['Accuracy'])
                    
                elif lex=='Thaiပြန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='Thaiပြန်','Accuracy'].reset_index()
                    Thaiပြန် +=float(accuracy['Accuracy'])
                    
                elif lex=='gwi': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='gwi','Accuracy'].reset_index()
                    gwi +=float(accuracy['Accuracy'])
                    
                elif lex=='ကမ္ဘာ့ကပ်ရောဂါကြီး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကမ္ဘာ့ကပ်ရောဂါကြီး','Accuracy'].reset_index()
                    ကမ္ဘာ့ကပ်ရောဂါကြီး +=float(accuracy['Accuracy'])
                    
                elif lex=='ကုလားပြည်နယ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားပြည်နယ်','Accuracy'].reset_index()
                    ကုလားပြည်နယ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကုလားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားတွေ','Accuracy'].reset_index()
                    ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ကျောင်းနွား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကျောင်းနွား','Accuracy'].reset_index()
                    ကျောင်းနွား +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်','Accuracy'].reset_index()
                    ကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်သခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သခိုး','Accuracy'].reset_index()
                    ကြံ့ဖွတ်သခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်သူခိုးကောင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သူခိုးကောင်','Accuracy'].reset_index()
                    ကြံ့ဖွတ်သူခိုးကောင် +=float(accuracy['Accuracy'])
                    
                elif lex=='ကြံ့ဖွတ်ပါတီ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်ပါတီ','Accuracy'].reset_index()
                    ကြံ့ဖွတ်ပါတီ +=float(accuracy['Accuracy'])
                    
                elif lex=='ခိုးဝင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခိုးဝင်','Accuracy'].reset_index()
                    ခိုးဝင် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးတပ်မတော်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတပ်မတော်','Accuracy'].reset_index()
                    ခွေးတပ်မတော် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးတရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတရုတ်','Accuracy'].reset_index()
                    ခွေးတရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသား','Accuracy'].reset_index()
                    ခွေးသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသူတောင်းစားခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားခွေး','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားခွေး +=float(accuracy['Accuracy'])
                    
                elif lex== 'ခွေးသူတောင်းစားမီဒီညာ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီညာ','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားမီဒီညာ +=float(accuracy['Accuracy'])
                
                elif lex=='ခွေးဦးနှောက်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဦးနှောက်','Accuracy'].reset_index()
                    ခွေးဦးနှောက် +=float(accuracy['Accuracy'])
                
                elif lex=='ခွေးဝဲစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဝဲစား','Accuracy'].reset_index()
                    ခွေးဝဲစား +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသတ်မတော်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသတ်မတော်','Accuracy'].reset_index()
                    ခွေးသတ်မတော် +=float(accuracy['Accuracy'])

                elif lex=='ငပွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငပွေး','Accuracy'].reset_index()
                    ငပွေး +=float(accuracy['Accuracy'])

                elif lex=='ငလူး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူး','Accuracy'].reset_index()
                    ငလူး +=float(accuracy['Accuracy'])
                    
                elif lex=='ငလူးပဲ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူးပဲ','Accuracy'].reset_index()
                    ငလူးပဲ +=float(accuracy['Accuracy'])
                
                elif lex=='ငှက်နီ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငှက်နီ','Accuracy'].reset_index()
                    ငှက်နီ +=float(accuracy['Accuracy'])
                    
                elif lex== 'စစ်သူခိုးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်သူခိုးကြံ့ဖွတ်','Accuracy'].reset_index()
                    စစ်သူခိုးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်အာဏာရှင်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်အာဏာရှင်','Accuracy'].reset_index()
                    စစ်အာဏာရှင် +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ခွေး','Accuracy'].reset_index()
                    စစ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='စစ်ဦးဘီလူး': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ဦးဘီလူး','Accuracy'].reset_index()
                    စစ်ဦးဘီလူး +=float(accuracy['Accuracy'])
                    
                elif lex=='စောက်တရုတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်တရုတ်','Accuracy'].reset_index()
                    စောက်တရုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='စောက်သုံးမကျအစိုးရ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်သုံးမကျအစိုးရ','Accuracy'].reset_index()
                    စောက်သုံးမကျအစိုးရ +=float(accuracy['Accuracy'])
                    
                elif lex=='စောင်ကုလား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောင်ကုလား','Accuracy'].reset_index()
                    စောင်ကုလား +=float(accuracy['Accuracy'])
                    
                elif lex=='တရုပ်စုပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုပ်စုပ်','Accuracy'].reset_index()
                    တရုပ်စုပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='တရုတ်ခွေး' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုတ်ခွေး','Accuracy'].reset_index()
                    တရုတ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='တောသား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တောသား','Accuracy'].reset_index()
                    တောသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ထန်းတောသားတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထန်းတောသားတွေ','Accuracy'].reset_index()
                    ထန်းတောသားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထမိန်ခြုံနဲ့ဘောမ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမိန်ခြုံနဲ့ဘောမ','Accuracy'].reset_index()
                    ထမိန်ခြုံနဲ့ဘောမ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထမီခြုံ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမီခြုံ','Accuracy'].reset_index()
                    ထမီခြုံ +=float(accuracy['Accuracy'])
                    
                elif lex=='ထောင်ထွက်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထောင်ထွက်','Accuracy'].reset_index()
                    ထောင်ထွက် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဒီမိုခွေးတွေ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒီမိုခွေးတွေ','Accuracy'].reset_index()
                    ဒီမိုခွေးတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဒေါ်လာစား': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒေါ်လာစား','Accuracy'].reset_index()
                    ဒေါ်လာစား +=float(accuracy['Accuracy'])
                
                elif lex== 'နပီဗမာစစ်\u200b\u200bခွေးတပ်' or lex=='နပီဗမာစစ်ခွေးတပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နပီဗမာစစ်ခွေးတပ်','Accuracy'].reset_index()
                    နပီဗမာစစ်ခွေးတပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='နီပိန်း' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပိန်း','Accuracy'].reset_index()
                    နီပိန်း +=float(accuracy['Accuracy'])
                    
                elif lex=='နီပေါ': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပေါ','Accuracy'].reset_index()
                    နီပေါ +=float(accuracy['Accuracy'])
                    
                elif lex=='နွားကျောင်းသား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နွားကျောင်းသား','Accuracy'].reset_index()
                    နွားကျောင်းသား +=float(accuracy['Accuracy'])
                    
                elif lex=='ပလောင်တွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပလောင်တွေ','Accuracy'].reset_index()
                    ပလောင်တွေ +=float(accuracy['Accuracy'])

                elif lex=='ပြည်ခိုင်ဖြိုးသူခိုး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ခိုင်ဖြိုးသူခိုး','Accuracy'].reset_index()
                    ပြည်ခိုင်ဖြိုးသူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ပြည်ထိုင်ခိုး' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ထိုင်ခိုး','Accuracy'].reset_index()
                    ပြည်ထိုင်ခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖင်ကုံး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ကုံး','Accuracy'].reset_index()
                    ဖင်ကုံး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖင်ယား' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ယား','Accuracy'].reset_index()
                    ဖင်ယား +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖာသေမစု': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖာသေမစု','Accuracy'].reset_index()
                    ဖာသေမစု +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်သူခိုး': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်သူခိုး','Accuracy'].reset_index()
                    ဖွတ်သူခိုး +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်','Accuracy'].reset_index()
                    ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဖွတ်ပါတီ' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်ပါတီ','Accuracy'].reset_index()
                    ဖွတ်ပါတီ +=float(accuracy['Accuracy'])

                elif lex=='ဗမာတွေ' or lex=='ဗမာ' or lex=='ဗမာေတွ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာတွေ','Accuracy'].reset_index()
                    ဗမာတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာစစ်အာဏာရှင်အုပ်စု': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်အာဏာရှင်အုပ်စု','Accuracy'].reset_index()
                    ဗမာစစ်အာဏာရှင်အုပ်စု +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာသောင်းကြမ်းသူအဖွဲ့':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာသောင်းကြမ်းသူအဖွဲ့','Accuracy'].reset_index()
                    ဗမာသောင်းကြမ်းသူအဖွဲ့ +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာအစိုးရစစ်တပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစိုးရစစ်တပ်','Accuracy'].reset_index()
                    ဗမာအစိုးရစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗမာအစောရနှင့်ဗမာစစ်တပ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစောရနှင့်ဗမာစစ်တပ်','Accuracy'].reset_index()
                    ဗမာအစောရနှင့်ဗမာစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာစစ်တပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်တပ်','Accuracy'].reset_index()
                    ဗမာစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex=='ဗမာအကြမ်းဖက်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအကြမ်းဖက်','Accuracy'].reset_index()
                    ဗမာအကြမ်းဖက် +=float(accuracy['Accuracy'])
                    
                elif lex== 'ဗလီတွေ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗလီတွေ','Accuracy'].reset_index()
                    ဗလီတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဘင်ဂါလီ' or lex=='ဘင်္ဂါလီ' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘင်ဂါလီ','Accuracy'].reset_index()
                    ဘင်ဂါလီ +=float(accuracy['Accuracy'])
                    
                elif lex=='ဘိန်းစား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘိန်းစား','Accuracy'].reset_index()
                    ဘိန်းစား +=float(accuracy['Accuracy'])
                    
                elif lex== 'မအေလိုးကြံ့ဖွတ်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မအေလိုးကြံ့ဖွတ်','Accuracy'].reset_index()
                    မအေလိုးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်','Accuracy'].reset_index()
                    မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက် +=float(accuracy['Accuracy'])
                    
                elif lex== 'မာမွတ်စူလတန်':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာမွတ်စူလတန်','Accuracy'].reset_index()
                    မာမွတ်စူလတန် +=float(accuracy['Accuracy'])
                    
                elif lex=='မုဒိန်းစစ်တပ်': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မုဒိန်းစစ်တပ်','Accuracy'].reset_index()
                    မုဒိန်းစစ်တပ် +=float(accuracy['Accuracy'])
                    
                elif lex== 'မူစလင်ကုလား' : 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူစလင်ကုလား','Accuracy'].reset_index()
                    မူစလင်ကုလား +=float(accuracy['Accuracy'])
                    
                elif lex=='မူဆလင်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်','Accuracy'].reset_index()
                    မူဆလင် +=float(accuracy['Accuracy'])
                    
                elif lex=='မူဆလင်ကုလားတွေ': 
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်ကုလားတွေ','Accuracy'].reset_index()
                    မူဆလင်ကုလားတွေ +=float(accuracy['Accuracy'])
                    
                elif lex=='မျိုးဖြုတ်' :
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မျိုးဖြုတ်','Accuracy'].reset_index()
                    မျိုးဖြုတ် +=float(accuracy['Accuracy'])
                    
                elif lex=='တစ်မတ်သား':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တစ်မတ်သား','Accuracy'].reset_index()
                    တစ်မတ်သား +=float(accuracy['Accuracy'])
                    
                elif lex=='အရိုးကိုက်ဖွတ်ခွေး':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အရိုးကိုက်ဖွတ်ခွေး','Accuracy'].reset_index()
                    အရိုးကိုက်ဖွတ်ခွေး +=float(accuracy['Accuracy'])
                    
                elif lex=='ခွေးသူတောင်းစားမီဒီယာ':
                    accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီယာ','Accuracy'].reset_index()
                    ခွေးသူတောင်းစားမီဒီယာ +=float(accuracy['Accuracy'])
                    

            weight_value = မွတ်ကုလား+မြို့သား+မြေသြဇာ+မွတ်+မွတ်ကုလားတွေ+မွတ်ဒေါင်း+မွတ်ဒေါင်းခွေ+မွတ်ပါတီ+ရခိုင်အကြမ်းဖက်သမား+ရခိး+ရခီးတွေ+ရွာသား+လီးကြံ့ဖွတ်+လီးဆူး+လူရိုင်း+လူသားစိတ္ကင္းမဲ့+ဝူဟန်+ဝူဟန်တရုတ်+သတ်မတော်+သုတ်ကြောင်မ+သူခိုး+သူပုန်+သူပုန်မ+သူပုန်လော်ဘီ+သောင်းကျမ်းသူ+အကြမ်းဖက်+အကြမ်းဖက်ကုလားတွေ+အစိမ်းရောင်ခွေး+အစွန်းရောက်+အစွန်းရောက်ရခိုင်+အဆိပ်သားတွေ+အနီကြောင်+အပြုတ်တိုက်+အဖျက်သမားaa+အဘAA+အမျိုးယုတ်+အမျိုးယုတ်ရှမ်း+အမြစ်ပြတ်ရှင်း+အာနာရူးတွေ+အာနာရူးတွေ+အိမ်စောင့်ခွေး+အောက်တန်းကျ+အောက်တန်းစား+ဖွတ်တွေလဒတွေ+ခွေး+string_786+AAသူပုန်+Thaiပြန်+gwi+ကမ္ဘာ့ကပ်ရောဂါကြီး+ကုလားပြည်နယ်+ကုလားတွေ+ကျောင်းနွား+ကြံ့ဖွတ်+ကြံ့ဖွတ်သခိုး+ကြံ့ဖွတ်သူခိုးကောင်+ကြံ့ဖွတ်ပါတီ+ခိုးဝင်+ခွေးတပ်မတော်+ခွေးတရုတ်+ခွေးသား+ခွေးသူတောင်းစားခွေး+ခွေးသူတောင်းစားမီဒီညာ+ခွေးဦးနှောက်+ခွေးဝဲစား+ခွေးသတ်မတော်+ခွေးသား+ငပွေး+ငလူး+ငလူးပဲ+ငှက်နီ+စစ်သူခိုးကြံ့ဖွတ်+စစ်အာဏာရှင်+စစ်ခွေး+စစ်ဦးဘီလူး+စောက်တရုတ်+စောက်သုံးမကျအစိုးရ+စောင်ကုလား+တရုပ်စုပ်+တရုတ်ခွေး+တောသား+ထန်းတောသားတွေ+ထမိန်ခြုံနဲ့ဘောမ+ထမီခြုံ+ထောင်ထွက်+ဒီမိုခွေးတွေ+ဒေါ်လာစား+နပီဗမာစစ်ခွေးတပ်+နီပိန်း+နီပေါ+နွားကျောင်းသား+ပလောင်တွေ+ပြည်ခိုင်ဖြိုးသူခိုး+ပြည်ထိုင်ခိုး+ဖင်ကုံး+ဖင်ယား+ဖာသေမစု+ဖွတ်သူခိုး+ဖွတ်+ဖွတ်ပါတီ+ဗမာတွေ+ဗမာစစ်အာဏာရှင်အုပ်စု+ဗမာသောင်းကြမ်းသူအဖွဲ့+ဗမာအစိုးရစစ်တပ်+ဗမာအစောရနှင့်ဗမာစစ်တပ်+ဗမာစစ်တပ်+ဗမာအကြမ်းဖက်+ဗလီတွေ+ဘင်ဂါလီ+ဘိန်းစား+မအေလိုးကြံ့ဖွတ်+မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်+မာမွတ်စူလတန်+မုဒိန်းစစ်တပ်+မူစလင်ကုလား+မူဆလင်+မူဆလင်ကုလားတွေ+မျိုးဖြုတ်+တစ်မတ်သား+အရိုးကိုက်ဖွတ်ခွေး+ခွေးသူတောင်းစားမီဒီယာ
            word_weight.append([str(LexFound),MsgUniSeg,NewHSWordInSentence,weight_value])

        elif (lexicon_regex.search(str(LexFound))==None) and (newword_regex.search(str(NewHSWordInSentence))==None):
            lex=LexFound
            if isinstance(lex,str)==False:pass
            
            else: 
                if isinstance(NewHSWordInSentence,str)==False:
                    n_weight=[lex]

                else:
                    new=NewHSWordInSentence.replace(" ", "")
                    lex=lex+','+new
                    n_weight = lex.split(',')
                for lex in n_weight:
                    if lex=='မွတ်ကုလား':
                        accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလား','Accuracy'].reset_index()
                        မွတ်ကုလား +=float(accuracy['Accuracy'])
                    elif lex=='မြို့သား':
                        accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြို့သား','Accuracy'].reset_index()
                        မြို့သား +=float(accuracy['Accuracy'])

                    elif lex=='မြေသြဇာ':
                        accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မြေသြဇာ','Accuracy'].reset_index()
                        မြေသြဇာ +=float(accuracy['Accuracy'])

                    elif lex=='မွတ်':
                        accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်','Accuracy'].reset_index()
                        မွတ် +=float(accuracy['Accuracy'])

                    elif lex=='မွတ်ကုလားတွေ':
                        accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ကုလားတွေ','Accuracy'].reset_index()
                        မွတ်ကုလားတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='မွတ်ဒေါင်း':
                        accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်း','Accuracy'].reset_index()
                        မွတ်ဒေါင်း +=float(accuracy['Accuracy'])
                            
                    elif lex=='မွတ်ဒေါင်းခွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ဒေါင်းခွေ','Accuracy'].reset_index()
                        မွတ်ဒေါင်းခွေ +=float(accuracy['Accuracy'])

                    elif lex=='မွတ်ပါတီ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မွတ်ပါတီ','Accuracy'].reset_index()
                        မွတ်ပါတီ +=float(accuracy['Accuracy'])

                    elif lex=='ရခိုင်အကြမ်းဖက်သမား':
                        accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အကြမ်းဖက်သမား','Accuracy'].reset_index()
                        ရခိုင်အကြမ်းဖက်သမား +=float(accuracy['Accuracy'])
                        
                    elif lex=='ရခိး' or lex=='ရခီး' or lex=='ရခီး' or lex=='ရခွီး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိး','Accuracy'].reset_index()
                        ရခိး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ရခိုင်တပ်တော်AA':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်တပ်တော်AA','Accuracy'].reset_index()
                        ရခိုင်တပ်တော်AA +=float(accuracy['Accuracy'])
                        
                    elif lex=='ရခိုင်နဲ့မပွေး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်နဲ့မပွေး','Accuracy'].reset_index()
                        ရခိုင်နဲ့မပွေး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ရခိုင်သူပုန်aaအကြမ်းဖက်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်သူပုန်aaအကြမ်းဖက်','Accuracy'].reset_index()
                        ရခိုင်သူပုန်aaအကြမ်းဖက် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ရခိုင်အစွန်းရောက်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်အစွန်းရောက်','Accuracy'].reset_index()
                        ရခိုင်အစွန်းရောက် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ရခိုင်ကုလားတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခိုင်ကုလားတွေ','Accuracy'].reset_index()
                        ရခိုင်ကုလားတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ရခီးတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရခီးတွေ','Accuracy'].reset_index()
                        ရခီးတွေ +=float(accuracy['Accuracy'])

                    elif lex=='ရွာသား':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ရွာသား','Accuracy'].reset_index()
                        ရွာသား +=float(accuracy['Accuracy'])
                        
                    elif lex=='လီးကြံ့ဖွတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးကြံ့ဖွတ်','Accuracy'].reset_index()
                        လီးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='လီးဆူး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လီးဆူး','Accuracy'].reset_index()
                        လီးဆူး +=float(accuracy['Accuracy'])
                        
                    elif lex=='လူရိုင်း': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လူရိုင်း','Accuracy'].reset_index()
                        လူရိုင်း +=float(accuracy['Accuracy'])
                        
                    elif lex=='လူသားစိတ္ ကင္းမဲ့' or lex=='လူသားစိတ်ကင်းမဲ့':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='လူသားစိတ္ကင္းမဲ့','Accuracy'].reset_index()
                        လူသားစိတ်ကင်းမဲ့ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဝူဟန်':
                        accuracy =lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်','Accuracy'].reset_index()
                        ဝူဟန် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဝူဟန်တရုတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဝူဟန်တရုတ်','Accuracy'].reset_index()
                        ဝူဟန်တရုတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='သတ်မတော်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သတ်မတော်','Accuracy'].reset_index()
                        သတ်မတော် +=float(accuracy['Accuracy'])
                        
                    elif lex=='သုတ်ကြောင်မ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သုတ်ကြောင်မ','Accuracy'].reset_index()
                        သုတ်ကြောင်မ +=float(accuracy['Accuracy'])
                        
                    elif lex=='သူခိုး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူခိုး','Accuracy'].reset_index()
                        သူခိုး +=float(accuracy['Accuracy'])
                        
                    elif lex=='သူပုန်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်','Accuracy'].reset_index()
                        သူပုန် +=float(accuracy['Accuracy'])
                        
                    elif lex=='သူပုန်မ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်မ','Accuracy'].reset_index()
                        သူပုန်မ +=float(accuracy['Accuracy'])
                        
                    elif lex=='သူပုန်လော်ဘီ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သူပုန်လော်ဘီ','Accuracy'].reset_index()
                        သူပုန်လော်ဘီ +=float(accuracy['Accuracy'])
                        
                    elif lex=='သောင်းကျမ်းသူ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='သောင်းကျမ်းသူ','Accuracy'].reset_index()
                        သောင်းကျမ်းသူ +=float(accuracy['Accuracy'])
                        
                    elif lex=='အကြမ်းဖက်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်','Accuracy'].reset_index()
                        အကြမ်းဖက် +=float(accuracy['Accuracy'])
                        
                    elif lex=='အကြမ်းဖက်ကုလားတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အကြမ်းဖက်ကုလားတွေ','Accuracy'].reset_index()
                        အကြမ်းဖက်ကုလားတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='အစိမ်းရောင်ခွေး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစိမ်းရောင်ခွေး','Accuracy'].reset_index()
                        အစိမ်းရောင်ခွေး +=float(accuracy['Accuracy'])
                        
                    elif lex=='အစွန်းရောက်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်','Accuracy'].reset_index()
                        အစွန်းရောက် +=float(accuracy['Accuracy'])
                        
                    elif lex=='အစွန်းရောက်ရခိုင်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အစွန်းရောက်ရခိုင်','Accuracy'].reset_index()
                        အစွန်းရောက်ရခိုင် +=float(accuracy['Accuracy'])
                        
                    elif lex=='အဆိပ်သားတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဆိပ်သားတွေ','Accuracy'].reset_index()
                        အဆိပ်သားတွေ +=float(accuracy['Accuracy'])
                    
                    elif lex=='အနီကြောင်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အနီကြောင်','Accuracy'].reset_index()
                        အနီကြောင် +=float(accuracy['Accuracy'])
                        
                    elif lex=='အပြုတ်တိုက်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အပြုတ်တိုက်','Accuracy'].reset_index()
                        အပြုတ်တိုက် +=float(accuracy['Accuracy'])

                    elif lex=='အဖျက်သမားaa':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဖျက်သမားaa','Accuracy'].reset_index()
                        အဖျက်သမားaa +=float(accuracy['Accuracy'])
                        
                    elif lex=='အဘAA' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အဘAA','Accuracy'].reset_index()
                        အဘAA +=float(accuracy['Accuracy'])
                        
                    elif lex=='အမျိုးယုတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်','Accuracy'].reset_index()
                        အမျိုးယုတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='အမျိုးယုတ်ရှမ်း':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမျိုးယုတ်ရှမ်း','Accuracy'].reset_index()
                        အမျိုးယုတ်ရှမ်း +=float(accuracy['Accuracy'])
                        
                    elif lex=='အမြစ်ပြတ်ရှင်း':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အမြစ်ပြတ်ရှင်း','Accuracy'].reset_index()
                        အမြစ်ပြတ်ရှင်း +=float(accuracy['Accuracy'])
                        
                    elif lex=='အာနာရူးတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အာနာရူးတွေ','Accuracy'].reset_index()
                        အာနာရူးတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='အိမ်စောင့်ခွေး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အိမ်စောင့်ခွေး','Accuracy'].reset_index()
                        အိမ်စောင့်ခွေး +=float(accuracy['Accuracy'])
                        
                    elif lex=='အောက်တန်းကျ' or lex=='အောက်တန်းကြ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းကျ','Accuracy'].reset_index()
                        အောက်တန်းကျ +=float(accuracy['Accuracy'])
                        
                    elif lex=='အောက်တန်းစား':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အောက်တန်းစား','Accuracy'].reset_index()
                        အောက်တန်းစား +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဖွတ်တွေလဒတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်တွေလဒတွေ','Accuracy'].reset_index()
                        ဖွတ်တွေလဒတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ေခွး' or lex=='ခွေး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေး','Accuracy'].reset_index()
                        ခွေး +=float(accuracy['Accuracy'])
                        
                    elif lex=='၇၈၆':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='၇၈၆','Accuracy'].reset_index()
                        string_786 +=float(accuracy['Accuracy'])
                        
                    elif lex== 'AAသူပုန်': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='AAသူပုန်','Accuracy'].reset_index()
                        AAသူပုန် +=float(accuracy['Accuracy'])
                        
                    elif lex=='Thaiပြန်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='Thaiပြန်','Accuracy'].reset_index()
                        Thaiပြန် +=float(accuracy['Accuracy'])
                        
                    elif lex=='gwi': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='gwi','Accuracy'].reset_index()
                        gwi +=float(accuracy['Accuracy'])
                        
                    elif lex=='ကမ္ဘာ့ကပ်ရောဂါကြီး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကမ္ဘာ့ကပ်ရောဂါကြီး','Accuracy'].reset_index()
                        ကမ္ဘာ့ကပ်ရောဂါကြီး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ကုလားပြည်နယ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားပြည်နယ်','Accuracy'].reset_index()
                        ကုလားပြည်နယ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ကုလားတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကုလားတွေ','Accuracy'].reset_index()
                        ကုလားတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ကျောင်းနွား': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကျောင်းနွား','Accuracy'].reset_index()
                        ကျောင်းနွား +=float(accuracy['Accuracy'])
                        
                    elif lex=='ကြံ့ဖွတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်','Accuracy'].reset_index()
                        ကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ကြံ့ဖွတ်သခိုး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သခိုး','Accuracy'].reset_index()
                        ကြံ့ဖွတ်သခိုး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ကြံ့ဖွတ်သူခိုးကောင်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်သူခိုးကောင်','Accuracy'].reset_index()
                        ကြံ့ဖွတ်သူခိုးကောင် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ကြံ့ဖွတ်ပါတီ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ကြံ့ဖွတ်ပါတီ','Accuracy'].reset_index()
                        ကြံ့ဖွတ်ပါတီ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ခိုးဝင်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခိုးဝင်','Accuracy'].reset_index()
                        ခိုးဝင် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ခွေးတပ်မတော်' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတပ်မတော်','Accuracy'].reset_index()
                        ခွေးတပ်မတော် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ခွေးတရုတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးတရုတ်','Accuracy'].reset_index()
                        ခွေးတရုတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ခွေးသား':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသား','Accuracy'].reset_index()
                        ခွေးသား +=float(accuracy['Accuracy'])
                        
                    elif lex=='ခွေးသူတောင်းစားခွေး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားခွေး','Accuracy'].reset_index()
                        ခွေးသူတောင်းစားခွေး +=float(accuracy['Accuracy'])
                        
                    elif lex== 'ခွေးသူတောင်းစားမီဒီညာ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီညာ','Accuracy'].reset_index()
                        ခွေးသူတောင်းစားမီဒီညာ +=float(accuracy['Accuracy'])
                    
                    elif lex=='ခွေးဦးနှောက်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဦးနှောက်','Accuracy'].reset_index()
                        ခွေးဦးနှောက် +=float(accuracy['Accuracy'])
                    
                    elif lex=='ခွေးဝဲစား':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးဝဲစား','Accuracy'].reset_index()
                        ခွေးဝဲစား +=float(accuracy['Accuracy'])
                        
                    elif lex=='ခွေးသတ်မတော်' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသတ်မတော်','Accuracy'].reset_index()
                        ခွေးသတ်မတော် +=float(accuracy['Accuracy'])

                    elif lex=='ငပွေး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငပွေး','Accuracy'].reset_index()
                        ငပွေး +=float(accuracy['Accuracy'])

                    elif lex=='ငလူး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူး','Accuracy'].reset_index()
                        ငလူး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ငလူးပဲ' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငလူးပဲ','Accuracy'].reset_index()
                        ငလူးပဲ +=float(accuracy['Accuracy'])
                    
                    elif lex=='ငှက်နီ' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ငှက်နီ','Accuracy'].reset_index()
                        ငှက်နီ +=float(accuracy['Accuracy'])
                        
                    elif lex== 'စစ်သူခိုးကြံ့ဖွတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်သူခိုးကြံ့ဖွတ်','Accuracy'].reset_index()
                        စစ်သူခိုးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='စစ်အာဏာရှင်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်အာဏာရှင်','Accuracy'].reset_index()
                        စစ်အာဏာရှင် +=float(accuracy['Accuracy'])
                        
                    elif lex=='စစ်ခွေး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ခွေး','Accuracy'].reset_index()
                        စစ်ခွေး +=float(accuracy['Accuracy'])
                        
                    elif lex=='စစ်ဦးဘီလူး': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စစ်ဦးဘီလူး','Accuracy'].reset_index()
                        စစ်ဦးဘီလူး +=float(accuracy['Accuracy'])
                        
                    elif lex=='စောက်တရုတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်တရုတ်','Accuracy'].reset_index()
                        စောက်တရုတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='စောက်သုံးမကျအစိုးရ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောက်သုံးမကျအစိုးရ','Accuracy'].reset_index()
                        စောက်သုံးမကျအစိုးရ +=float(accuracy['Accuracy'])
                        
                    elif lex=='စောင်ကုလား' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='စောင်ကုလား','Accuracy'].reset_index()
                        စောင်ကုလား +=float(accuracy['Accuracy'])
                        
                    elif lex=='တရုပ်စုပ်': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုပ်စုပ်','Accuracy'].reset_index()
                        တရုပ်စုပ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='တရုတ်ခွေး' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တရုတ်ခွေး','Accuracy'].reset_index()
                        တရုတ်ခွေး +=float(accuracy['Accuracy'])
                        
                    elif lex=='တောသား': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တောသား','Accuracy'].reset_index()
                        တောသား +=float(accuracy['Accuracy'])
                        
                    elif lex=='ထန်းတောသားတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထန်းတောသားတွေ','Accuracy'].reset_index()
                        ထန်းတောသားတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ထမိန်ခြုံနဲ့ဘောမ' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမိန်ခြုံနဲ့ဘောမ','Accuracy'].reset_index()
                        ထမိန်ခြုံနဲ့ဘောမ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ထမီခြုံ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထမီခြုံ','Accuracy'].reset_index()
                        ထမီခြုံ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ထောင်ထွက်': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ထောင်ထွက်','Accuracy'].reset_index()
                        ထောင်ထွက် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဒီမိုခွေးတွေ' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒီမိုခွေးတွေ','Accuracy'].reset_index()
                        ဒီမိုခွေးတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဒေါ်လာစား': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဒေါ်လာစား','Accuracy'].reset_index()
                        ဒေါ်လာစား +=float(accuracy['Accuracy'])
                    
                    elif lex== 'နပီဗမာစစ်\u200b\u200bခွေးတပ်' or lex=='နပီဗမာစစ်ခွေးတပ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နပီဗမာစစ်ခွေးတပ်','Accuracy'].reset_index()
                        နပီဗမာစစ်ခွေးတပ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='နီပိန်း' : 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပိန်း','Accuracy'].reset_index()
                        နီပိန်း +=float(accuracy['Accuracy'])
                        
                    elif lex=='နီပေါ': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နီပေါ','Accuracy'].reset_index()
                        နီပေါ +=float(accuracy['Accuracy'])
                        
                    elif lex=='နွားကျောင်းသား' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='နွားကျောင်းသား','Accuracy'].reset_index()
                        နွားကျောင်းသား +=float(accuracy['Accuracy'])
                        
                    elif lex=='ပလောင်တွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပလောင်တွေ','Accuracy'].reset_index()
                        ပလောင်တွေ +=float(accuracy['Accuracy'])

                    elif lex=='ပြည်ခိုင်ဖြိုးသူခိုး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ခိုင်ဖြိုးသူခိုး','Accuracy'].reset_index()
                        ပြည်ခိုင်ဖြိုးသူခိုး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ပြည်ထိုင်ခိုး' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ပြည်ထိုင်ခိုး','Accuracy'].reset_index()
                        ပြည်ထိုင်ခိုး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဖင်ကုံး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ကုံး','Accuracy'].reset_index()
                        ဖင်ကုံး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဖင်ယား' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖင်ယား','Accuracy'].reset_index()
                        ဖင်ယား +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဖာသေမစု': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖာသေမစု','Accuracy'].reset_index()
                        ဖာသေမစု +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဖွတ်သူခိုး': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်သူခိုး','Accuracy'].reset_index()
                        ဖွတ်သူခိုး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဖွတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်','Accuracy'].reset_index()
                        ဖွတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဖွတ်ပါတီ' : 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဖွတ်ပါတီ','Accuracy'].reset_index()
                        ဖွတ်ပါတီ +=float(accuracy['Accuracy'])

                    elif lex=='ဗမာတွေ' or lex=='ဗမာ' or lex=='ဗမာေတွ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာတွေ','Accuracy'].reset_index()
                        ဗမာတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဗမာစစ်အာဏာရှင်အုပ်စု': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်အာဏာရှင်အုပ်စု','Accuracy'].reset_index()
                        ဗမာစစ်အာဏာရှင်အုပ်စု +=float(accuracy['Accuracy'])
                        
                    elif lex== 'ဗမာသောင်းကြမ်းသူအဖွဲ့':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာသောင်းကြမ်းသူအဖွဲ့','Accuracy'].reset_index()
                        ဗမာသောင်းကြမ်းသူအဖွဲ့ +=float(accuracy['Accuracy'])
                        
                    elif lex== 'ဗမာအစိုးရစစ်တပ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစိုးရစစ်တပ်','Accuracy'].reset_index()
                        ဗမာအစိုးရစစ်တပ် +=float(accuracy['Accuracy'])
                        
                    elif lex== 'ဗမာအစောရနှင့်ဗမာစစ်တပ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအစောရနှင့်ဗမာစစ်တပ်','Accuracy'].reset_index()
                        ဗမာအစောရနှင့်ဗမာစစ်တပ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဗမာစစ်တပ်': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာစစ်တပ်','Accuracy'].reset_index()
                        ဗမာစစ်တပ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဗမာအကြမ်းဖက်' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗမာအကြမ်းဖက်','Accuracy'].reset_index()
                        ဗမာအကြမ်းဖက် +=float(accuracy['Accuracy'])
                        
                    elif lex== 'ဗလီတွေ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဗလီတွေ','Accuracy'].reset_index()
                        ဗလီတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဘင်ဂါလီ' or lex=='ဘင်္ဂါလီ' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘင်ဂါလီ','Accuracy'].reset_index()
                        ဘင်ဂါလီ +=float(accuracy['Accuracy'])
                        
                    elif lex=='ဘိန်းစား':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ဘိန်းစား','Accuracy'].reset_index()
                        ဘိန်းစား +=float(accuracy['Accuracy'])
                        
                    elif lex== 'မအေလိုးကြံ့ဖွတ်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မအေလိုးကြံ့ဖွတ်','Accuracy'].reset_index()
                        မအေလိုးကြံ့ဖွတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်','Accuracy'].reset_index()
                        မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက် +=float(accuracy['Accuracy'])
                        
                    elif lex== 'မာမွတ်စူလတန်':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မာမွတ်စူလတန်','Accuracy'].reset_index()
                        မာမွတ်စူလတန် +=float(accuracy['Accuracy'])
                        
                    elif lex=='မုဒိန်းစစ်တပ်': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မုဒိန်းစစ်တပ်','Accuracy'].reset_index()
                        မုဒိန်းစစ်တပ် +=float(accuracy['Accuracy'])
                        
                    elif lex== 'မူစလင်ကုလား' : 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူစလင်ကုလား','Accuracy'].reset_index()
                        မူစလင်ကုလား +=float(accuracy['Accuracy'])
                        
                    elif lex=='မူဆလင်' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်','Accuracy'].reset_index()
                        မူဆလင် +=float(accuracy['Accuracy'])
                        
                    elif lex=='မူဆလင်ကုလားတွေ': 
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မူဆလင်ကုလားတွေ','Accuracy'].reset_index()
                        မူဆလင်ကုလားတွေ +=float(accuracy['Accuracy'])
                        
                    elif lex=='မျိုးဖြုတ်' :
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='မျိုးဖြုတ်','Accuracy'].reset_index()
                        မျိုးဖြုတ် +=float(accuracy['Accuracy'])
                        
                    elif lex=='တစ်မတ်သား':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='တစ်မတ်သား','Accuracy'].reset_index()
                        တစ်မတ်သား +=float(accuracy['Accuracy'])
                        
                    elif lex=='အရိုးကိုက်ဖွတ်ခွေး':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='အရိုးကိုက်ဖွတ်ခွေး','Accuracy'].reset_index()
                        အရိုးကိုက်ဖွတ်ခွေး +=float(accuracy['Accuracy'])
                        
                    elif lex=='ခွေးသူတောင်းစားမီဒီယာ':
                        accuracy=lexicon_pd.loc[lexicon_pd['Lexicon']=='ခွေးသူတောင်းစားမီဒီယာ','Accuracy'].reset_index()
                        ခွေးသူတောင်းစားမီဒီယာ +=float(accuracy['Accuracy'])
                    
                            
                weight_value = မွတ်ကုလား+မြို့သား+မြေသြဇာ+မွတ်+မွတ်ကုလားတွေ+မွတ်ဒေါင်း+မွတ်ဒေါင်းခွေ+မွတ်ပါတီ+ရခိုင်အကြမ်းဖက်သမား+ရခိး+ရခီးတွေ+ရွာသား+လီးကြံ့ဖွတ်+လီးဆူး+လူရိုင်း+လူသားစိတ္ကင္းမဲ့+ဝူဟန်+ဝူဟန်တရုတ်+သတ်မတော်+သုတ်ကြောင်မ+သူခိုး+သူပုန်+သူပုန်မ+သူပုန်လော်ဘီ+သောင်းကျမ်းသူ+အကြမ်းဖက်+အကြမ်းဖက်ကုလားတွေ+အစိမ်းရောင်ခွေး+အစွန်းရောက်+အစွန်းရောက်ရခိုင်+အဆိပ်သားတွေ+အနီကြောင်+အပြုတ်တိုက်+အဖျက်သမားaa+အဘAA+အမျိုးယုတ်+အမျိုးယုတ်ရှမ်း+အမြစ်ပြတ်ရှင်း+အာနာရူးတွေ+အာနာရူးတွေ+အိမ်စောင့်ခွေး+အောက်တန်းကျ+အောက်တန်းစား+ဖွတ်တွေလဒတွေ+ခွေး+string_786+AAသူပုန်+Thaiပြန်+gwi+ကမ္ဘာ့ကပ်ရောဂါကြီး+ကုလားပြည်နယ်+ကုလားတွေ+ကျောင်းနွား+ကြံ့ဖွတ်+ကြံ့ဖွတ်သခိုး+ကြံ့ဖွတ်သူခိုးကောင်+ကြံ့ဖွတ်ပါတီ+ခိုးဝင်+ခွေးတပ်မတော်+ခွေးတရုတ်+ခွေးသား+ခွေးသူတောင်းစားခွေး+ခွေးသူတောင်းစားမီဒီညာ+ခွေးဦးနှောက်+ခွေးဝဲစား+ခွေးသတ်မတော်+ငပွေး+ငလူး+ငလူးပဲ+ငှက်နီ+စစ်သူခိုးကြံ့ဖွတ်+စစ်အာဏာရှင်+စစ်ခွေး+စစ်ဦးဘီလူး+စောက်တရုတ်+စောက်သုံးမကျအစိုးရ+စောင်ကုလား+တရုပ်စုပ်+တရုတ်ခွေး+တောသား+ထန်းတောသားတွေ+ထမိန်ခြုံနဲ့ဘောမ+ထမီခြုံ+ထောင်ထွက်+ဒီမိုခွေးတွေ+ဒေါ်လာစား+နပီဗမာစစ်ခွေးတပ်+နီပိန်း+နီပေါ+နွားကျောင်းသား+ပလောင်တွေ+ပြည်ခိုင်ဖြိုးသူခိုး+ပြည်ထိုင်ခိုး+ဖင်ကုံး+ဖင်ယား+ဖာသေမစု+ဖွတ်သူခိုး+ဖွတ်+ဖွတ်ပါတီ+ဗမာတွေ+ဗမာစစ်အာဏာရှင်အုပ်စု+ဗမာသောင်းကြမ်းသူအဖွဲ့+ဗမာအစိုးရစစ်တပ်+ဗမာအစောရနှင့်ဗမာစစ်တပ်+ဗမာစစ်တပ်+ဗမာအကြမ်းဖက်+ဗလီတွေ+ဘင်ဂါလီ+ဘိန်းစား+မအေလိုးကြံ့ဖွတ်+မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်+မာမွတ်စူလတန်+မုဒိန်းစစ်တပ်+မူစလင်ကုလား+မူဆလင်+မူဆလင်ကုလားတွေ+မျိုးဖြုတ်+တစ်မတ်သား+အရိုးကိုက်ဖွတ်ခွေး+ခွေးသူတောင်းစားမီဒီယာ
                word_weight.append([str(LexFound),MsgUniSeg,NewHSWordInSentence,weight_value])
    return word_weight


