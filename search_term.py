import os
import sys
import re
from report_keywords import removeChars, reportFormat

def searchTerm(fileContents, fileList, term):
    output = reportFormat('Search for term: ' + term + '\n')
    return output