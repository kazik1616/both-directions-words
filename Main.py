# -*- coding: utf-8 -*-

import os
import xml.dom.minidom
import re
import math
import codecs
import random
from sets import Set

stopwords =  Set(['a', 'aby', 'acz', 'aczkolwiek', 'aż', 'ale', 'ależ', 'bardzo', 'bardziej', 'bez', 'będą', 'będzie', 'bo', 'by', 'być', 'byli', 'był', 'była', 'było', 'były', 'cali', 'cała', 'cały', 'co', 'cokolwiek', 'coś', 'czasami', 'czasem', 'czy', 'czemu', 'dla', 'dlaczego', 'do', 'gdy', 'gdyż', 'gdzie', 'gdziekolwiek', 'gdzieś', 'i', 'ile', 'ich', 'inna', 'inny', 'iż', 'ja', 'jak', 'jakaś', 'jakichś', 'jakiś', 'jakiż', 'jakkolwiek', 'jako', 'jakoś', 'ją', 'jednak', 'jednakże', 'jego', 'jej', 'jest', 'jeszcze', 'jeżeli', 'już', 'kiedy', 'kimś', 'kto', 'ktokolwiek', 'ktoś', 'która', 'które', 'który', 'których', 'lat', 'lecz', 'lub', 'ma', 'mi', 'mimo', 'mnie', 'moim', 'może', 'możliwe', 'można', 'mu', 'na', 'nad', 'nas', 'natomiast', 'nawet', 'nic', 'nich', 'nie', 'nigdy', 'niż', 'no', 'o', 'obok', 'od', 'około', 'on', 'ona', 'ono', 'oraz', 'pan', 'pana', 'pani', 'po', 'pod', 'podczas', 'pomimo', 'ponad', 'ponieważ', 'powinien', 'powinna', 'powinni', 'powinno', 'prawie', 'przecież', 'przed', 'przez', 'przy', 'roku', 'również', 'są', 'się', 'sobą', 'sobie', 'sposób', 'ta', 'tak', 'taka', 'taki', 'takie', 'także', 'tam', 'te', 'tego', 'tej', 'ten', 'teraz', 'też', 'trzeba', 'to', 'tobie', 'toteż', 'tu', 'twoim', 'twoja', 'twoje', 'twój', 'twym', 'ty', 'tych', 'tylko', 'tym', 'w', 'we', 'według', 'więc', 'właśnie', 'wszyscy', 'wszystko', 'wszystkie', 'za', 'zapewne', 'zawsze', 'ze', 'znowu', 'znów', 'żadna', 'żadne', 'żadnych', 'że', 'żeby'])


class Review:
	def __init__(self,words,grade,wordsno):
		self.words = words
		self.grade = grade
		self.wordsno = wordsno

	def occurences(self, word):
		if (self.words.has_key(word)):
			return self.words[word]
		else:
			return 0

	def differentwords(self):
		return len(self.words)



def getwords(txt):
  # Split words by all non-alpha characters
  words=re.compile('[0-9\t-:{};"()., ?!]+').split(txt)
  # Convert to lowercase
  return [word.lower( ) for word in words if word!='']


def getwordscounted(words):
	res = {}
	for word in words: 

		# Nie liczymy stopwords oraz słów krótszych niż 3 znaki
		#if word in stopwords or len(word)<3:
		if len(word)<3:
			continue
	
		res.setdefault(word,0)
		res[word]+=1
	return res


def addtowc(words):
	for w in words:
		wc.setdefault(w,0)
		wc[w]+=1


def removerareatts():
	for k,v in wc.items():

		#usuwaj slowa wystepujace w malej liczbie dokumentow
		if v<30:
			del wc[k]


def calculateidfs():
	for k,v in wc.items():
		#print v, k, math.log(float(alldocs)/v,2)	
		idfs[k] = math.log(float(alldocs)/v,2)	

def resizenegativesandneutral():
	r = reviews.values()

	for i in range(positivegrades-negativegrades):
		pos = random.randint(0,len(r)-1)
		grade = r[pos].grade
		
		while grade != 'bad':
			pos = random.randint(0,len(r)-1)
			grade = r[pos].grade

		reviews['bad'+str(i)] = r[pos]


	for i in range(positivegrades-neutralgrades):
		pos = random.randint(0,len(r)-1)
		grade = r[pos].grade
		
		while grade != 'neutral':
			pos = random.randint(0,len(r)-1)
			grade = r[pos].grade

		reviews['neutral'+str(i)] = r[pos]



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

reviews = {} 
wc = {} # Lista słów wraz z liczbą dokumentów w których one wystąpiły



for root, dirs, files in os.walk('data/txt'):
	
	print root
	for name in files:
		print name
		file = open(root+"/"+name,'r+')
		text = file.read()
		#print text

