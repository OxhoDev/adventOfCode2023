import re
#import os

file_name = '/home/rle/Documents/adventOfCode2023/day06/files/example.txt'
#file_name = '/home/rle/Documents/adventOfCode2023/day06/files/data.txt'
result = 0
reDigits = "[^z0-9]"

myLines = open(file_name, 'r').readlines()

races = [s for s in re.split(reDigits, myLines[0]) if s != '']

print(races)