import re
import os

#file_name = '/home/rle/Documents/adventOfCode2023/day08/files/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day08/files/data.txt'
result = 0
reLetter = "[^A-Za-z]+"

### Func

def build_dir_dict (directions):
    dirDict = {}
    for line in directions:
        dir = re.split(reLetter, line)
        dirDict[dir[0]] = [dir[1:3]]

    return dirDict

### Vars
myLines = open(file_name, 'r').readlines()

dirSequence = myLines[0].strip()
#dirIterator = iter(dirSequence)

directions = [s.strip() for s in myLines[2:-1]]
#start = directions[0].split('=')[0].strip()
start = 'AAA'

### Main

directions = build_dir_dict(directions)
steps = 0

while start != 'ZZZ':
    #nextSeq = next(dirIterator)
    for c in dirSequence:
        
        match (c):
            case 'L':
                start = directions[start][0][0]
            case 'R':
                start = directions[start][0][1]
        steps += 1
        print(start)
        if start == 'ZZZ':
            print('Start is ZZZ')
            break


print(steps)

## 'AAA': [['BBB', 'CCC']]
#print(directions['AAA'][0])
## returns ['BBB', 'CCC']
#print(directions['AAA'][0][1])
## returns CCC
