import sys
import re
fileName = sys.argv[1]
file = open('../'+fileName, "r").read()
myDic = {}

x = re.findall('', file)

print(len(x))




