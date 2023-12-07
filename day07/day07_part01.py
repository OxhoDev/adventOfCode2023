import re
import os

file_name = '/home/rle/Documents/adventOfCode2023/day07/files/example.txt'
#file_name = '/home/rle/Documents/adventOfCode2023/day07/files/data.txt'
result = 0

### Func

def count_unique_cards (handCards):

    uniqueCard = set(handCards)
    #print(handCards)
    handCalc = {}

    for card in uniqueCard:
        #print(card)
        handCalc[card] = (handCards.count(card))
        #print(handCalc)

    return handCalc
### Vars
myLines = open(file_name, 'r').readlines()

cardsValue = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

hands = list(enumerate(myLines))

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

    