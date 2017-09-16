import os
import sys
import re

def reportMentions(fileContents,fileList):
    for i in range(len(fileContents)):
		tempMentions = []
		for j in range(len(fileContents[i])):
			if re.search('@', fileContents[i][j]):
				line = fileContents[i][j].split(' ')
				for k in range(len(line)):
					if re.search('^@', line[k]):
						tempMentions.append(line[k].strip())
		if len(tempMentions) > 0:
			print fileList[i]
			tempMentions = list(set(tempMentions))
			for j in range(len(tempMentions)):
				print tempMentions[j]
