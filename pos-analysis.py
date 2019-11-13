import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords') 
stop_words = set(stopwords.words('english')) 


with open('F:/New folder/BBC-Dataset-News-Classification-master/dataset/data_files/sport/001.txt') as f:
        #wordBank = [word.lower() for line in f for word in line.split()]
        txt =""
        for word in f:
            txt +=word 

tokenized = sent_tokenize(txt.lower())
for i in tokenized: 
	
	# Word tokenizers is used to find the words 
	# and punctuation in a string 
	wordsList = nltk.word_tokenize(i)
   # removing stop words from wordList 
	wordsList = [w for w in wordsList if not w in stop_words]
    

	# Using a Tagger. Which is part-of-speech 
	# tagger or POS-tagger. 
	tagged = nltk.pos_tag(wordsList) 

	print(tagged) 
