import sys
import re

fileName = sys.argv[1]
file = open('../' + fileName, "r")
fileParse = open('../' + fileName, "r")
textString = file.read()
lines = fileParse.readlines()

myDiction = {'a': 0}

for line in lines:
    for word in line.split():
        occurList = re.findall('\\b'+word.lower()+'\\b', textString)
        occur = len(occurList)
        myDiction[word] = occur

print(myDiction)
