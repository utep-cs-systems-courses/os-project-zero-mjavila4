import sys
import re


def overlap(word, oList):
    i = 0
    for string in oList:
        if word == string:
            i += 1
    return i


fileName = sys.argv[1]
file = open('../' + fileName, "r")
fileParse = open('../' + fileName, "r")
textString = file.read()
lines = fileParse.readlines()

myDiction = {'a': 0}

for line in lines:
    for word in line.split():
        occurList = re.findall('\\b'+word+'\\b', textString)
        occur = len(occurList)
        if len(word) == 0:
            occur = overlap(word, occurList)
        myDiction[word] = occur

print(myDiction)
