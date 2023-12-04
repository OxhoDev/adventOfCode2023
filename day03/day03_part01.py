import re

#file_name = '/home/rle/Documents/adventOfCode2023/day03/files/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day03/files/data.txt'
result = 0

# Exo 1

result = 0
partNumber = -42
lastPartNumber = -42
reSChar = "[^A-Za-z0-9\.]"
reDigits = "[\d]"

def find_schar_pos (matrix,reSChar):
    pos = []
    for l in range(len(matrix)):
        #print(l)
        #foreach char in the current matrix linx
        #for c in range(len(matrix[l])):
        for cIndex, c in enumerate(matrix[l]):
            
            #print(c)
            #if match the regex
            #re.match(regex, c)
            if re.match(reSChar, c):
                print(cIndex, c)
                ## BEFORE CHANGE ON INDEX SYNTAX
                pos.append(str(l)+'|'+ str(cIndex))
    return pos

def find_schar_neighbors_pos (matrix,scharPos,reDigits):
    neighborsPos = []
    lastMatchingIndex = -42
    for scharIndex in scharPos:
        scharIndex = scharIndex.split('|')
        #print(scharIndex)
        for l in range(-1,2):
            lIndex = int(scharIndex[0])
            #print(l)
            lIndex = lIndex + l
            #print(lIndex)
            for c in range(-1,2):
                cIndex = int(scharIndex[1])
                #print(c)
                cIndex = cIndex + c
                if re.match(reDigits, matrix[lIndex][cIndex]):
                    #print(lIndex,cIndex)
                    nIndex = str(lIndex)+str(cIndex)
                    #print(nIndex)
                    if int(nIndex) == lastMatchingIndex+1:
                        print('Found neighbour is already taken in account as digit is next to the previous one')
                    else:
                        if nIndex in neighborsPos:
                            print('Already found this neighbor to a char, don\'t input twice')
                        else:
                            #toto = 'toto'
                            neighborsPos.append(str(lIndex)+'|'+str(cIndex))
                        lastMatchingIndex = int(nIndex)
                    #print(lastMatchingIndex)
                    #print(neighborsPos)
                #pos.append(str(l)+'|'+ str(cIndex))
    return neighborsPos

def find_number (matrix,numIndex,reDigits):
    #numIndex = '02'
    numIndex = numIndex.split('|')
    lIndex = int(numIndex[0])
    cIndex = int(numIndex[1])
    #lIndex = 0
    #cIndex = 2
    partNumber = ''
    #print(matrix[lIndex][cIndex])
    while bool(re.match(reDigits, matrix[lIndex][cIndex])) is True:
        #print(matrix[lIndex][cIndex])
        partNumber = matrix[lIndex][cIndex] + partNumber
        #print(partNumber)
        cIndex = cIndex -1

    cIndex = int(numIndex[1])+1
    while bool(re.match(reDigits, matrix[lIndex][cIndex])) is True:
        #print(matrix[lIndex][cIndex])
        partNumber = partNumber + matrix[lIndex][cIndex]
        #print(partNumber)
        cIndex = cIndex +1

    return partNumber

#MAIN
with open(file_name, 'r') as input_file:
    matrix = [[char for char in line.strip()] for line in input_file]
    scharPos = find_schar_pos(matrix,reSChar)
    print(scharPos)
    neighborsPos = find_schar_neighbors_pos(matrix,scharPos,reDigits)
    print(neighborsPos)
    
    for numIndex in neighborsPos:
        partNumber = find_number(matrix,numIndex,reDigits)
        #if int(partNumber) != int(lastPartNumber):
        result += int(partNumber)
        print(partNumber)
        #lastPartNumber = int(partNumber)

print(result)