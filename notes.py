import os
import sys
import re
from report_mentions import reportMentions
from organize_by_mention import organizeByMention
from report_keywords import reportKeywords

def tabsToSpaces(s):
	output = ''
	for i in range(len(s)):
		if s[i] == '\t':
			output = ' '*4
		else:
			output += s[i]
	return output

def reportFormat(t):
	t = t.split('\n')
	t = map(tabsToSpaces, t)
	lengths = map(len, t)
	output = '+' + '-' * max(lengths) + '+\n'
	for i in range(len(t)):
		if i != len(t) - 1:
			output += '|' + t[i] + ' ' * (max(lengths) - lengths[i]) + '|\n'
	output += '+' + '-' * max(lengths) + '+\n\n'
	return output

def main():
	if len(sys.argv) < 2:
		print "Please add the directory in which your notes are found:\npython notes.py path/to/notes/"
		return
	os.chdir(sys.argv[1])
	fileList = os.listdir(os.curdir)
	fileContents = list(fileList)
	
	o = open('analysis_output.txt', 'w')
	
	for i in range(len(fileList)):
		fileContents[i] = open(fileList[i], 'r').readlines()
		
	userInput = '-'
	newData = ''
	
	while True:
		flag = True
		print "Please select a tool:\n\tA. report mentions\n\tB. organize notes by mention\n\tC. Report keywords\n\tQ. quit Notes"
		userInput = raw_input()
		if userInput.lower() == 'a':
			newData = reportMentions(fileContents,fileList)
		elif userInput.lower() == 'b':
			newData = organizeByMention(fileContents, fileList)
		elif userInput.lower() == 'c':
			newData = reportKeywords(fileContents, fileList)
		elif userInput.lower() == 'q':
			break
		else:
			print "\n\nPlease choose one of the options below.\n\n"
			flag = False
		if flag:
			print "The following has been added to your Analysis Output:"
			print reportFormat(newData)
			o.write(newData + '\n')
	
	print "Thank you for using Notes.\nYour analysis is stored in analysis_output.txt"
	o.close()
	
main()
