import pandas as pd
import numpy as np
import re
import json 
import gspread
from glob import glob 
import os 
from oauth2client.service_account import ServiceAccountCredentials



AAသူပုန်_zero=ကုလားတွေ_zero=ကျောင်းနွား_zero=ကြံ့ဖွတ်_zero=ကြံ့ဖွတ်ပါတီ_zero=ခိုးဝင်_zero=ခွေးတပ်မတော်_zero=ခွေးတရုတ်_zero=ခွေးဝဲစား_zero=ခွေးသတ်မတော်_zero=ခွေးသား_zero=ခွေးဦးနှောက်_zero=ငလူး_zero=ငှက်နီ_zero=စစ်ခွေး_zero=စစ်အာဏာရှင်_zero=စောက်တရုတ်_zero=တစ်မတ်သား_zero=တရုတ်ခွေး_zero=တောသား_zero=ထမီခြုံ_zero=ထောင်ထွက်_zero=ဒီမိုခွေးတွေ_zero=ဒေါ်လာစား_zero=နီပိန်း_zero=နီပေါ_zero=ပြည်ထိုင်ခိုး_zero=ဖင်ယား_zero=ဖွတ်_zero=ဖွတ်ပါတီ_zero=ဖွတ်သူခိုး_zero=ဗမာသောင်းကြမ်းသူအဖွဲ့_zero=ဗမာတွေ_zero=ဗမာစစ်တပ်_zero=ဗမာအကြမ်းဖက်_zero=ဗမာတွေ_zero=ဗလီတွေ_zero=ဘင်ဂါလီ_zero=ဘိန်းစား_zero=မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_zero=မူစလင်ကုလား_zero=မူဆလင်_zero=မူဆလင်ကုလားတွေ_zero=မျိုးဖြုတ်_zero=မြို့သား_zero=မြေသြဇာ_zero=မွတ်_zero=မွတ်ကုလား_zero=မွတ်ကုလားတွေ_zero=မွတ်ဒေါင်း_zero=မွတ်ပါတီ_zero=ရခိုင်အကြမ်းဖက်သမား_zero=ရခိုင်တပ်တော်AA_zero=ရခိုင်သူပုန်aaအကြမ်းဖက်_zero=ရခိုင်အစွန်းရောက်_zero=ရခိုင်ကုလားတွေ_zero=ရခီးတွေ_zero=ရွာသား_zero=လီးကြံ့ဖွတ်_zero=လူရိုင်း_zero=ဝူဟန်_zero=ဝူဟန်တရုတ်_zero=သတ်မတော်_zero=သူခိုး_zero=သူပုန်_zero=သူပုန်မ_zero=သူပုန်လော်ဘီ_zero=သောင်းကျမ်းသူ_zero=အကြမ်းဖက်_zero=အစွန်းရောက်_zero=အဆိပ်သားတွေ_zero=အနီကြောင်_zero=အပြုတ်တိုက်_zero=အမျိုးယုတ်_zero=အမျိုးယုတ်ရှမ်း_zero=အာနာရူးတွေ_zero=အိမ်စောင့်ခွေး_zero=အောက်တန်းကျ_zero=အောက်တန်းစား_zero=string_786_zero =အဘAA_zero=အမြစ်ပြတ်ရှင်း_zero=ခွေး_zero =Thaiပြန်_zero=gwi_zero=ကမ္ဘာ့ကပ်ရောဂါကြီး_zero=ကုလားပြည်နယ်_zero=ကြံ့ဖွတ်သခိုး_zero=ကြံ့ဖွတ်သူခိုးကောင်_zero=ခွေးသူတောင်းစားခွေး_zero=ခွေးသူတောင်းစားမီဒီညာ_zero=ငပွေး_zero=ငလူးပဲ_zero=စစ်သူခိုးကြံ့ဖွတ်_zero=စစ်ဦးဘီလူး_zero=စောက်သုံးမကျအစိုးရ_zero=စောင်ကုလား_zero=တရုပ်စုပ်_zero=တစ်မတ်သား_zero=ထန်းတောသားတွေ_zero=ထမိန်ခြုံနဲ့ဘောမ_zero=နပီဗမာစစ်ခွေးတပ်_zero=နွားကျောင်းသား_zero=ပလောင်တွေ_zero=ပြည်ခိုင်ဖြိုးသူခိုး_zero=ဖင်ကုံး_zero=ဖာသေမစု_zero=ဗမာစစ်အာဏာရှင်အုပ်စု_zero=ဗမာသောင်းကြမ်းသူအဖွဲ့_zero=ဗမာအစိုးရစစ်တပ်_zero=ဗမာအစောရနှင့်ဗမာစစ်တပ်_zero=ဗလီတွေ_zero=မအေလိုးကြံ့ဖွတ်_zero=စောင်ကုလား_zero=လီးဆူး_zero=သုတ်ကြောင်မ_zero=မာမွတ်စူလတန်_zero=မုဒိန်းစစ်တပ်_zero=လူသားစိတ္ကင္းမဲ့_zero=အစွန်းရောက်_zero=အစွန်းရောက်ရခိုင်_zero=အဖျက်သမားaa_zero=ရခိး_zero=အကြမ်းဖက်ကုလားတွေ_zero=အစိမ်းရောင်ခွေး_zero=ရခိုင်နဲ့မပွေး_zero=မွတ်ဒေါင်းခွေ_zero=အရိုးကိုက်ဖွတ်ခွေး_zero=0

AAသူပုန်_one=ကုလားတွေ_one=ကျောင်းနွား_one=ကြံ့ဖွတ်_one=ကြံ့ဖွတ်ပါတီ_one=ခိုးဝင်_one=ခွေးတပ်မတော်_one=ခွေးတရုတ်_one=ခွေးဝဲစား_one=ခွေးသတ်မတော်_one=ခွေးသား_one=ခွေးဦးနှောက်_one=ငလူး_one=ငှက်နီ_one=စစ်ခွေး_one=စစ်အာဏာရှင်_one=စောက်တရုတ်_one=တစ်မတ်သား_one=တရုတ်ခွေး_one=တောသား_one=ထမီခြုံ_one=ထောင်ထွက်_one=ဒီမိုခွေးတွေ_one=ဒေါ်လာစား_one=နီပိန်း_one=နီပေါ_one=ပြည်ထိုင်ခိုး_one=ဖင်ယား_one=ဖွတ်_one=ဖွတ်ပါတီ_one=ဖွတ်သူခိုး_one=ဗမာသောင်းကြမ်းသူအဖွဲ့_one=ဗမာတွေ_one=ဗမာစစ်တပ်_one=ဗမာအကြမ်းဖက်_one=ဗမာတွေ_one=ဗလီတွေ_one=ဘင်ဂါလီ_one=ဘိန်းစား_one=မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_one=မူစလင်ကုလား_one=မူဆလင်_one=မူဆလင်ကုလားတွေ_one=မျိုးဖြုတ်_one=မြို့သား_one=မြေသြဇာ_one=မွတ်_one=မွတ်ကုလား_one=မွတ်ကုလားတွေ_one=မွတ်ဒေါင်း_one=မွတ်ပါတီ_one=ရခိုင်အကြမ်းဖက်သမား_one=ရခိုင်တပ်တော်AA_one=ရခိုင်သူပုန်aaအကြမ်းဖက်_one=ရခိုင်အစွန်းရောက်_one=ရခိုင်ကုလားတွေ_one=ရခီးတွေ_one=ရွာသား_one=လီးကြံ့ဖွတ်_one=လူရိုင်း_one=ဝူဟန်_one=ဝူဟန်တရုတ်_one=သတ်မတော်_one=သူခိုး_one=သူပုန်_one=သူပုန်မ_one=သူပုန်လော်ဘီ_one=သောင်းကျမ်းသူ_one=အကြမ်းဖက်_one=အစွန်းရောက်_one=အဆိပ်သားတွေ_one=အနီကြောင်_one=အပြုတ်တိုက်_one=အမျိုးယုတ်_one=အမျိုးယုတ်ရှမ်း_one=အာနာရူးတွေ_one=အိမ်စောင့်ခွေး_one=အောက်တန်းကျ_one=အောက်တန်းစား_one=string_786_one =အဘAA_one=အမြစ်ပြတ်ရှင်း_one=ခွေး_one =Thaiပြန်_one=gwi_one=ကမ္ဘာ့ကပ်ရောဂါကြီး_one=ကုလားပြည်နယ်_one=ကြံ့ဖွတ်သခိုး_one=ကြံ့ဖွတ်သူခိုးကောင်_one=ခွေးသူတောင်းစားခွေး_one=ခွေးသူတောင်းစားမီဒီညာ_one=ငပွေး_one=ငလူးပဲ_one=စစ်သူခိုးကြံ့ဖွတ်_one=စစ်ဦးဘီလူး_one=စောက်သုံးမကျအစိုးရ_one=စောင်ကုလား_one=တရုပ်စုပ်_one=တစ်မတ်သား_one=ထန်းတောသားတွေ_one=ထမိန်ခြုံနဲ့ဘောမ_one=နပီဗမာစစ်ခွေးတပ်_one=နွားကျောင်းသား_one=ပလောင်တွေ_one=ပြည်ခိုင်ဖြိုးသူခိုး_one=ဖင်ကုံး_one=ဖာသေမစု_one=ဗမာစစ်အာဏာရှင်အုပ်စု_one=ဗမာသောင်းကြမ်းသူအဖွဲ့_one=ဗမာအစိုးရစစ်တပ်_one=ဗမာအစောရနှင့်ဗမာစစ်တပ်_one=ဗလီတွေ_one=မအေလိုးကြံ့ဖွတ်_one=စောင်ကုလား_one=လီးဆူး_one=သုတ်ကြောင်မ_one=မာမွတ်စူလတန်_one=မုဒိန်းစစ်တပ်_one=လူသားစိတ္ကင္းမဲ့_one=အစွန်းရောက်_one=အစွန်းရောက်ရခိုင်_one=အဖျက်သမားaa_one=ရခိး_one=အကြမ်းဖက်ကုလားတွေ_one=အစိမ်းရောင်ခွေး_one=ရခိုင်နဲ့မပွေး_one=မွတ်ဒေါင်းခွေ_one=အရိုးကိုက်ဖွတ်ခွေး_one =0

