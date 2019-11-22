import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import re
nltk.download('stopwords') 
stop_words = set(stopwords.words('english')) 

data =  pd.read_csv('C:/Users/HP/Music/words-lookup.csv')
col_list= data.axes[1]
row_list= data.axes[0]
with open('F:/New folder/BBC-Dataset-News-Classification-master/dataset/data_files/sport/001.txt') as f:
        txt =""
        for word in f:
            txt +=word
tokenized = sent_tokenize(txt.lower())
wordList = []
for i in tokenized:
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words]
    for i in wordsList : 
        wordList.append(i)
for i in range(len(col_list)-1):
        for k in range(len(row_list)):
            match = '{}\{}'.format(data[col_list[i+1]][k], 'b')
            words = [re.sub(r"\b"+match,str(data[col_list[0]][k]),w) for w in wordList]
            wordList=words
tagged = nltk.pos_tag(wordList)
wordList = []
for item in tagged:
    for k in range(len(row_list)):
        if str(item[0]) == data[col_list[0]][k]:
            wordList.append(str(item[0]))
    if str(item[1])=="CD" or str(item[1])=="NN" or str(item[1])=="NNS" or str(item[1])=="NNP" or str(item[1])=="NNPS" or str(item[1])=="VB" or str(item[1])=="VBD" or str(item[1])=="VBG" or str(item[1])=="VBN" or str(item[1])=="VBP" or str(item[1])=="VBZ" or str(item[1])=="RB" or str(item[1])=="RBR" or str(item[1])=="RBS" or str(item[1])=="JJ" or str(item[1])=="JJR" or str(item[1])=="JJS":
        for k in range(len(row_list)):
            if str(item[0]) != data[col_list[0]][k]:
                wordList.append(str(item[1]))
txtStr=""
for words in wordList:
    txtStr +=words + " "
print(txtStr)
