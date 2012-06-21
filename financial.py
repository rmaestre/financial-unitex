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
    #print "Companies Are %s" %companyRawData
    companyData = json.loads(companyRawData.replace('=>', ':'))
    
    companyText = ""
    companyElements = []
    for element in companyData:
        test = '%s %s %s' %(element["arrow"], element["change"], element["code"])
        companyElements.append(test)
        
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
def parseFile(filename):
    file = open(filename, 'r')
    return file.read()

if __name__ == '__main__':
    main(sys.argv[1:])

