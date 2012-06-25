#!/usr/bin/python
# coding: utf-8

from UnitexManager import UnitexManager

import sys
import twitter
from operator import itemgetter


try:
    # version 2.6+
    import json
except:
    # version 2.5
    import simplejson as json
    
DEFAULT_FILENAME = "../data/NASDAQ_TOP10.json" 


def main(argv):
    print "Starting process..." 

    api = twitter.Api(consumer_key = 'THE KEY' , consumer_secret='THE GOOD',
		 access_token_key='THE BAD', access_token_secret='THE UGLY')
    
    print api.VerifyCredentials()
	
    companyRawData = parseFile(DEFAULT_FILENAME)
    print "Companies Are %s" %companyRawData
    companyData = json.loads(companyRawData.replace('=>', ':'))


    companyText = ""
    companyElements = []
    for element in companyData:
        test = '%s %s %s' %(element["arrow"], element["change"], element["code"])
        companyElements.append(test)
   
    extractedData = []        

    for companyLine in companyElements:
        print " -> Processing: %s " % companyLine
        unitexManager = UnitexManager()
        # Get tokens
        tokens_result = unitexManager.tokenizer(companyLine, "en")
        # Apply POSTtagging
        pos_tagging = unitexManager.postagger(tokens_result, "en")
        # Apply Grammar
        grammar = unitexManager.grammar(tokens_result, pos_tagging, "en")
        print grammar
	extractedData.append(json.loads(grammar))

    print "Extracted data is:\n%s" %extractedData

    stocks = sorted(extractedData, key=itemgetter('number'), reverse=True)   
    print "Ordered Stocks are:\n%s" %stocks

    mostActive = stocks[0:4] 
    print "Most active are:\n%s" %mostActive

    msg = "The most active values in NASDAQ are "
    for stock in mostActive:
	sign = u"↑" if  stock['operator'] == "up" else u"↓";
	msg = "%s %s: %s %s;" %(msg, stock['symbol'], stock['number'], sign)

    print "Msg is [%s]" %msg 	   	
    status = api.PostUpdate(msg)
    print status
	
	
def parseFile(filename):
    file = open(filename, 'r')
    return file.read()

if __name__ == '__main__':
    main(sys.argv[1:])

