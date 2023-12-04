import re

#file_name = '/home/rle/Documents/adventOfCode2023/day04/files/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day04/files/data.txt'
result = 0

##DEF
reSChar = "[^A-Za-z0-9\s]"


def find_winning_num (winNum, playNum):
    print('WIP')
  
'''
def count_card_points (nMatch):
    #multiplies number of match by npoints
    #score = 1
    
    if nMatch == 0:
        score = 0
    else:
        score = 2**(nMatch-1)

    return score
'''

lIndex = 0
#MAIN
with open(file_name, 'r') as input_file:
    myLines = input_file.readlines()
    cardResult = [1] * len(myLines)
    print(cardResult)                     

    for line in myLines:
        #print(line)
        #print(lIndex)
        #print(line)
        splitResult = re.split(reSChar, line.strip())
        #splitResult = ['Card 1', ' 41 48 83 86 17 ', ' 83 86  6 31 17  9 48 53']
        #print(splitResult)

        ### SANDBOX

        lotNum = set([int(n) for n in splitResult[1].split(' ') if n != ''])
        playNum = set([int(n) for n in splitResult[2].split(' ') if n != ''])
        #winNum = [n for n in splitResult[2].split(' ')]
        
        winNum = lotNum.intersection(playNum)
        nWinNum = len(winNum)
        if nWinNum != 0:
            for n in range(1,nWinNum+1):
                print(n)
                cardResult[lIndex+n] += cardResult[lIndex]
        #cardScore = count_card_points(nWinNum)
        lIndex += 1
        print(cardResult)
        
print(sum(cardResult))