AAသူပုန်=ကုလားတွေ=ကျောင်းနွား=ကြံ့ဖွတ်=ကြံ့ဖွတ်ပါတီ=ခိုးဝင်=ခွေးတပ်မတော်=ခွေးတရုတ်=ခွေးဝဲစား=ခွေးသတ်မတော်=ခွေးသား=ခွေးဦးနှောက်=ငလူး=ငှက်နီ=စစ်ခွေး=စစ်အာဏာရှင်=စောက်တရုတ်=တစ်မတ်သား=တရုတ်ခွေး=တောသား=ထမီခြုံ=ထောင်ထွက်=ဒီမိုခွေးတွေ=ဒေါ်လာစား=နီပိန်း=နီပေါ=ပြည်ထိုင်ခိုး=ဖင်ယား=ဖွတ်=ဖွတ်ပါတီ=ဖွတ်သူခိုး=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာတွေ=ဗမာစစ်တပ်=ဗမာအကြမ်းဖက်=ဗမာေတွ=ဗလီတွေ=ဘင်ဂါလီ=ဘိန်းစား=မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်=မူစလင်ကုလား=မူဆလင်=မူဆလင်ကုလားတွေ=မျိုးဖြုတ်=မြို့သား=မြေသြဇာ=မွတ်=မွတ်ကုလား=မွတ်ကုလားတွေ=မွတ်ဒေါင်း=မွတ်ပါတီ=ရခိုင်အကြမ်းဖက်သမား=ရခိုင်တပ်တော်AA=ရခိုင်သူပုန်aaအကြမ်းဖက်=ရခိုင်အစွန်းရောက်=ရခိုင်ကုလားတွေ=ရခိုင်တပ်တော်AA=ရခီးတွေ=ရွာသား=လီးကြံ့ဖွတ်=လူရိုင်း=ဝူဟန်=ဝူဟန်တရုတ်=သတ်မတော်=သူခိုး=သူပုန်=သူပုန်မ=သူပုန်လော်ဘီ=သောင်းကျမ်းသူ=အကြမ်းဖက်=အစွန်းရောက်=အဆိပ်သားတွေ=အနီကြောင်=အပြုတ်တိုက်=အမျိုးယုတ်=အမျိုးယုတ်ရှမ်း=အာနာရူးတွေ=အိမ်စောင့်ခွေး=အောက်တန်းကျ=အောက်တန်းစား=string_786 =အဘAA=အမြစ်ပြတ်ရှင်း=ခွေး =Thaiပြန်=gwi=ကမ္ဘာ့ကပ်ရောဂါကြီး=ကုလားပြည်နယ်=ကြံ့ဖွတ်သခိုး=ကြံ့ဖွတ်သူခိုးကောင်=ခွေးသူတောင်းစားခွေး=ခွေးသူတောင်းစားမီဒီညာ=ငပွေး=ငလူးပဲ=စစ်သူခိုးကြံ့ဖွတ်=စစ်ဦးဘီလူး=စောက်သုံးမကျအစိုးရ=စောင်ကုလား=တရုပ်စုပ်=တစ်မတ်သား=ထန်းတောသားတွေ=ထမိန်ခြုံနဲ့ဘောမ=နပီဗမာစစ်ခွေးတပ်=နွားကျောင်းသား=ပလောင်တွေ=ပြည်ခိုင်ဖြိုးသူခိုး=ဖင်ကုံး=ဖာသေမစု=ဗမာစစ်အာဏာရှင်အုပ်စု=ဗမာသောင်းကြမ်းသူအဖွဲ့=ဗမာအစိုးရစစ်တပ်=ဗမာအစောရနှင့်ဗမာစစ်တပ်=ဗလီတွေ=မအေလိုးကြံ့ဖွတ်=စောင်ကုလား=လီးဆူး=သုတ်ကြောင်မ=မာမွတ်စူလတန်=မုဒိန်းစစ်တပ်=လူသားစိတ္ကင္းမဲ့=အစွန်းရောက်=အစွန်းရောက်ရခိုင်=အဖျက်သမားaa=ရခိး =အကြမ်းဖက်ကုလားတွေ=အစိမ်းရောင်ခွေး=ရခိုင်နဲ့မပွေး=မွတ်ဒေါင်းခွေ=အရိုးကိုက်ဖွတ်ခွေး =ခွေးသူတောင်းစားမီဒီယာ=0


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
        elif key=='NewHSWordInSentence':
            NewHSWordInSentence_key=annotate_here_val[index][key]
        elif key=='IsHS':
            IsHS_key=annotate_here_val[index][key]
        else:pass
    annotate_here_list.append([LexFound_key,NewHSWordInSentence_key,IsHS_key])

#Create annotate_here dataframe 
annotate_here_df = pd.DataFrame(annotate_here_list, columns=['LexFound','NewHSWordInSentence','IsHS'])



# Annotate_here_2
annotate_here_two = annotate.get_worksheet(1)   
annotate_here_two_val=annotate_here_two.get_all_records()
annotate_here_two_list=[]
for index in range(len(annotate_here_two_val)):
    for key in annotate_here_two_val[index]:
        if key=='LexFound':
            LexFound_key=annotate_here_two_val[index][key]
        elif key=='NewHSWordInSentence':
            NewHSWordInSentence_key=annotate_here_two_val[index][key]
        elif key=='IsHS':
            IsHS_key=annotate_here_two_val[index][key]
        else:pass
    annotate_here_two_list.append([LexFound_key,NewHSWordInSentence_key,IsHS_key])
    
#Create annotate_here dataframe 
annotate_here_two_df = pd.DataFrame(annotate_here_two_list, columns=['LexFound','NewHSWordInSentence','IsHS'])


# Annotate_here_3
annotate_here_three = annotate.get_worksheet(2)   #
annotate_here_threeval=annotate_here_three.get_all_records()
annotate_here_three_list=[]
for index in range(len(annotate_here_threeval)):
    for key in annotate_here_threeval[index]:
        if key=='LexFound':
            LexFound_key=annotate_here_threeval[index][key]
        elif key=='NewHSWordInSentence':
            NewHSWordInSentence_key=annotate_here_threeval[index][key]
        elif key=='IsHS':
            IsHS_key=annotate_here_threeval[index][key]
        else:pass
    annotate_here_three_list.append([LexFound_key,NewHSWordInSentence_key,IsHS_key])

#Create annotate_here dataframe 
annotate_here_three_df = pd.DataFrame(annotate_here_three_list, columns=['LexFound','NewHSWordInSentence','IsHS'])
annotate_here_three_df.head()

hatespeech=annotate_here_df.append((annotate_here_two_df,annotate_here_three_df),ignore_index=True)

hatespeech_annotate=hate=[]
hs_total_count=nohs_total_count=0
for index, row in hatespeech.iterrows(): 
    isHS=row["IsHS"]
    if isHS=="1" or isHS==1 or isHS=="1.0" or isHS==1.0:    # Count the number of hs comment is TRUE
        hs_total_count+=1
        hatespeech_annotate.append(row)
    elif isHS=="0" or isHS==0 or isHS==0.0 or isHS=="0.0":      # Count the number of no hs comment is TRUE 
        nohs_total_count+=1
        hatespeech_annotate.append(row)
print("HS comment : ",hs_total_count," and NO HS Comment : ", nohs_total_count)

total_hs_count=hs_total_count+nohs_total_count 



annotate_folder =glob('../annotate/accuracy-folder/')
annotate=max(annotate_folder, key=os.path.getmtime)


## Accuracy Value  which is HS Comment
Accuracy = (hs_total_count)/(hs_total_count+nohs_total_count)

Accuracy_list=['Accuracy',Accuracy]
accuracy_df=pd.DataFrame([Accuracy_list],columns=['HS Comment','Value'])

accuracy_df=accuracy_df.to_csv(annotate+"hatespeech_accuracy.csv", sep='~',index=False)



LexFound = hatespeech['LexFound'].unique()


