# -*- coding: utf-8 -*-

import os
import re
import codecs
from sets import Set

allwords =  Set() #list of all found words
splitter = re.compile('[\s\d_\-\>.,\<:;*?~()\\$!\'\/"]+') #words splitter
txtext = [".txt"] #we oricess only txt files

def getpalindrom(str):
	return str[::-1] #What a hack :)


def getwords(txt):
  # Split words by all non-alpha characters
  words=splitter.split(txt)
  # Convert to lowercase
  return [word.lower( ) for word in words if word!='']


for root, dirs, files in os.walk('data/txt'):
	
	for name in files:
		filepath = root+"/"+name
		if os.path.splitext(filepath)[1] in txtext:	
			print 'Processing ',filepath
			file = open(filepath,'r+')
			text = file.read()
			text = unicode(text, 'utf-8')

			for word in getwords(text):
				allwords.add(word)


print 'All different words found: ',len(allwords)

bothdirections = 0
palindroms = 0

print 'List of Words read in both directions:'
for word in allwords:
	palindrom = getpalindrom(word)
	if palindrom in allwords:
		print word,'\t=>\t',palindrom
		bothdirections += 1
		if palindrom == word:
			palindroms += 1

print 'All words that can be read in both directions: ',bothdirections
print 'Numbeer of palindroms: ', palindroms
