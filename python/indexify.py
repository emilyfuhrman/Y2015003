import os
import csv
import nltk

## reset working directory to custom corpus
## first, check what the current directory is
## os.getcwd()

## it should be this:
## '/Users/emilyfuhrman'

## change it to the folder containing convolutes
## os.chdir(r'Dropbox/_Y2015004/Text/convolutes')
## os.getcwd()

from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader

corpusDir = '/Users/emilyfuhrman/Dropbox/_Y2015004/Text/convolutes/'

def getThis(_name):

	name = _name
	path = corpusDir + name + '.txt';

	## FOR INDIVIDUAL WORKS ---------- ##

	## test: import Convolute A
	## 'r' means to open the file for reading (the default)
	## 'U' stands for "Universal", which lets us ignore the different conventions used for marking newlines.
	conv = open(path,'rU')
	conv_raw = conv.read()

	## tokenize
	conv_tokens = word_tokenize(conv_raw)

	## double check that the tokenized text is of type 'list'
	type(conv_tokens)

	## it should say this:
	## <class 'list'>

	## part of speech tagging
	conv_pos = nltk.pos_tag(conv_tokens)

	## now you've got an array of tuples: every word [0], plus its POS [1] -- time to hack
	## create clean array for all the instances of 'this', as well as preceding and following words
	## the order of values will be: 
	## idx, totalLength, {word_this}, {word_this_POS}, {word_prec}, {word_prec_POS}, {word_foll}, {word_foll_POS}
	list_this = []

	for idx,w in enumerate(conv_pos):
		if(w[0].lower() == 'this'):

			## create new array to append to list_this
			item_this = []

			## store total length of text file
			totalLength = len(conv_pos)

			## append index, {word_this}, and {word_this_POS} to that array
			item_this.append(idx)
			item_this.append(totalLength)
			item_this.append(w[0].lower())
			item_this.append(w[1])

			## test for {word_prec}
			if(idx >0):
				item_this.append(conv_pos[idx-1][0].lower())
				item_this.append(conv_pos[idx-1][1])
			else:
				item_this.append('NULL')
				item_this.append('NULL')

			## test for {word_foll}
			if(idx <totalLength):
				item_this.append(conv_pos[idx+1][0].lower())
				item_this.append(conv_pos[idx+1][1])
			else:
				item_this.append('NULL')
				item_this.append('NULL')
			list_this.append(item_this)

	## print(list_this)
	exportCSV(name,list_this)

def exportCSV(_name,_arr):

	filestring = '../Data/' + 'output_' + _name +'.csv'

	with open(filestring,'w',newline='') as f:
		writer = csv.writer(f)
		writer.writerows(_arr)

	## print(_name)

## getThis('A')

## get all files in convolutes directory
fileList = os.listdir(corpusDir)
for f in fileList:
	name = f.split('.')[0]
	if(f.split('.')[1] == 'txt'):
		getThis(name)

