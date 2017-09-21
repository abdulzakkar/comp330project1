import os
import sys
import re
from report_keywords import removeChars, reportFormat

def topologicalSort(fileContents, fileList):
    output = reportFormat('Notes topologically sorted:\n')
    for i in range(len(fileContents)):
        for j in range(len(fileContents[i])):
            words = map(removeChars, fileContents[i][j].strip().split(' '))
            for k in range(len(words)):
                if len(words[k]) > 0:
                    if re.search('/\\^/',words[k]) or words[k][0] == '^':
                        output += words[k] + '\n'
    return output