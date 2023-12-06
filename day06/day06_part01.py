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
racesBest = []

for raceTime in (racesTimes):
    #print(raceTime)
    distanceTab = []
    possibleRecord = 0

    for pressTime in range(0, int(raceTime[1])+1):
        #print(pressTime)
        speed = pressTime
        distance = speed * (int(raceTime[1]) - pressTime) 
        #print(distance)
        if distance > int(racesRecords[raceTime[0]]):
            possibleRecord += 1
        #distanceTab.append(distance)
    #print(possibleRecord)
    
    racesBest.append(possibleRecord)

print(racesBest)

result = calculate_result(racesBest)
print(result)

#'''
#Pour chaque course
#    Pour chaque milisec
#        on calcule la distance pour chaque input
#        on stock dans un tableau []


#        function: on compte le nombre de fois qu'on trouve le max[ditance]
#            on renvoit
#'''