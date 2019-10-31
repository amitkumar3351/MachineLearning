from PIL import Image
from spellchecker import SpellChecker 
import pytesseract
import os
import nltk
import nltk.corpus
import os.path
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize 
import time
import numpy as np
import re
import json


data =  pd.read_csv('C:/Users/HP/Music/citi.csv')
col_list= data.axes[1]
row_list= data.axes[0]
masterrow= data["Master_Words"]
start = time.time()
parentDic = {"TotalTime":""}
for j in range(90):
    txtCounter=j+1
    txtCounter= "00"+str(txtCounter)
    if j>=9:
       txtCounter=""
       txtCounter=j+1
       txtCounter= "0"+str(txtCounter)
    with open('F:/New folder/BBC-Dataset-News-Classification-master/dataset/data_files/sport/'+txtCounter+'.txt') as f:
        wordBank = [word.lower() for line in f for word in line.split()]
        infoDic = {"WordsCount": "", "Time": ""}
        infoDic['WordsCount'] = len(wordBank)
        for i in range(len(col_list)-1):
            for k in range(len(row_list)):
                #test
                match = '{}\{}'.format(data[col_list[i+1]][k], 'b')
                words = [re.sub(r"\b"+match,data[col_list[0]][k],w) for w in wordBank]
                wordBank=""
                wordBank=words
                print(wordBank)
        end = time.time()
        infoDic['Time']= end - start
        parentDic.update({txtCounter+".txt":infoDic})        
end = time.time()
parentDic['TotalTime'] = end - start
with open('F:/New folder/BBC-Dataset-News-Classification-master/dataset/data_files/sport/Details_Dump.txt', 'w') as file:
     file.write(json.dumps(parentDic))   
    
