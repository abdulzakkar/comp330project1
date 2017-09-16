import os
import sys
import re

def main():
	f = open('notes.txt', 'r')
	s = f.readlines()
	f.close()

	for i in range(len(s)):
		if re.search('^!', s[i]):
			print s[i]
	
main()
