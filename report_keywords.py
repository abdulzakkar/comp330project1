import os
import sys
import re

def removeChars(s):
    c = '\'!@#$%^&*().,><;:"[]{}\\|?/`~=+-_'
    output = ''
    for i in range(len(s)):
        if s[i] not in c:
            output += s[i]
    return output
    
def isNum(s):
    for i in range(len(s)):
        if s[i] not in '0123456789':
            return False
    return True
    

def reportKeywords(fileContents,fileList):
    f = open('/home/ubuntu/workspace/boring_words_filtered.txt', 'r')
    boringWords = map(str.lower, map(str.strip, f.readlines()))
    f.close()
    output = 'All Keywords:\n'
    wordCounts = {}
    for i in range(len(fileContents)):
		for j in range(len(fileContents[i])):
		    words = map(str.strip, fileContents[i][j].split(' '))
		    words = map(removeChars, words)
		    for k in range(len(words)):
		        if words[k].lower() in map(str.lower, wordCounts.keys()) and words[k].lower() not in boringWords and not isNum(words[k].lower()):
		            wordCounts[words[k].lower()] += 1
		        else:
		            wordCounts[words[k].lower()]=1
		            if words[k].lower().strip() == 'jacobs':
		                print fileList[i]
    finalOutput = []
    for key, value in wordCounts.iteritems():
        if value > 2:
            finalOutput.append(key)
    finalOutput = sorted(finalOutput)
    for i in range(len(finalOutput)):
        output += finalOutput[i] + '\n'
    return output