for index,row in hatespeech.iterrows():
    LexFound=str(row["LexFound"]).replace(" ","").split("~")
    NewHSWordInSentence=str(row["NewHSWordInSentence"]).replace(" ","").split(",")
    Lexicon= LexFound+NewHSWordInSentence
    isHS=row["IsHS"]

    for lex in Lexicon:
        if lex=='မွတ်ကုလား':
            if isHS==1: မွတ်ကုလား_one+=1
            elif isHS==0:မွတ်ကုလား_zero+=1

        elif lex=='မြို့သား':
            if isHS==1: မြို့သား_one+=1
            elif isHS==0:မြို့သား_zero+=1

        elif lex=='မြေသြဇာ':
            if isHS==1: မြေသြဇာ_one+=1
            elif isHS==0:မြေသြဇာ_zero+=1

        elif lex=='မွတ်':
            if isHS==1: မွတ်_one+=1
            elif isHS==0:မွတ်_zero+=1

        elif lex=='မွတ်ကုလားတွေ':
            if isHS==1:
                မွတ်ကုလားတွေ_one+=1
            elif isHS==0:
                မွတ်ကုလားတွေ_zero+=1
            
        elif lex=='မွတ်ဒေါင်း':
            if isHS==1: မွတ်ဒေါင်း_one+=1
            elif isHS==0:မွတ်ဒေါင်း_zero+=1
   
        elif lex=='မွတ်ဒေါင်းခွေ':
            if isHS==1: 
                မွတ်ဒေါင်းခွေ_one+=1
                
            elif isHS==0:
                မွတ်ဒေါင်းခွေ_zero+=1
            
        elif lex=='မွတ်ပါတီ':
            if isHS==1: မွတ်ပါတီ_one+=1
            elif isHS==0:မွတ်ပါတီ_zero+=1

        elif lex=='ရခိုင်အကြမ်းဖက်သမား':
            if isHS==1: ရခိုင်အကြမ်းဖက်သမား_one+=1
            elif isHS==0:ရခိုင်အကြမ်းဖက်သမား_zero+=1
            
        elif lex=='ရခိး' or lex=='ရခီး' or lex=='ရခွီး':
            if isHS==1: ရခိး_one+=1
            elif isHS==0:ရခိး_zero+=1
        elif lex=='ရခိုင်တပ်တော်AA':
            if isHS==1: ရခိုင်တပ်တော်AA_one+=1
            elif isHS==0:ရခိုင်တပ်တော်AA_zero+=1

        elif lex=='ရခိုင်နဲ့မပွေး':
            if isHS==1: ရခိုင်နဲ့မပွေး_one+=1
            elif isHS==0:ရခိုင်နဲ့မပွေး_zero+=1

        elif lex=='ရခိုင်သူပုန်aaအကြမ်းဖက်':
            if isHS==1:ရခိုင်သူပုန်aaအကြမ်းဖက်_one+=1
            elif isHS==0:ရခိုင်သူပုန်aaအကြမ်းဖက်_zero+=1

        elif lex=='ရခိုင်အစွန်းရောက်':
            if isHS==1:ရခိုင်အစွန်းရောက်_one+=1
            elif isHS==0:ရခိုင်အစွန်းရောက်_zero+=1

        elif lex=='ရခိုင်ကုလားတွေ':
            if isHS==1:ရခိုင်ကုလားတွေ_one+=1
            elif isHS==0:ရခိုင်ကုလားတွေ_zero+=1

        elif lex=='ရခီးတွေ':
            if isHS==1:ရခီးတွေ_one+=1
            elif isHS==0:ရခီးတွေ_zero+=1

        elif lex=='ရွာသား':
            if isHS==1:ရွာသား_one+=1
            elif isHS==0:ရွာသား_zero+=1
            
        elif lex=='လီးကြံ့ဖွတ်':
            if isHS==1:လီးကြံ့ဖွတ်_one+=1
            elif isHS==0:လီးကြံ့ဖွတ်_zero+=1

        elif lex=='လီးဆူး':
            if isHS==1:လီးဆူး_one+=1
            elif isHS==0:လီးဆူး_zero+=1

        elif lex=='လူရိုင်း':
            if isHS==1:လူရိုင်း_one+=1
            elif isHS==0:လူရိုင်း_zero+=1
            
        elif lex=='လူသားစိတ္ ကင္းမဲ့' or lex=='လူသားစိတ်ကင်းမဲ့':
            if isHS==1:လူသားစိတ္ကင္းမဲ့_one+=1
            elif isHS==0:လူသားစိတ္ကင္းမဲ့_zero+=1
            
        elif lex=='ဝူဟန်':
            if isHS==1:ဝူဟန်_one+=1
            elif isHS==0:ဝူဟန်_zero+=1
            
        elif lex=='ဝူဟန်တရုတ်':
            if isHS==1:ဝူဟန်တရုတ်_one+=1
            elif isHS==0:ဝူဟန်တရုတ်_zero+=1

        elif lex=='သတ်မတော်':
            if isHS==1:သတ်မတော်_one+=1
            elif isHS==0:သတ်မတော်_zero+=1
            
        elif lex=='သုတ်ကြောင်မ':
            if isHS==1:သုတ်ကြောင်မ_one+=1
            elif isHS==0:သုတ်ကြောင်မ_zero+=1
            
        elif lex=='သူခိုး':
            if isHS==1:သူခိုး_one+=1
            elif isHS==0:သူခိုး_zero+=1
            
        elif lex=='သူပုန်':
            if isHS==1:သူပုန်_one+=1
            elif isHS==0:သူပုန်_zero+=1
            
        elif lex=='သူပုန်မ':
            if isHS==1:သူပုန်မ_one+=1
            elif isHS==0:သူပုန်မ_zero+=1
            
        elif lex=='သူပုန်လော်ဘီ':
            if isHS==1:သူပုန်လော်ဘီ_one+=1
            elif isHS==0:သူပုန်လော်ဘီ_zero+=1
            
        elif lex=='သောင်းကျမ်းသူ':
            if isHS==1:သောင်းကျမ်းသူ_one+=1
            elif isHS==0:သောင်းကျမ်းသူ_zero+=1
            
        elif lex=='အကြမ်းဖက်':
            if isHS==1:အကြမ်းဖက်_one+=1
            elif isHS==0:အကြမ်းဖက်_zero+=1
            
        elif lex=='အကြမ်းဖက်ကုလားတွေ':
            if isHS==1:အကြမ်းဖက်ကုလားတွေ_one+=1
            elif isHS==0:အကြမ်းဖက်ကုလားတွေ_zero+=1

        elif lex=='အစိမ်းရောင်ခွေး':
            if isHS==1:အစိမ်းရောင်ခွေး_one+=1
            elif isHS==0:အစိမ်းရောင်ခွေး_zero+=1
        
        elif lex=='အစွန်းရောက်':
            if isHS==1:အစွန်းရောက်_one+=1
            elif isHS==0:အစွန်းရောက်_zero+=1
            
        elif lex=='အစွန်းရောက်ရခိုင်':
            if isHS==1:အစွန်းရောက်ရခိုင်_one+=1
            elif isHS==0:အစွန်းရောက်ရခိုင်_zero+=1

        elif lex=='အဆိပ်သားတွေ':
            if isHS==1:အဆိပ်သားတွေ_one+=1
            elif isHS==0:အဆိပ်သားတွေ_zero+=1

        elif lex=='အနီကြောင်':
            if isHS==1:အနီကြောင်_one+=1
            elif isHS==0:အနီကြောင်_zero+=1

        elif lex=='အပြုတ်တိုက်':
            if isHS==1:အပြုတ်တိုက်_one+=1
            elif isHS==0:အပြုတ်တိုက်_zero+=1

        elif lex=='အဖျက်သမားaa':
            if isHS==1:အဖျက်သမားaa_one+=1
            elif isHS==0:အဖျက်သမားaa_zero+=1
            
        elif lex=='အဘAA' :
            if isHS==1:အဘAA_one+=1
            elif isHS==0:အဘAA_zero+=1
            
        elif lex=='အမျိုးယုတ်':
            if isHS==1:အမျိုးယုတ်_one+=1
            elif isHS==0:အမျိုးယုတ်_zero+=1
            
        elif lex=='အမျိုးယုတ်ရှမ်း':
            if isHS==1:အမျိုးယုတ်ရှမ်း_one+=1
            elif isHS==0:အမျိုးယုတ်ရှမ်း_zero+=1

        elif lex=='အမြစ်ပြတ်ရှင်း':
            if isHS==1:အမြစ်ပြတ်ရှင်း_one+=1
            elif isHS==0:အမြစ်ပြတ်ရှင်း_zero+=1

        elif lex=='အာနာရူးတွေ':
            if isHS==1:အာနာရူးတွေ_one+=1
            elif isHS==0:အာနာရူးတွေ_zero+=1

        elif lex=='အိမ်စောင့်ခွေး':
            if isHS==1:အိမ်စောင့်ခွေး_one+=1
            elif isHS==0:အိမ်စောင့်ခွေး_zero+=1

        elif lex=='အောက်တန်းကျ' or lex=='အောက်တန်းကြ':
            if isHS==1:အောက်တန်းကျ_one+=1
            elif isHS==0:အောက်တန်းကျ_zero+=1

        elif lex=='အောက်တန်းစား':
            if isHS==1:အောက်တန်းစား_one+=1
            elif isHS==0:အောက်တန်းစား_zero+=1


        elif lex=='ေခွး' or lex=='ခွေး':
            if isHS==1:ခွေး_one+=1
            elif isHS==0:ခွေး_zero+=1

        elif lex=='၇၈၆':
            if isHS==1:string_786_one+=1
            elif isHS==0:string_786_zero+=1

        elif lex== 'AAသူပုန်': 
            if isHS==1:AAသူပုန်_one+=1
            elif isHS==0:AAသူပုန်_zero+=1

        elif lex=='Thaiပြန်': 
            if isHS==1:Thaiပြန်_one+=1
            elif isHS==0:Thaiပြန်_zero+=1

        elif lex=='gwi': 
            if isHS==1:gwi_one+=1
            elif isHS==0:gwi_zero+=1

        elif lex=='ကမ္ဘာ့ကပ်ရောဂါကြီး':
            if isHS==1:ကမ္ဘာ့ကပ်ရောဂါကြီး_one+=1
            elif isHS==0:ကမ္ဘာ့ကပ်ရောဂါကြီး_zero+=1

        elif lex=='ကုလားပြည်နယ်':
            if isHS==1:ကုလားပြည်နယ်_one+=1
            elif isHS==0:ကုလားပြည်နယ်_zero+=1

        elif lex=='ကုလားတွေ':
            if isHS==1:ကုလားတွေ_one+=1
            elif isHS==0:ကုလားတွေ_zero+=1

        elif lex=='ကျောင်းနွား': 
            if isHS==1:ကျောင်းနွား_one+=1
            elif isHS==0:ကျောင်းနွား_zero+=1

        elif lex=='ကြံ့ဖွတ်':
            if isHS==1:ကြံ့ဖွတ်_one+=1
            elif isHS==0:ကြံ့ဖွတ်_zero+=1

        elif lex=='ကြံ့ဖွတ်သခိုး':
            if isHS==1:ကြံ့ဖွတ်သခိုး_one+=1
            elif isHS==0:ကြံ့ဖွတ်သခိုး_zero+=1


        elif lex=='ကြံ့ဖွတ်သူခိုးကောင်':
            if isHS==1:ကြံ့ဖွတ်သူခိုးကောင်_one+=1
            elif isHS==0:ကြံ့ဖွတ်သူခိုးကောင်_zero+=1

        elif lex=='ကြံ့ဖွတ်ပါတီ':
            if isHS==1:ကြံ့ဖွတ်ပါတီ_one+=1
            elif isHS==0:ကြံ့ဖွတ်ပါတီ_zero+=1

        elif lex=='ခိုးဝင်':
            if isHS==1:ခိုးဝင်_one+=1
            elif isHS==0:ခိုးဝင်_zero+=1

        elif lex=='ခွေးတပ်မတော်' :
            if isHS==1:ခွေးတပ်မတော်_one+=1
            elif isHS==0:ခွေးတပ်မတော်_zero+=1

        elif lex=='ခွေးတရုတ်':
            if isHS==1:ခွေးတရုတ်_one+=1
            elif isHS==0:ခွေးတရုတ်_zero+=1

        elif lex=='ခွေးသား':
            if isHS==1:ခွေးသား_one+=1
            elif isHS==0:ခွေးသား_zero+=1

        elif lex=='ခွေးသူတောင်းစားခွေး':
            if isHS==1:ခွေးသူတောင်းစားခွေး_one+=1
            elif isHS==0:ခွေးသူတောင်းစားခွေး_zero+=1

        elif lex== 'ခွေးသူတောင်းစားမီဒီညာ':
            if isHS==1:ခွေးသူတောင်းစားမီဒီညာ_one+=1
            elif isHS==0:ခွေးသူတောင်းစားမီဒီညာ_zero+=1


        elif lex=='ခွေးဦးနှောက်':
            if isHS==1:ခွေးဦးနှောက်_one+=1
            elif isHS==0:ခွေးဦးနှောက်_zero+=1

        elif lex=='ခွေးဝဲစား':
            if isHS==1:ခွေးဝဲစား_one+=1
            elif isHS==0:ခွေးဝဲစား_zero+=1

        elif lex=='ခွေးသတ်မတော်' :
            if isHS==1:ခွေးသတ်မတော်_one+=1
            elif isHS==0:ခွေးသတ်မတော်_zero+=1

        elif lex=='ငပွေး':
            if isHS==1:ငပွေး_one+=1
            elif isHS==0:ငပွေး_zero+=1

        elif lex=='ငလူး':
            if isHS==1:ငလူး_one+=1
            elif isHS==0:ငလူး_zero+=1
            
        elif lex=='ငလူးပဲ' :
            if isHS==1:ငလူးပဲ_one+=1
            elif isHS==0:ငလူးပဲ_zero+=1
            
        elif lex=='ငှက်နီ' :
            if isHS==1:ငှက်နီ_one+=1
            elif isHS==0:ငှက်နီ_zero+=1
            
        elif lex== 'စစ်သူခိုးကြံ့ဖွတ်':
            if isHS==1:စစ်သူခိုးကြံ့ဖွတ်_one+=1
            elif isHS==0:စစ်သူခိုးကြံ့ဖွတ်_zero+=1
            
        elif lex=='စစ်အာဏာရှင်':
            if isHS==1:စစ်အာဏာရှင်_one+=1
            elif isHS==0:စစ်အာဏာရှင်_zero+=1
            
        elif lex=='စစ်ခွေး':
            if isHS==1:စစ်ခွေး_one+=1
            elif isHS==0:စစ်ခွေး_zero+=1
        
        elif lex=='စစ်ဦးဘီလူး': 
            if isHS==1:စစ်ဦးဘီလူး_one+=1
            elif isHS==0:စစ်ဦးဘီလူး_zero+=1
            
        elif lex=='စောက်တရုတ်':
            if isHS==1:စောက်တရုတ်_one+=1
            elif isHS==0:စောက်တရုတ်_zero+=1
            
        elif lex=='စောက်သုံးမကျအစိုးရ':
            if isHS==1:စောက်သုံးမကျအစိုးရ_one+=1
            elif isHS==0:စောက်သုံးမကျအစိုးရ_zero+=1

        elif lex=='စောင်ကုလား' :
            if isHS==1:စောင်ကုလား_one+=1
            elif isHS==0:စောင်ကုလား_zero+=1

        elif lex=='တရုပ်စုပ်': 
            if isHS==1:တရုပ်စုပ်_one+=1
            elif isHS==0:တရုပ်စုပ်_zero+=1

        elif lex=='တရုတ်ခွေး' : 
            if isHS==1:တရုတ်ခွေး_one+=1
            elif isHS==0:တရုတ်ခွေး_zero+=1

        elif lex=='တောသား':
            if isHS==1:တောသား_one+=1
            elif isHS==0:တောသား_zero+=1


        elif lex=='ထန်းတောသားတွေ':
            if isHS==1:ထန်းတောသားတွေ_one+=1
            elif isHS==0:ထန်းတောသားတွေ_zero+=1

        elif lex=='ထမိန်ခြုံနဲ့ဘောမ':
            if isHS==1:ထမိန်ခြုံနဲ့ဘောမ_one+=1
            elif isHS==0:ထမိန်ခြုံနဲ့ဘောမ_zero+=1

        elif lex=='ထမီခြုံ':
            if isHS==1:ထမီခြုံ_one+=1
            elif isHS==0:ထမီခြုံ_zero+=1

        elif lex=='ထောင်ထွက်': 
            if isHS==1:ထောင်ထွက်_one+=1
            elif isHS==0:ထောင်ထွက်_zero+=1

        elif lex=='ဒီမိုခွေးတွေ':
            if isHS==1:ဒီမိုခွေးတွေ_one+=1
            elif isHS==0:ဒီမိုခွေးတွေ_zero+=1

        elif lex=='ဒေါ်လာစား': 
            if isHS==1:ဒေါ်လာစား_one+=1
            elif isHS==0:ဒေါ်လာစား_zero+=1

        elif lex== 'နပီဗမာစစ်\u200b\u200bခွေးတပ်' or lex=='နပီဗမာစစ်ခွေးတပ်':
            if isHS==1:နပီဗမာစစ်ခွေးတပ်_one+=1
            elif isHS==0:နပီဗမာစစ်ခွေးတပ်_zero+=1

        elif lex=='နီပိန်း' : 
            if isHS==1:နီပိန်း_one+=1
            elif isHS==0:နီပိန်း_zero+=1

        elif lex=='နီပေါ': 
            if isHS==1:နီပေါ_one+=1
            elif isHS==0:နီပေါ_zero+=1

        elif lex=='နွားကျောင်းသား':
            if isHS==1:နွားကျောင်းသား_one+=1
            elif isHS==0:နွားကျောင်းသား_zero+=1

        elif lex=='ပလောင်တွေ':
            if isHS==1:ပလောင်တွေ_one+=1
            elif isHS==0:ပလောင်တွေ_zero+=1

        elif lex=='ပြည်ခိုင်ဖြိုးသူခိုး':
            if isHS==1:ပြည်ခိုင်ဖြိုးသူခိုး_one+=1
            elif isHS==0:ပြည်ခိုင်ဖြိုးသူခိုး_zero+=1

        elif lex=='ပြည်ထိုင်ခိုး':
            if isHS==1:ပြည်ထိုင်ခိုး_one+=1
            elif isHS==0:ပြည်ထိုင်ခိုး_zero+=1

        elif lex=='ဖင်ကုံး': 
            if isHS==1:ဖင်ကုံး_one+=1
            elif isHS==0:ဖင်ကုံး_zero+=1

        elif lex=='ဖင်ယား':
            if isHS==1:ဖင်ယား_one+=1
            elif isHS==0:ဖင်ယား_zero+=1

        elif lex=='ဖာသေမစု': 
            if isHS==1:ဖာသေမစု_one+=1
            elif isHS==0:ဖာသေမစု_zero+=1

        elif lex=='ဖွတ်သူခိုး': 
            if isHS==1:ဖွတ်သူခိုး_one+=1
            elif isHS==0:ဖွတ်သူခိုး_zero+=1

        elif lex=='ဖွတ်':
            if isHS==1:ဖွတ်_one+=1
            elif isHS==0:ဖွတ်_zero+=1

        elif lex=='ဖွတ်ပါတီ':
            if isHS==1:ဖွတ်ပါတီ_one+=1
            elif isHS==0:ဖွတ်ပါတီ_zero+=1

        elif lex=='ဗမာတွေ' or lex=='ဗမာ' or lex=='ဗမာေတွ':
            if isHS==1:ဗမာတွေ_one+=1
            elif isHS==0:ဗမာတွေ_zero+=1

        elif lex=='ဗမာစစ်အာဏာရှင်အုပ်စု': 
            if isHS==1:ဗမာစစ်အာဏာရှင်အုပ်စု_one+=1
            elif isHS==0:ဗမာစစ်အာဏာရှင်အုပ်စု_zero+=1

        elif lex== 'ဗမာသောင်းကြမ်းသူအဖွဲ့':
            if isHS==1:ဗမာသောင်းကြမ်းသူအဖွဲ့_one+=1
            elif isHS==0:ဗမာသောင်းကြမ်းသူအဖွဲ့_zero+=1

        elif lex== 'ဗမာအစိုးရစစ်တပ်':
            if isHS==1:ဗမာအစိုးရစစ်တပ်_one+=1
            elif isHS==0:ဗမာအစိုးရစစ်တပ်_zero+=1

        elif lex== 'ဗမာအစောရနှင့်ဗမာစစ်တပ်':
            if isHS==1:ဗမာအစောရနှင့်ဗမာစစ်တပ်_one+=1
            elif isHS==0:ဗမာအစောရနှင့်ဗမာစစ်တပ်_zero+=1

        elif lex=='ဗမာစစ်တပ်': 
            if isHS==1:ဗမာစစ်တပ်_one+=1
            elif isHS==0:ဗမာစစ်တပ်_zero+=1

        elif lex=='ဗမာအကြမ်းဖက်':
            if isHS==1:ဗမာအကြမ်းဖက်_one+=1
            elif isHS==0:ဗမာအကြမ်းဖက်_zero+=1

        elif lex== 'ဗလီတွေ':
            if isHS==1:ဗလီတွေ_one+=1
            elif isHS==0:ဗလီတွေ_zero+=1

        elif lex=='ဘင်ဂါလီ' or lex=='ဘင်္ဂါလီ':
            if isHS==1:ဘင်ဂါလီ_one+=1
            elif isHS==0:ဘင်ဂါလီ_zero+=1

        elif lex=='ဘိန်းစား':
            if isHS==1:ဘိန်းစား_one+=1
            elif isHS==0:ဘိန်းစား_zero+=1

        elif lex== 'မအေလိုးကြံ့ဖွတ်':
            if isHS==1:မအေလိုးကြံ့ဖွတ်_one+=1
            elif isHS==0:မအေလိုးကြံ့ဖွတ်_zero+=1

        elif lex=='မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်':
            if isHS==1:မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_one+=1
            elif isHS==0:မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_zero+=1

        elif lex== 'မာမွတ်စူလတန်':
            if isHS==1:မာမွတ်စူလတန်_one+=1
            elif isHS==0:မာမွတ်စူလတန်_zero+=1

        elif lex=='မုဒိန်းစစ်တပ်':
            if isHS==1:မုဒိန်းစစ်တပ်_one+=1
            elif isHS==0:မုဒိန်းစစ်တပ်_zero+=1

        elif lex== 'မူစလင်ကုလား': 
            if isHS==1:မူစလင်ကုလား_one+=1
            elif isHS==0:မူစလင်ကုလား_zero+=1

        elif lex=='မူဆလင်':
            if isHS==1:မူဆလင်_one+=1
            elif isHS==0:မူဆလင်_zero+=1

        elif lex=='မူဆလင်ကုလားတွေ': 
            if isHS==1:မူဆလင်ကုလားတွေ_one+=1
            elif isHS==0:မူဆလင်ကုလားတွေ_zero+=1

        elif lex=='မျိုးဖြုတ်':
            if isHS==1:မျိုးဖြုတ်_one+=1
            elif isHS==0:မျိုးဖြုတ်_zero+=1

        elif lex=='တစ်မတ်သား':
            if isHS==1:တစ်မတ်သား_one+=1
            elif isHS==0:တစ်မတ်သား_zero+=1

        elif lex=='အရိုးကိုက်ဖွတ်ခွေး':
            if isHS==1:အရိုးကိုက်ဖွတ်ခွေး_one+=1
            elif isHS==0:အရိုးကိုက်ဖွတ်ခွေး_zero+=1

        elif lex=='ခွေးသူတောင်းစားမီဒီယာ':
            if isHS==1:ခွေးသူတောင်းစားမီဒီယာ_one+=1
            elif isHS==0:ခွေးသူတောင်းစားမီဒီယာ_zero+=1

