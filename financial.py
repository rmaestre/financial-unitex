#!/usr/bin/python
# coding: utf-8

from UnitexManager import UnitexManager
import sys

try:
    # version 2.6+
    import json
except:
    # version 2.5
    import simplejson as json

DEFAULT_FILENAME = "testData.json"

def main(argv):
	print "Starting process..."

	companyRawData = parseFile(DEFAULT_FILENAME)
#	print "Companies Are %s" %companyRawData

	companyData = json.loads(companyRawData.replace('=>', ':'))
#	print companyData

	companyText = ""
	companyElements = []
	for element in companyData:
		companyText = '%s \n %s' %(companyText," ".join(element.values()) )
		test = " ".join(element.values())
		companyElements.append(test)


	print "Company information: \n%s" %companyText

	# Instanciate an object
	unitexManager = UnitexManager()


	print "AAAAAAAAAAAAAAAAAH KAKA"
	for companyLine in companyElements:
		unitexManager = UnitexManager()
		# Get tokens
		tokens_result = unitexManager.tokenizer(companyLine, "en")
		print companyLine		
		
        	# Apply POSTtagging
        	pos_tagging = unitexManager.postagger(tokens_result, "en")
	        print 'Pos tagging: ',pos_tagging
	        print 'token_result:',tokens_result	
  
		print unitexManager
		# Apply Grammar
        	grammar = unitexManager.grammar(tokens_result, pos_tagging, "en")
        	print '=> ',grammar

def parseFile(filename):
	file = open(filename, 'r')
	return file.read()

if __name__ == '__main__':
    main(sys.argv[1:])

