#!/usr/bin/python

#getting the requirements
import json

#initializing data from json array
file = open("words.json")
data = json.load(file)

#for records
removed_words = []

#getting the source
filename = "testfile.txt"

source = open(filename)
source_words = source.read().split()
source.close()

#for debugging
print source_words

#applying sensor
for i in range(0,len(source_words)):
	if source_words[i].lower() in data["words"]:
		removed_words.append(source_words[i])
		source_words[i]="***"

#generating new text
new_text = " ".join(source_words)

#for debugging
print new_text
destination = open(filename,"w")
destination.write(new_text+"\n")
destination.close()

print "\nSensored the document : "+filename
print removed_words,len(removed_words),"words removed."