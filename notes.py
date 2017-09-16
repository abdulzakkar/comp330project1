import os
import sys
import re
from report_mentions import reportMentions

def main():
	os.chdir(sys.argv[1])
	fileList = os.listdir(os.curdir)
	fileContents = list(fileList)
	
	for i in range(len(fileList)):
		fileContents[i] = open(fileList[i], 'r').readlines()
	
	print "Please select a tool:\n\tA. report mentions"
	
	userInput = raw_input()
	if userInput.lower() == 'a':	
		reportMentions(fileContents,fileList)
	
main()
