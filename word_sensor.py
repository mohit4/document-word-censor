#!/usr/bin/python

#getting the requirements
import os
import json
from pprint import pprint

#initializing data from json array
file = open("words.json")
data = json.load(file)

#for records
removed_words = []

#getting the source
source_fileName = "testfile.txt"
destin_fileName = "modifile.txt"

destin_fileObj = open(destin_fileName,"w")
source_fileObj = open(source_fileName)
source_text = source_fileObj.read()
source_fileObj.close()

#for debugging only
#pprint(source_text)

records = []

temp = ""
for x in xrange(len(source_text)):
	c = source_text[x]
	if not c.isalnum():
		destin_fileObj.write(temp)
		destin_fileObj.write(c)
		temp = ""
	else:
		temp+=c

	if temp.lower() in data["words"]:
		destin_fileObj.write("SENSORED")
		records.append(temp)
		temp = ""

destin_fileObj.close()

os.remove(source_fileName)
os.rename(destin_fileName,source_fileName)

print "Sensored the document : "+source_fileName
pprint(records)
print len(records),"words removed."
