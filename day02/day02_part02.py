import re

#file_name = '/home/rle/Documents/adventOfCode2023/day02/files/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day02/files/data.txt'


result = 0
#line = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'



with open(file_name, 'r') as input_file:
    for line in input_file:
        game = line.rstrip('\n').split(':')
        gameResult = game[1]
        gameResult = gameResult.replace(';', ',')

        redTable = []
        greenTable = []
        blueTable = []
        for res in gameResult.split(','):
            drawResult = res.strip().split(' ')
            #print(drawResult)

            match drawResult[1]:
                case 'red':
                    #print('red')
                    redTable.append(int(drawResult[0]))
                    #print(redTable)
                case 'green':
                    #print('green')
                    greenTable.append(int(drawResult[0]))
                case 'blue':
                    #print('blue')
                    blueTable.append(int(drawResult[0]))

        result += max(redTable) * max(greenTable) * max(blueTable)

print(result)
