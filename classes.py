import os
import random

# Clearing the Screen
os.system('cls')


class Deck:
    def __init__(self):
        self.cards = []
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
            for rank in ranks:
                self.cards.append([suit, rank])

    def shuffleCards(self):   # revuelve las cartas :V
        random.shuffle(self.cards)

    def dealCard(self, quantity):
        cards_dealt = []
        for i in range(quantity):
            # elegimos carta con .pop(), luego la añadimos a la lista de cartas elegidas
            cards_dealt.append(self.cards.pop())
        return cards_dealt


deck1 = Deck()
deck2 = Deck()
deck2.shuffleCards()

print('Deck 1:', deck1.cards)  # deck1 no esya revuelta (no shuffled)
# print(deck1.cards[1][1]['value'])  # carta indice 1, el dict de ranks, el valor del rank
print('Deck 2:', deck2.cards)  # deck2 esta revuelta (suffled)
