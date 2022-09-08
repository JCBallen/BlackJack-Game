import os
import random

# Clearing the Screen
os.system('cls')


cards = []
suits = ['hearts', 'diamonds', 'spades', 'clubs']
ranks = [
    {'rank': 'A', 'value': 11},
    {'rank': '2', 'value': 2},
    {'rank': '3', 'value': 3},
    {'rank': '4', 'value': 4},
    {'rank': '5', 'value': 5},
    {'rank': '6', 'value': 6},
    {'rank': '7', 'value': 7},
    {'rank': '8', 'value': 8},
    {'rank': '9', 'value': 9},
    {'rank': '10', 'value': 10},
    {'rank': 'J', 'value': 10},
    {'rank': 'Q', 'value': 10},
    {'rank': 'K', 'value': 10}
]


for suit in suits:
    print(suit)


for suit in suits:
    for rank in ranks:
        cards.append([rank, suit])

# print(cards)
# print(list(enumerate(cards)))
# random.shuffle(cards)


def shuffleCards(deck):   # revuelve las cartas :V
    random.shuffle(deck)


def dealCard(deck, quantity):
    cards_dealt = []
    for i in range(quantity):
        # elegimos carta con .pop(), luego la añadimos a la lista de cartas elegidas
        cards_dealt.append(deck.pop())
    return cards_dealt
