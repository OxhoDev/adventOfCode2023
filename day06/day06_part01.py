import re
#import os

file_name = '/home/rle/Documents/adventOfCode2023/day06/files/example.txt'
#file_name = '/home/rle/Documents/adventOfCode2023/day06/files/data.txt'
result = 0
reDigits = "[^z0-9]"

### Functions

def count_max_value (distance):
    print('WIP')


### Main

myLines = open(file_name, 'r').readlines()
races = [s for s in re.split(reDigits, myLines[0]) if s != '']

print(races)

for r in (races):
    distance = []
    for t in range(0, int(r)+1):
        print(t)
        speed = t
        d = r - t       
        distance.append(d)
    
    #maxDistance = count_max_value(distance)


#'''
#Pour chaque course
#    Pour chaque milisec
#        on calcule la distance pour chaque input
#        on stock dans un tableau []


#        function: on compte le nombre de fois qu'on trouve le max[ditance]
#            on renvoit
#'''