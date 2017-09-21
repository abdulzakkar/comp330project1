import os
import sys
import re
from report_mentions import reportMentions
from organize_by_mention import organizeByMention
from report_keywords import reportKeywords, isNum, reportFormat
from notes_by_keyword import notesByKeyword

def menu(isWrite):
	if isWrite:
		toggle = 'ON '
	else:
		toggle = 'OFF'
	output = ''
	output += "+------------------------------------------------------------+\n"
	output += "| Please select a tool:                                      |\n"
	output += "|                                                            |\n"
	output += "| +--------------------+              +--------------------+ |\n"
	output += "| | A. Report mentions |              | Write to file: " + toggle + " | |\n"
	output += "| +--------------------+              | T. Toggle          | |\n"
	output += "|                                     +--------------------+ |\n"
	output += "| +------------------------------+                           |\n"
	output += "| | B. Organize notes by mention |                           |\n"
	output += "| +------------------------------+                           |\n"
	output += "|                                                            |\n"
	output += "| +--------------------+                                     |\n"
	output += "| | C. Report keywords |                                     |\n"
	output += "| +--------------------+                                     |\n"
	output += "|                                                            |\n"
	output += "| +-----------------------------------+                      |\n"
	output += "| | D. Search term (syntax: D [term]) |                      |\n"
	output += "| +-----------------------------------+                      |\n"
	output += "|                                                            |\n"
	output += "| +---------------------+                                    |\n"
	output += "| | E. Notes by keyword |                                    |\n"
	output += "| +---------------------+                                    |\n"
	output += "|                                                            |\n"
	output += "| +---------------------------------+                        |\n"
	output += "| | F. Topologically sort all notes |                        |\n"
	output += "| +---------------------------------+                        |\n"
	output += "|                                                            |\n"
	output += "| +---------------+                                          |\n"
	output += "| | Q. QUIT NOTES |                                          |\n"
	output += "| +---------------+                                          |\n"
	output += "+------------------------------------------------------------+\n"
	return output
	
def save(output,wroteSomething):
	os.chdir('..')
	while True:
		print reportFormat("Thank you for using Notes.\n")
		if wroteSomething:
			print reportFormat("Would you like to save your work? (y/n)\n")
			userInput = raw_input()
			if userInput[0].lower() == 'y':
				print reportFormat('Please name your save file.\n')
				fileName = raw_input()
				if os.path.isfile(fileName):
					print reportFormat(fileName + ' already exists. Overwrite? (y/n)\n')
					userInput = raw_input()
					if userInput[0].lower() == 'y':
						o = open(fileName, 'w')
						o.write(output)
						o.close()
						break
				else:
					try:
						o = open(fileName, 'w')
						o.write(output)
						o.close()
						break
					except:
						print reportFormat('invalid file name/directory.\n')
			else:
				break
		else:
			break

def main():
	if len(sys.argv) < 2:
		print reportFormat('Please add the directory in which your notes are found:\npython notes.py path/to/notes/\n')
		return
	os.chdir(sys.argv[1])
	fileList = os.listdir(os.curdir)
	fileContents = list(fileList)

	for i in range(len(fileList)):
		fileContents[i] = open(fileList[i], 'r').readlines()
		
	userInput = '-'
	newData = ''
	write = True
	output = ''
	wroteSomething = False
	
	while True:
		flag = True
		print menu(write)
		userInput = map(str.strip,raw_input().split(' '))
		if userInput[0].lower() == 'a':
			newData = reportMentions(fileContents,fileList)
		elif userInput[0].lower() == 'b':
			newData = organizeByMention(fileContents, fileList)
		elif userInput[0].lower() == 'c':
			if len(userInput) == 1:
				newData = reportKeywords(fileContents, fileList, 's', 2)
			else:
				if isNum(userInput[1]):
					newData = reportKeywords(fileContents, fileList, 's', int(userInput[1]))
				else:
					print reportFormat('Invalid entry; correct input:\nC [integer: number of columns | default = 2]\n')
					print '+----------------------------------------------+\n'
					flag = False
		elif userInput[0].lower() == 'd':
			print 'Not yet implemented'
			flag = False
		elif userInput[0].lower() == 'e':
			if len(userInput) == 1:
				newData = notesByKeyword(fileContents, fileList, 2)
			else:
				if isNum(userInput[1]):
					newData = notesByKeyword(fileContents, fileList, int(userInput[1]))
				else:
					print reportFormat('Invalid entry; correct input:\nE [integer: minimum number of files containing given keyword | default = 2]\n')
		elif userInput[0].lower() == 'f':
			print 'Not yet implemented'
			flag = False
		elif userInput[0].lower() == 't':
			if write:
				toggle = 'OFF'
				write = False
			else:
				toggle = 'ON '
				write = True
			print reportFormat('Writing to file has been toggled ' + toggle + '\n')
			flag = False
		elif userInput[0].lower() == 'q':
			break
		else:
			print reportFormat("Please choose one of the options below.\n")
			flag = False
		if flag:
			if write:
				wroteSomething = True
				print reportFormat("The following has been added to your Analysis Output:\n")
				output += newData + '\n'
			print reportFormat(newData)
		print reportFormat('PRESS ENTER TO CONTINUE\n')
		z = raw_input()
			
	save(output,wroteSomething)
	
main()
