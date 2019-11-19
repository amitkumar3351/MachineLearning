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
        #wordBank = [word.lower() for line in f for word in line.split()]
        txt =""
        for word in f:
            txt +=word 

tokenized = sent_tokenize(txt.lower())
for i in tokenized:
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words]
    tagged = nltk.pos_tag(wordsList) 
wordList = []
for item in tagged:
    wordList.append(str(item[0]))
    wordList.append(str(item[1]))
for i in range(len(col_list)-1):
            for k in range(len(row_list)):
                match = '{}\{}'.format(data[col_list[i+1]][k], 'b')
                words = [re.sub(r"\b"+match,str(data[col_list[0]][k]),w) for w in wordList]
                wordList=words
                #newTagged =  nltk.pos_tag(wordList)
                #print(newTagged)
print(nltk.help.upenn_tagset)
