import re

#file_name = '/home/rle/Documents/adventOfCode2023/day02/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day02/data.txt'

mainConfig = {
    'red': 12,
    'green': 13,
    'blue': 14
}

result = 0

with open(file_name, 'r') as input_file:
    for line in input_file:
        #print(line)
        game = line.rstrip('\n').split(':')
        print(game)
        #gameID = re.findall('d\', game[0])
        gameID = game[0].split(' ')[-1]
        
        gameResult = game[1]

        isCorrect = True
        gameResult = gameResult.replace(';', ',')
        for res in gameResult.split(','):
            #print(isCorrect)
            drawResult = res.split(' ')
            #print(drawResult[1])
            #print(mainConfig[drawResult[2]])
            if int(drawResult[1]) > mainConfig[drawResult[2]]:
                isCorrect = False
                break
        print(isCorrect)
        if isCorrect is True:
            print(gameID[0])
            result += int(gameID)

print(result)
