#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

#make sure text files exist
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()

#make sure output file exists
if not os.path.exists(outputFname):
    print ("wordCount output file %s doesn't exist! Exiting" % outputFname)
    exit()

    
#dictionary for word count
wordcount = {}
#keylist = {}


# attempt to open input file
with open(textFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        #Remove '
        line = line.replace("'"," ") 
        # remove . 
        line = line.replace(".","")
        # remove ?
        line = line.replace("?","")
        # remove !
        line = line.replace("!","")
        # remove ; 
        line = line.replace(";","")
        # remove "
        line = line.replace("\"","")
        #remove ,
        line = line.replace(",","")
        #remove :
        line = line.replace(":","")
        #replace -- with space
        line = line.replace("--"," ")
        #replace 0 with space
        line = line.replace("-"," ")
        # split line on whitespace and punctuation
        words = re.split('[ \t]', line)
        for word in words:
            if word is not "":
                word = word.lower()
                #keylist[word] = word
                if wordcount.get(word) is None:
                    wordcount[word] = 1
                else:
                    wordcount[word] = wordcount[word] + 1 

#sortedWordCount = sorted(wordcount.keys())

#print(key, value) for (key, value) in sorted(orders.items(), key=lambda x: x[1])
with open(outputFname, 'w') as outputFile:
    for i in sorted(wordcount):
        outputFile.write(i + " " + str(wordcount[i]) + "\n")
        

        
