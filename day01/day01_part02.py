#file_name = '/home/rle/Documents/adventOfCode2023/day01/files/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day01/files/data.txt'

inLetter = ["zero","one","two","three","four","five","six","seven","eight","nine"]
inDigit = ["0","1","2","3","4","5","6","7","8","9"]
#line = 'eightwothree'
result = 0

with open(file_name, 'r') as input_file:
    for line in input_file:
        indexTable = {}
        rindexTable = {}

        for i in range (10):
            #firstNum
            lIndex = line.index(inLetter[i]) if inLetter[i] in line else 10000
            dIndex = line.index(inDigit[i]) if inDigit[i] in line else 10000
            indexTable[i] = min(lIndex,dIndex)
            #lastNum
            lRIndex = line.rindex(inLetter[i]) if inLetter[i] in line else -1
            dRIndex = line.rindex(inDigit[i]) if inDigit[i] in line else -1
            rindexTable[i] = max(lRIndex,dRIndex)
        
        #sort indexes to find first and last letter
        sortedIndexTable = sorted(indexTable.items(), key=lambda item: item[1])
        sortedRIndexTable = sorted(rindexTable.items(), key=lambda item: item[1])

        firstNum = sortedIndexTable[0][0]
        lastNum = sortedRIndexTable[-1][0]
        
        result += int(f'{firstNum}{lastNum}')
print(result)
