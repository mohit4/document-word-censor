#!/usr/bin/python

#getting the requirements
import os
import json
import sys
#from pprint import pprint

records = []
data = None

def sensor_func(source_text):
	global records
	global data
	sensored_text = ""

	temp = ""
	for x in xrange(len(source_text)):
		c = source_text[x]
		if not c.isalnum():
			sensored_text+=temp
			sensored_text+=c
			temp = ""
		else:
			temp+=c

		if temp.lower() in data["words"]:
			sensored_text+="SENSORED"
			records.append(temp)
			temp = ""

	return sensored_text

def main():
	
	global records
	global data
	records = []

	#initializing data from json array
	file = open("sensor_words.json")
	data = json.load(file)

	#getting the source

	if len(sys.argv) <= 1:
		print "Error : No input file given"
		sys.exit(1)

	source_fileName = sys.argv[1]

	if not os.path.isfile(source_fileName):
		print "Error : No such file "+source_fileName
		sys.exit(2)

	destin_fileName = "temp"
	if len(sys.argv) > 2:
		destin_fileName = sys.argv[2]

	source_fileObj = open(source_fileName)
	source_text = source_fileObj.read()
	source_fileObj.close()

	#for debugging only
	#pprint(source_text)

	res_text = sensor_func(source_text)
	destin_fileObj = open(destin_fileName,"w")
	destin_fileObj.write(res_text)
	destin_fileObj.close()

	if destin_fileName == "temp":
		os.remove(source_fileName)
		os.rename(destin_fileName,source_fileName)

	print "Sensored the document : "+source_fileName
	#for debugging only
	#print records
	print len(records),"words removed."


if __name__ == "__main__":
	main()
