# -*- coding: utf-8 -*-

import os
import re
import codecs
from sets import Set

allwords =  Set()

def getpalindrom(str):
	return str[::-1] #What a hack :)


def getwords(txt):
  # Split words by all non-alpha characters
  words=re.compile('[0-9\t-:{};"()., ?!]+').split(txt)
  # Convert to lowercase
  return [word.lower( ) for word in words if word!='']




def createoutput():
	
	sortedwords = wc.keys()
	sortedwords.sort()

	file = codecs.open('films.arff','w','utf-8')
	
	file.write('@RELATION films\n');

	for w in sortedwords:
		file.write('@ATTRIBUTE ' + w + ' {t,n}\n');

	
	file.write('@ATTRIBUTE wszystkichslow REAL\n');
	file.write('@ATTRIBUTE roznychslow REAL\n');
	file.write('@ATTRIBUTE ocena {good, neutral, bad}\n\n');
		
	file.write('@DATA\n');	

	for review in reviews.values():


		#zliczanie najczęściej pojawiającego się słowa
		mostrecent = ''
		mostrecentocc = 0

		for w in sortedwords: 

			occurences =  review.occurences(w)

			#Waga będzie niczym alkohol - w promilach
			#weight = occurences * idfs[w] * 1000
			
			#file.write('%d,'%weight)

			if occurences > 0:
				file.write('t,')
			else:
				file.write('n,')


		grade = review.grade
		wordsno = review.wordsno
		differentwords = review.differentwords()

		file.write('%d,%d,%s\n'%(wordsno, differentwords, grade))

	file.close();


for root, dirs, files in os.walk('data/txt'):
	for name in files:
		filepath = root+"/"+name
		print filepath
		file = open(filepath,'r+')
		text = file.read()
		text = unicode(text, 'utf-8')

		for word in getwords(text):
			allwords.add(word)


for word in allwords:
	palindrom = getpalindrom(word)
	if palindrom in allwords:
		print word,' ',palindrom
