import sys
import re

fileName = sys.argv[1]
file = open('../' + fileName, "r")
fileString = file.read().lower()
fileWordList = fileString.split()

myDiction = {}

for word in fileWordList:
    occur = len(re.findall('\\b'+word+'\\b', fileString))
    myDiction[word] = occur

print(myDiction)