# # # # Accuracy

AAသူပုန်=round((AAသူပုန်_one/(AAသူပုန်_one+AAသူပုန်_zero)),7)
ကုလားတွေ=round((ကုလားတွေ_one/(ကုလားတွေ_one+ကုလားတွေ_zero)),7)
ကျောင်းနွား=round((ကျောင်းနွား_one/(ကျောင်းနွား_one+ကျောင်းနွား_zero)),7)
ကြံ့ဖွတ်=round((ကြံ့ဖွတ်_one/(ကြံ့ဖွတ်_one+ကြံ့ဖွတ်_zero)),7)
ကြံ့ဖွတ်ပါတီ=round((ကြံ့ဖွတ်ပါတီ_one/(ကြံ့ဖွတ်ပါတီ_one+ကြံ့ဖွတ်ပါတီ_zero)),7)
ခိုးဝင်=round((ခိုးဝင်_one/(ခိုးဝင်_one+ခိုးဝင်_zero)),7)
ခွေးတပ်မတော်=round((ခွေးတပ်မတော်_one/(ခွေးတပ်မတော်_one+ခွေးတပ်မတော်_zero)),7)
ခွေးတရုတ်=round((ခွေးတရုတ်_one/(ခွေးတရုတ်_one+ခွေးတရုတ်_zero)),7)
ခွေးဝဲစား=round((ခွေးဝဲစား_one/(ခွေးဝဲစား_one+ခွေးဝဲစား_zero)),7)
ခွေးသတ်မတော်=round((ခွေးသတ်မတော်_one/(ခွေးသတ်မတော်_one+ခွေးသတ်မတော်_zero)),7)
ခွေးသား=round((ခွေးသား_one/(ခွေးသား_one+ခွေးသား_zero)),7)
ခွေးဦးနှောက်=round((ခွေးဦးနှောက်_one/(ခွေးဦးနှောက်_one+ခွေးဦးနှောက်_zero)),7)
ငလူး=round((ငလူး_one/(ငလူး_one+ငလူး_zero)),7)
ငှက်နီ=round((ငှက်နီ_one/(ငှက်နီ_one+ငှက်နီ_zero)),7)
စစ်ခွေး=round((စစ်ခွေး_one/(စစ်ခွေး_one+စစ်ခွေး_zero)),7)
စစ်အာဏာရှင်=round((စစ်အာဏာရှင်_one/(စစ်အာဏာရှင်_one+စစ်အာဏာရှင်_zero)),7)
စောက်တရုတ်=round((စောက်တရုတ်_one/(စောက်တရုတ်_zero+စောက်တရုတ်_one)),7)
တစ်မတ်သား=round((တစ်မတ်သား_one/(တစ်မတ်သား_one+တစ်မတ်သား_zero)),7)
တရုတ်ခွေး=round((တရုတ်ခွေး_one/(တရုတ်ခွေး_one+တရုတ်ခွေး_zero)),7)
တောသား=round((တောသား_one/(တောသား_one+တောသား_zero)),7)
ထမီခြုံ=round((ထမီခြုံ_one/(ထမီခြုံ_one+ထမီခြုံ_zero)),7)
ထောင်ထွက်=round((ထောင်ထွက်_one/(ထောင်ထွက်_one+ထောင်ထွက်_zero)),7)
ဒီမိုခွေးတွေ=round((ဒီမိုခွေးတွေ_one/(ဒီမိုခွေးတွေ_one+ဒီမိုခွေးတွေ_zero)),7)
ဒေါ်လာစား=round((ဒေါ်လာစား_one/(ဒေါ်လာစား_one+ဒေါ်လာစား_zero)),7)
နီပိန်း=round((နီပိန်း_one/(နီပိန်း_one+နီပိန်း_zero)),7)
နီပေါ=round((နီပေါ_one/(နီပေါ_one+နီပေါ_zero)),7)
ပြည်ထိုင်ခိုး=round((ပြည်ထိုင်ခိုး_one/(ပြည်ထိုင်ခိုး_one+ပြည်ထိုင်ခိုး_zero)),7)
ဖင်ယား=round((ဖင်ယား_one/(ဖင်ယား_one+ဖင်ယား_zero)),7)
ဖွတ်=round((ဖွတ်_one/(ဖွတ်_one+ဖွတ်_zero)),7)
ဖွတ်ပါတီ=round((ဖွတ်ပါတီ_one/(ဖွတ်ပါတီ_one+ဖွတ်ပါတီ_zero)),7)
ဖွတ်သူခိုး=round((ဖွတ်သူခိုး_one/(ဖွတ်သူခိုး_one+ဖွတ်သူခိုး_zero)),7)
ဗမာသောင်းကြမ်းသူအဖွဲ့=round((ဗမာသောင်းကြမ်းသူအဖွဲ့_one/(ဗမာသောင်းကြမ်းသူအဖွဲ့_one+ဗမာသောင်းကြမ်းသူအဖွဲ့_zero)),7)
ဗမာတွေ=round((ဗမာတွေ_one/(ဗမာတွေ_one+ဗမာတွေ_zero)),7)
ဗမာစစ်တပ်=round((ဗမာစစ်တပ်_one/(ဗမာစစ်တပ်_one+ဗမာစစ်တပ်_zero)),7)
ဗမာအကြမ်းဖက်=round((ဗမာအကြမ်းဖက်_one/(ဗမာအကြမ်းဖက်_one+ဗမာအကြမ်းဖက်_zero)),7)
ဗမာတွေ=round((ဗမာတွေ_one/(ဗမာတွေ_one+ဗမာတွေ_zero)),7)
ဗလီတွေ=round((ဗလီတွေ_one/(ဗလီတွေ_one+ဗလီတွေ_zero)),7)
ဘင်ဂါလီ=round((ဘင်ဂါလီ_one/(ဘင်ဂါလီ_one+ဘင်ဂါလီ_zero)),7)
ဘိန်းစား=round((ဘိန်းစား_one/(ဘိန်းစား_one+ဘိန်းစား_zero)),7)
မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်=round((မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_one/(မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_one+မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်_zero)),7)
မူစလင်ကုလား=round((မူစလင်ကုလား_one/(မူစလင်ကုလား_one+မူစလင်ကုလား_zero)),7)
မူဆလင်=round((မူဆလင်_one/(မူဆလင်_one+မူဆလင်_zero)),7)
မူဆလင်ကုလားတွေ=round((မူဆလင်ကုလားတွေ_one/(မူဆလင်ကုလားတွေ_one+မူဆလင်ကုလားတွေ_zero)),7)
မျိုးဖြုတ်=round((မျိုးဖြုတ်_one/(မျိုးဖြုတ်_one+မျိုးဖြုတ်_zero)),7)
မြို့သား=round((မြို့သား_one/(မြို့သား_one+မြို့သား_zero)),7)
မြေသြဇာ=round((မြေသြဇာ_one/(မြေသြဇာ_one+မြေသြဇာ_zero)),7)
မွတ်=round((မွတ်_one/(မွတ်_one+မွတ်_zero)),7)
မွတ်ကုလား=round((မွတ်ကုလား_one/(မွတ်ကုလား_one+မွတ်ကုလား_zero)),7)
မွတ်ကုလားတွေ=round((မွတ်ကုလားတွေ_one/(မွတ်ကုလားတွေ_one+မွတ်ကုလားတွေ_zero)),7)
မွတ်ဒေါင်း=round((မွတ်ဒေါင်း_one/(မွတ်ဒေါင်း_one+မွတ်ဒေါင်း_zero)),7)
မွတ်ပါတီ=round((မွတ်ပါတီ_one/(မွတ်ပါတီ_one+မွတ်ပါတီ_zero)),7)
ရခိုင်အကြမ်းဖက်သမား=round((ရခိုင်အကြမ်းဖက်သမား_one/(ရခိုင်အကြမ်းဖက်သမား_one+ရခိုင်အကြမ်းဖက်သမား_zero)),7)
ရခိုင်တပ်တော်AA=round((ရခိုင်တပ်တော်AA_one/(ရခိုင်တပ်တော်AA_one+ရခိုင်တပ်တော်AA_zero)),7)
ရခိုင်သူပုန်aaအကြမ်းဖက်=round((ရခိုင်သူပုန်aaအကြမ်းဖက်_one/(ရခိုင်သူပုန်aaအကြမ်းဖက်_zero+ရခိုင်သူပုန်aaအကြမ်းဖက်_one)),7)
ရခိုင်အစွန်းရောက်=round((ရခိုင်အစွန်းရောက်_one/(ရခိုင်အစွန်းရောက်_one+ရခိုင်အစွန်းရောက်_zero)),7)
ရခိုင်ကုလားတွေ=round((ရခိုင်ကုလားတွေ_one/(ရခိုင်ကုလားတွေ_one+ရခိုင်ကုလားတွေ_zero)),7)
ရခီးတွေ=round((ရခီးတွေ_one/(ရခီးတွေ_one+ရခီးတွေ_zero)),7)
ရွာသား=round((ရွာသား_one/(ရွာသား_one+ရွာသား_zero)),7)
လီးကြံ့ဖွတ်=round((လီးကြံ့ဖွတ်_one/(လီးကြံ့ဖွတ်_one+လီးကြံ့ဖွတ်_zero)),7)
လူရိုင်း=round((လူရိုင်း_one/(လူရိုင်း_one+လူရိုင်း_zero)),7)
ဝူဟန်=round((ဝူဟန်_one/(ဝူဟန်_one+ဝူဟန်_zero)),7)
ဝူဟန်တရုတ်=round((ဝူဟန်တရုတ်_one/(ဝူဟန်တရုတ်_one+ဝူဟန်တရုတ်_zero)),7)
သတ်မတော်=round((သတ်မတော်_one/(သတ်မတော်_one+သတ်မတော်_zero)),7)
သူခိုး=round((သူခိုး_one/(သူခိုး_one+သူခိုး_zero)),7)
သူပုန်=round((သူပုန်_one/(သူပုန်_one+သူပုန်_zero)),7)
သူပုန်မ=round((သူပုန်မ_one/(သူပုန်မ_one+သူပုန်မ_zero)),7)
သူပုန်လော်ဘီ=round((သူပုန်လော်ဘီ_one/(သူပုန်လော်ဘီ_one+သူပုန်လော်ဘီ_zero)),7)
သောင်းကျမ်းသူ=round((သောင်းကျမ်းသူ_one/(သောင်းကျမ်းသူ_one+သောင်းကျမ်းသူ_zero)),7)
အကြမ်းဖက်=round((အကြမ်းဖက်_one/(အကြမ်းဖက်_one+အကြမ်းဖက်_zero)),7)
အစွန်းရောက်=round((အစွန်းရောက်_one/(အစွန်းရောက်_one+အစွန်းရောက်_zero)),7)
အဆိပ်သားတွေ=round((အဆိပ်သားတွေ_one/(အဆိပ်သားတွေ_one+အဆိပ်သားတွေ_zero)),7)
အနီကြောင်=round((အနီကြောင်_one/(အနီကြောင်_one+အနီကြောင်_zero)),7)
အပြုတ်တိုက်=round((အပြုတ်တိုက်_one/(အပြုတ်တိုက်_one+အပြုတ်တိုက်_zero)),7)
အမျိုးယုတ်=round((အမျိုးယုတ်_one/(အမျိုးယုတ်_one+အမျိုးယုတ်_zero)),7)
အမျိုးယုတ်ရှမ်း=round((အမျိုးယုတ်ရှမ်း_one/(အမျိုးယုတ်ရှမ်း_one+အမျိုးယုတ်ရှမ်း_zero)),7)
အာနာရူးတွေ=round((အာနာရူးတွေ_one/(အာနာရူးတွေ_one+အာနာရူးတွေ_zero)),7)
အိမ်စောင့်ခွေး=round((အိမ်စောင့်ခွေး_one/(အိမ်စောင့်ခွေး_one+အိမ်စောင့်ခွေး_zero)),7)
အောက်တန်းကျ=round((အောက်တန်းကျ_one/(အောက်တန်းကျ_one+အောက်တန်းကျ_zero)),7)
အောက်တန်းစား=round((အောက်တန်းစား_one/(အောက်တန်းစား_one+အောက်တန်းစား_zero)),7)
string_786 =round((string_786_one/(string_786_one+string_786_zero)),7)
အဘAA=round((အဘAA_one/(အဘAA_one+အဘAA_zero)),7)
အမြစ်ပြတ်ရှင်း=round((အမြစ်ပြတ်ရှင်း_one/(အမြစ်ပြတ်ရှင်း_one+အမြစ်ပြတ်ရှင်း_zero)),7)
ခွေး =round((ခွေး_one/(ခွေး_one+ခွေး_zero)),7)
Thaiပြန်=round((Thaiပြန်_one/(Thaiပြန်_one+Thaiပြန်_zero)),7)
gwi=round((gwi_one/(gwi_one+gwi_zero)),7)
ကမ္ဘာ့ကပ်ရောဂါကြီး=round((ကမ္ဘာ့ကပ်ရောဂါကြီး_one/(ကမ္ဘာ့ကပ်ရောဂါကြီး_one+ကမ္ဘာ့ကပ်ရောဂါကြီး_zero)),7)
ကုလားပြည်နယ်=round((ကုလားပြည်နယ်_one/(ကုလားပြည်နယ်_one+ကုလားပြည်နယ်_zero)),7)
ကြံ့ဖွတ်သခိုး=round((ကြံ့ဖွတ်သခိုး_one/(ကြံ့ဖွတ်သခိုး_one+ကြံ့ဖွတ်သခိုး_zero)),7)
ကြံ့ဖွတ်သူခိုးကောင်=round((ကြံ့ဖွတ်သူခိုးကောင်_one/(ကြံ့ဖွတ်သူခိုးကောင်_one+ကြံ့ဖွတ်သူခိုးကောင်_zero)),7)
ခွေးသူတောင်းစားခွေး=round((ခွေးသူတောင်းစားခွေး_one/(ခွေးသူတောင်းစားခွေး_one+ခွေးသူတောင်းစားခွေး_zero)),7)
ခွေးသူတောင်းစားမီဒီညာ=round((ခွေးသူတောင်းစားမီဒီညာ_one/(ခွေးသူတောင်းစားမီဒီညာ_one+ခွေးသူတောင်းစားမီဒီညာ_zero)),7)
ငပွေး=round((ငပွေး_one/(ငပွေး_one+ငပွေး_zero)),7)
ငလူးပဲ=round((ငလူးပဲ_one/(ငလူးပဲ_one+ငလူးပဲ_zero)),7)
စစ်သူခိုးကြံ့ဖွတ်=round((စစ်သူခိုးကြံ့ဖွတ်_one/(စစ်သူခိုးကြံ့ဖွတ်_one+စစ်သူခိုးကြံ့ဖွတ်_zero)),7)
စစ်ဦးဘီလူး=round((စစ်ဦးဘီလူး_one/(စစ်ဦးဘီလူး_one+စစ်ဦးဘီလူး_zero)),7)
စောက်သုံးမကျအစိုးရ=round((စောက်သုံးမကျအစိုးရ_one/(စောက်သုံးမကျအစိုးရ_one+စောက်သုံးမကျအစိုးရ_zero)),7)
စောင်ကုလား=round((စောင်ကုလား_one/(စောင်ကုလား_one+စောင်ကုလား_zero)),7)
တရုပ်စုပ်=round((တရုပ်စုပ်_one/(တရုပ်စုပ်_one+တရုပ်စုပ်_zero)),7)
တစ်မတ်သား=round((တစ်မတ်သား_one/(တစ်မတ်သား_one+တစ်မတ်သား_zero)),7)
ထန်းတောသားတွေ=round((ထန်းတောသားတွေ_one/(ထန်းတောသားတွေ_one+ထန်းတောသားတွေ_zero)),7)
ထမိန်ခြုံနဲ့ဘောမ=round((ထမိန်ခြုံနဲ့ဘောမ_one/(ထမိန်ခြုံနဲ့ဘောမ_one+ထမိန်ခြုံနဲ့ဘောမ_zero)),7)
နပီဗမာစစ်ခွေးတပ်=round((နပီဗမာစစ်ခွေးတပ်_one/(နပီဗမာစစ်ခွေးတပ်_one+နပီဗမာစစ်ခွေးတပ်_zero)),7)
နွားကျောင်းသား=round((နွားကျောင်းသား_one/(နွားကျောင်းသား_one+နွားကျောင်းသား_zero)),7)
ပလောင်တွေ=round((ပလောင်တွေ_one/(ပလောင်တွေ_one+ပလောင်တွေ_zero)),7)
ပြည်ခိုင်ဖြိုးသူခိုး=round((ပြည်ခိုင်ဖြိုးသူခိုး_one/(ပြည်ခိုင်ဖြိုးသူခိုး_one+ပြည်ခိုင်ဖြိုးသူခိုး_zero)),7)
ဖင်ကုံး=round((ဖင်ကုံး_one/(ဖင်ကုံး_one+ဖင်ကုံး_zero)),7)
ဖာသေမစု=round((ဖာသေမစု_one/(ဖာသေမစု_one+ဖာသေမစု_zero)),7)
ဗမာစစ်အာဏာရှင်အုပ်စု=round((ဗမာစစ်အာဏာရှင်အုပ်စု_one/(ဗမာစစ်အာဏာရှင်အုပ်စု_one+ဗမာစစ်အာဏာရှင်အုပ်စု_zero)),7)
ဗမာသောင်းကြမ်းသူအဖွဲ့=round((ဗမာသောင်းကြမ်းသူအဖွဲ့_one/(ဗမာသောင်းကြမ်းသူအဖွဲ့_one+ဗမာသောင်းကြမ်းသူအဖွဲ့_zero)),7)
ဗမာအစိုးရစစ်တပ်=round((ဗမာအစိုးရစစ်တပ်_one/(ဗမာအစိုးရစစ်တပ်_one+ဗမာအစိုးရစစ်တပ်_zero)),7)
ဗမာအစောရနှင့်ဗမာစစ်တပ်=round((ဗမာအစောရနှင့်ဗမာစစ်တပ်_one/(ဗမာအစောရနှင့်ဗမာစစ်တပ်_one+ဗမာအစောရနှင့်ဗမာစစ်တပ်_zero)),7)
ဗလီတွေ=round((ဗလီတွေ_one/(ဗလီတွေ_one+ဗလီတွေ_zero)),7)
မအေလိုးကြံ့ဖွတ်=round((မအေလိုးကြံ့ဖွတ်_one/(မအေလိုးကြံ့ဖွတ်_one+မအေလိုးကြံ့ဖွတ်_zero)),7)
စောင်ကုလား=round((စောင်ကုလား_one/(စောင်ကုလား_one+စောင်ကုလား_zero)),7)
လီးဆူး=round((လီးဆူး_one/(လီးဆူး_one+လီးဆူး_zero)),7)
သုတ်ကြောင်မ=round((သုတ်ကြောင်မ_one/(သုတ်ကြောင်မ_one+သုတ်ကြောင်မ_zero)),7)
မာမွတ်စူလတန်=round((မာမွတ်စူလတန်_one/(မာမွတ်စူလတန်_one+မာမွတ်စူလတန်_zero)),7)
မုဒိန်းစစ်တပ်=round((မုဒိန်းစစ်တပ်_one/(မုဒိန်းစစ်တပ်_one+မုဒိန်းစစ်တပ်_zero)),7)
လူသားစိတ္ကင္းမဲ့=round((လူသားစိတ္ကင္းမဲ့_one/(လူသားစိတ္ကင္းမဲ့_one+လူသားစိတ္ကင္းမဲ့_zero)),7)
အစွန်းရောက်=round((အစွန်းရောက်_one/(အစွန်းရောက်_one+အစွန်းရောက်_zero)),7)
အစွန်းရောက်ရခိုင်=round((အစွန်းရောက်ရခိုင်_one/(အစွန်းရောက်ရခိုင်_one+အစွန်းရောက်ရခိုင်_zero)),7)
အဖျက်သမားaa=round((အဖျက်သမားaa_one/(အဖျက်သမားaa_one+အဖျက်သမားaa_zero)),7)
ရခိး =round((ရခိး_one/(ရခိး_one+ရခိး_zero)),7)
အကြမ်းဖက်ကုလားတွေ=round((အကြမ်းဖက်ကုလားတွေ_one/(အကြမ်းဖက်ကုလားတွေ_one+အကြမ်းဖက်ကုလားတွေ_zero)),7)
အစိမ်းရောင်ခွေး=round((အစိမ်းရောင်ခွေး_one/(အစိမ်းရောင်ခွေး_one+အစိမ်းရောင်ခွေး_zero)),7)
ရခိုင်နဲ့မပွေး=round((ရခိုင်နဲ့မပွေး_one/(ရခိုင်နဲ့မပွေး_one+ရခိုင်နဲ့မပွေး_zero)),7)
မွတ်ဒေါင်းခွေ=round((မွတ်ဒေါင်းခွေ_one/(မွတ်ဒေါင်းခွေ_one+မွတ်ဒေါင်းခွေ_zero)),7)

