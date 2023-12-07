import re
import os

#file_name = '/home/rle/Documents/adventOfCode2023/day07/files/example.txt'
file_name = '/home/rle/Documents/adventOfCode2023/day07/files/data.txt'
#result = 0

### Func

def count_unique_cards (handCards):

    uniqueCard = set(handCards)
    #print(uniqueCard)
    handCalc = {}

    for card in uniqueCard:
        #print(card)
        handCalc[card] = (handCards.count(card))
        #print(handCalc)

    return handCalc

def find_hand_combination (handValue):
    handValue = dict(sorted(handValue.items(), key=lambda item: item[1], reverse=True))
    keys = list(handValue.keys())
    #print(keys)
    score = 0
    
    #Si Joker dans la main
    if 'J' in handValue:
        if handValue['J'] == 5:
            print('JJJJJ, skipping')
        #Si Joker est la carte prédominante
        elif keys.index('J') == 0:
            print('J is first')
            handValue['J'] += int(handValue[keys[1]]) 
        #Sinon on l'ajoute simplement au plus élevé
        else:
            handValue[keys[0]] += int(handValue['J'])
            handValue['J'] = 0
    print(handValue)

    #print(keys)

    match (handValue[keys[0]]):
        case 5:
            print('5 of a kind')
            score += 90
        case 4:
            print('4 of a kind')
            score += 80
        case 3:
            print('3 found, processing')
            if handValue[keys[1]] == 2:
                print('fullHouse')
                score += 70
            else:
                print('3 only')
                score += 50
        case 2:
            print('2 found, searching for another')
            if handValue[keys[1]] == 2:
                print('2 pairs')
                score += 40
            else:
                print('1 pair, no other found')
                score += 20
        case _:
            print('single card found')
            score += 10
    return score

def calculate_hand_sort_value (score, handCards, cardsValue):
    finalValue = str(score)

    for c in handCards:
        finalValue = finalValue + str(cardsValue[c])
    return finalValue

### Vars
myLines = open(file_name, 'r').readlines()

#because we fucking can
cardsValue = {
    'J': 11,
    '2': 12,
    '3': 13,
    '4': 14,
    '5': 15,
    '6': 16,
    '7': 17,
    '8': 18,
    '9': 19,
    'T': 20,
    'Q': 22,
    'K': 23,
    'A': 24,
}

hands = list(enumerate(myLines))
finalList = []

for hand in hands:
    #handID+1 to calculate at the end
    handID = int(hand[0])+1
    hand = hand[1].strip().split(' ')
    #Below declaration can be skipped, it's for clarity
    handCards = hand[0]
    handBid = hand[1]

    print('Cards are ' + handCards + ', pot is ' + handBid)
    handValue = count_unique_cards(handCards)
    print(handValue)

    score = find_hand_combination(handValue)
    handSortValue = calculate_hand_sort_value(score, handCards, cardsValue)
    #print(handSortValue)
    finalList.append([int(handSortValue),handCards,handBid])

    #print(finalList)
    handValue = dict(sorted(handValue.items(), key=lambda item: item[1], reverse=True))
    #sorted(finalList)


result = 0
i = 1
for entry in sorted(finalList):
    #print(i)
    result += int(entry[2]) * i
    #print(int(entry[2]))
    i += 1

print(result)
