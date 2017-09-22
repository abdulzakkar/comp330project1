import os
import sys
import re
from report_keywords import removeChars, reportFormat

def topologicalSort(fileContents, fileList):
    ids = []
    for i in range(len(fileContents)):
        ids.append(['-'])
    output = reportFormat('Notes topologically sorted\n(Sorted by indegree):\n')
    for i in range(len(fileContents)):
        for j in range(len(fileContents[i])):
            words = fileContents[i][j].strip().split(' ')
            for k in range(len(words)):
                if len(words[k]) > 0:
                    if re.search('^\\^',words[k]):
                        ids[i].append(words[k][1:])
                    if re.search('^!',words[k]):
                        ids[i][0] = words[k][1:]
    indegree = []
    for i in range(len(ids)):
        temp = 0
        for j in range(len(ids)):
            for k in range(1,len(ids[j][1:])+1):
                if ids[j][k] == ids[i][0]:
                    temp += 1
        indegree.append(temp)
    checked = []
    for i in range(len(indegree)):
        checked.append(False)
    for i in range(len(indegree)):
        maxPos = 0
        maxData = indegree[0]
        for j in range(len(indegree)):
            if (indegree[j] > maxData and not checked[j]) or (checked[maxPos] and not checked[j]):
                maxData = indegree[j]
                maxPos = j
        checked[maxPos] = True
        output += fileList[maxPos] + '\n\tIndegree: ' + str(indegree[maxPos]) + '\n'
    return output