# create accuracy for lexicon file
lexicon_value= [မွတ်ကုလား,မြို့သား,မြေသြဇာ,မွတ်,မွတ်ကုလားတွေ,မွတ်ဒေါင်း,မွတ်ဒေါင်းခွေ,မွတ်ပါတီ,ရခိုင်အကြမ်းဖက်သမား,ရခိး,ရခိုင်တပ်တော်AA,ရခိုင်နဲ့မပွေး,ရခိုင်သူပုန်aaအကြမ်းဖက်,ရခိုင်အစွန်းရောက်,ရခိုင်ကုလားတွေ,ရခီးတွေ,ရွာသား,လီးကြံ့ဖွတ်,လီးဆူး,လူရိုင်း,လူသားစိတ္ကင္းမဲ့,ဝူဟန်,ဝူဟန်တရုတ်,သတ်မတော်,သုတ်ကြောင်မ,သူခိုး,သူပုန်,သူပုန်မ,သူပုန်လော်ဘီ,သောင်းကျမ်းသူ,အကြမ်းဖက်,အကြမ်းဖက်ကုလားတွေ,အစိမ်းရောင်ခွေး,အစွန်းရောက်,အစွန်းရောက်ရခိုင်,အဆိပ်သားတွေ,အနီကြောင်,အပြုတ်တိုက်,အဖျက်သမားaa,အဘAA,အမျိုးယုတ်,အမျိုးယုတ်ရှမ်း,အမြစ်ပြတ်ရှင်း,အာနာရူးတွေ,အိမ်စောင့်ခွေး,အောက်တန်းကျ,အောက်တန်းစား,ခွေး,string_786,AAသူပုန်,Thaiပြန်,gwi,ကမ္ဘာ့ကပ်ရောဂါကြီး,ကုလားပြည်နယ်,ကုလားတွေ,ကျောင်းနွား,ကြံ့ဖွတ်,ကြံ့ဖွတ်သခိုး,ကြံ့ဖွတ်သူခိုးကောင် ,ကြံ့ဖွတ်ပါတီ,ခိုးဝင်,ခွေးတပ်မတော်,ခွေးတရုတ်,ခွေးသား,ခွေးသူတောင်းစားခွေး,ခွေးသူတောင်းစားမီဒီညာ,ခွေးဦးနှောက်,ခွေးဝဲစား,ခွေးသတ်မတော် ,ငပွေး,ငလူး,ငလူးပဲ,ငှက်နီ,စစ်သူခိုးကြံ့ဖွတ်,စစ်အာဏာရှင်,စစ်ခွေး,စစ်ဦးဘီလူး,စောက်တရုတ်,စောက်သုံးမကျအစိုးရ,စောင်ကုလား,တရုပ်စုပ်,တရုတ်ခွေး,တောသား,ထန်းတောသားတွေ,ထမိန်ခြုံနဲ့ဘောမ,ထမီခြုံ,ထောင်ထွက်,ဒီမိုခွေးတွေ,ဒေါ်လာစား,နပီဗမာစစ်ခွေးတပ်,နီပိန်း,နီပေါ,နွားကျောင်းသား,ပလောင်တွေ,ပြည်ခိုင်ဖြိုးသူခိုး,ပြည်ထိုင်ခိုး,ဖင်ကုံး,ဖင်ယား,ဖာသေမစု,ဖွတ်သူခိုး,ဖွတ်,ဖွတ်ပါတီ,ဗမာတွေ,ဗမာစစ်အာဏာရှင်အုပ်စု,ဗမာသောင်းကြမ်းသူအဖွဲ့,ဗမာအစိုးရစစ်တပ်,ဗမာအစောရနှင့်ဗမာစစ်တပ်,ဗမာစစ်တပ်,ဗမာအကြမ်းဖက်,ဗလီတွေ,ဘင်ဂါလီ,ဘိန်းစား,မအေလိုးကြံ့ဖွတ်,မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်,မာမွတ်စူလတန်,မုဒိန်းစစ်တပ်,မူစလင်ကုလား,မူဆလင်,မူဆလင်ကုလားတွေ,မျိုးဖြုတ်,တစ်မတ်သား,အရိုးကိုက်ဖွတ်ခွေး,ခွေးသူတောင်းစားမီဒီယာ]

