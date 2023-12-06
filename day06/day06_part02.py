import re
#import os

#file_name = '/home/rle/Documents/adventOfCode2023/day06/files/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day06/files/data.txt'
result = 0
reDigits = "[^z0-9]"

### Functions

#def count_max_value (distance):
#    maxDistance = max(distance)

def calculate_result (possibleList):
    result = 1
    for n in possibleList:
        result = result * n
    return result


### Main

myLines = open(file_name, 'r').readlines()
racesTimes = list(enumerate([s for s in re.split(reDigits, myLines[0]) if s != '']))
racesRecords = [s for s in re.split(reDigits, myLines[1]) if s != '']

print(races)
raceBest = []

raceTime = ''
for value in racesTimes:
    raceTime += value[1]
    #print(raceTime)
raceRecord = ''
for value in racesRecords:
    raceRecord = raceRecord + value
    #print(raceRecord)

#for raceTime in (racesTimes):
#    #print(raceTime)
distanceTab = []
possibleRecord = 0

for pressTime in range(0, int(raceTime)+1):
    #print(pressTime)
    speed = pressTime
    distance = speed * (int(raceTime) - pressTime) 
    #print(distance)
    if distance > int(raceRecord):
        possibleRecord += 1
    #distanceTab.append(distance)

#result = calculate_result(raceBest)
print(possibleRecord)
