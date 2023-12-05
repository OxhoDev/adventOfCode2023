import re
import os

#file_name = '/home/rle/Documents/adventOfCode2023/day05/files/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day05/files/data.txt'
result = 0

##DEF
reSeeds = "[^z0-9]"
reLocation = "[^z0-9]"

def find_location (sNum, line):
    banana = line.split(';')
    videIntersideral = banana.pop(0)

    for b in banana:
        vars = re.split(reSeeds , b)
        d = int(vars[0])
        s = int(vars[1])
        rStart = int(vars[2])
        rEnd = int(s+rStart)

        if int(sNum) in range(s, rEnd):
            location = sNum - (s - d)
            #print(location)
            return location
        
    return sNum

##VAR
myFormatLines = []
seedsLocation = []
#lIndex = 1
##MAIN

myLines = open(file_name, 'r').read().split(2*os.linesep)
#print(myLines)
myFormatLines = [l.replace('\n', ';') for l in myLines]
#print(myFormatLines)
seeds = [s for s in re.split(reSeeds, myFormatLines[0]) if s != '']
#remove seeds line because she sucks, and yes, she is a 'she'
videIntersideral = myFormatLines.pop(0)

for sNum in seeds:
    print(sNum)

    #sNum = '79'
    for line in myFormatLines:
        print(line)
        ## find_location
        #print(sNum)
        sNum = find_location(int(sNum), line)
        #location = find_location(sNum, line)
    seedsLocation.append(sNum)
    
print(min(seedsLocation))