lexicon_cols= ['မွတ်ကုလား','မြို့သား','မြေသြဇာ','မွတ်','မွတ်ကုလားတွေ','မွတ်ဒေါင်း','မွတ်ဒေါင်းခွေ','မွတ်ပါတီ','ရခိုင်အကြမ်းဖက်သမား','ရခိး','ရခိုင်တပ်တော်AA','ရခိုင်နဲ့မပွေး','ရခိုင်သူပုန်aaအကြမ်းဖက်','ရခိုင်အစွန်းရောက်','ရခိုင်ကုလားတွေ','ရခီးတွေ','ရွာသား','လီးကြံ့ဖွတ်','လီးဆူး','လူရိုင်း','လူသားစိတ္ကင္းမဲ့','ဝူဟန်','ဝူဟန်တရုတ်','သတ်မတော်','သုတ်ကြောင်မ','သူခိုး','သူပုန်','သူပုန်မ','သူပုန်လော်ဘီ','သောင်းကျမ်းသူ','အကြမ်းဖက်','အကြမ်းဖက်ကုလားတွေ','အစိမ်းရောင်ခွေး','အစွန်းရောက်','အစွန်းရောက်ရခိုင်','အဆိပ်သားတွေ','အနီကြောင်','အပြုတ်တိုက်','အဖျက်သမားaa','အဘAA','အမျိုးယုတ်','အမျိုးယုတ်ရှမ်း','အမြစ်ပြတ်ရှင်း','အာနာရူးတွေ','အိမ်စောင့်ခွေး','အောက်တန်းကျ','အောက်တန်းစား','ခွေး','၇၈၆','AAသူပုန်','Thaiပြန်','gwi','ကမ္ဘာ့ကပ်ရောဂါကြီး','ကုလားပြည်နယ်','ကုလားတွေ','ကျောင်းနွား','ကြံ့ဖွတ်','ကြံ့ဖွတ်သခိုး','ကြံ့ဖွတ်သူခိုးကောင်' ,'ကြံ့ဖွတ်ပါတီ','ခိုးဝင်','ခွေးတပ်မတော်','ခွေးတရုတ်','ခွေးသား','ခွေးသူတောင်းစားခွေး','ခွေးသူတောင်းစားမီဒီညာ','ခွေးဦးနှောက်','ခွေးဝဲစား','ခွေးသတ်မတော်','ငပွေး','ငလူး','ငလူးပဲ','ငှက်နီ','စစ်သူခိုးကြံ့ဖွတ်','စစ်အာဏာရှင်','စစ်ခွေး','စစ်ဦးဘီလူး','စောက်တရုတ်','စောက်သုံးမကျအစိုးရ','စောင်ကုလား','တရုပ်စုပ်','တရုတ်ခွေး','တောသား','ထန်းတောသားတွေ','ထမိန်ခြုံနဲ့ဘောမ','ထမီခြုံ','ထောင်ထွက်','ဒီမိုခွေးတွေ','ဒေါ်လာစား','နပီဗမာစစ်ခွေးတပ်','နီပိန်း','နီပေါ','နွားကျောင်းသား','ပလောင်တွေ','ပြည်ခိုင်ဖြိုးသူခိုး','ပြည်ထိုင်ခိုး','ဖင်ကုံး','ဖင်ယား','ဖာသေမစု','ဖွတ်သူခိုး','ဖွတ်','ဖွတ်ပါတီ','ဗမာတွေ','ဗမာစစ်အာဏာရှင်အုပ်စု','ဗမာသောင်းကြမ်းသူအဖွဲ့','ဗမာအစိုးရစစ်တပ်','ဗမာအစောရနှင့်ဗမာစစ်တပ်','ဗမာစစ်တပ်','ဗမာအကြမ်းဖက်','ဗလီတွေ','ဘင်ဂါလီ','ဘိန်းစား','မအေလိုးကြံ့ဖွတ်','မာဖီးယားအကြမ်းဖက်စစ်တပ်ထွက်','မာမွတ်စူလတန်','မုဒိန်းစစ်တပ်','မူစလင်ကုလား','မူဆလင်','မူဆလင်ကုလားတွေ','မျိုးဖြုတ်','တစ်မတ်သား','အရိုးကိုက်ဖွတ်ခွေး','ခွေးသူတောင်းစားမီဒီယာ']

# Save as a lexicon's accuracy
uni_lexicon_accuracy=list(zip(lexicon_cols,lexicon_value))




# Save as a uni_lexicon_accuracy csv file
df = pd.DataFrame(uni_lexicon_accuracy,columns=["Lexicon","Accuracy"])
lexicon_accuracy_df=df.to_csv(annotate+"accuracy.csv", sep='~',index=False,mode='w')

