import re

file_name = '/home/rle/Documents/adventOfCode2023/day04/files/example.txt'
#file_name = '/home/rle/Documents/adventOfCode2023/day04/files/data.txt'
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

#MAIN
with open(file_name, 'r') as input_file:
    cardResult = [1] * len(input_file.readlines())

    for line in input_file.readlines():
        #print(line)
        #splitResult = re.split(reSChar, line.strip())
        splitResult = ['Card 1', ' 41 48 83 86 17 ', ' 83 86  6 31 17  9 48 53']
        print(splitResult)

        ### SANDBOX

        lotNum = set([int(n) for n in splitResult[1].split(' ') if n != ''])
        playNum = set([int(n) for n in splitResult[2].split(' ') if n != ''])
        #winNum = [n for n in splitResult[2].split(' ')]
        
        winNum = lotNum.intersection(playNum)
        nWinNum = len(winNum)

        for n in range(1,nWinNum+1):
            print(n)

        #cardScore = count_card_points(nWinNum)
        #print(cardScore)
        
print(result)
