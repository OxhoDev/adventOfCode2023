import re

#file_name = '/home/rle/Documents/adventOfCode2023/day01/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day01/data.txt'
result = 0

# Exo 1
with open(file_name, 'r') as input_file:
    for line in input_file:
        #print(line.strip())
        lineResult = re.findall('\d', line)
        calib = lineResult[0] + lineResult[-1]
        result += int(calib)
        print(calib)
        #print(lineResult[0]
print(result)
