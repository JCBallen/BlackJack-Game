from cgitb import handler
import enum
import os
import random

# Clearing the Screen
os.system('cls')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank["rank"]} of {self.suit}'


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
                self.cards.append(Card(suit, rank))  # basicamente estamos creando objetos carta y luego appendeando esos objetos al Deck.cards (queda una lista de objetos)
                                                     # si vieramos el deck se veria ahora algo como esto: ['J of spades', '3 of hearts', Q of clubs, 10 of diamonds, ...]

    def shuffleCards(self):   # revuelve las cartas :V
        if len(self.cards) <= 1:
            return f'Only {len(self.cards)} card(s) in the deck left'
        random.shuffle(self.cards)

    def dealCard(self, quantity):
        cards_dealt = []
        for i in range(quantity):
            # Comprobamos que haya cartas en el deck que sacar, mas que sea 1 :V
            if len(self.cards) < 1:
                return "Deck out of cards"
            # elegimos carta con .pop(), luego la añadimos a la lista de cartas elegidas
            cards_dealt.append(self.cards.pop())
        return cards_dealt

# -------------------------------------------------------------- Test 
deck1 = Deck()
deck2 = Deck()
deck2.shuffleCards()

print('Deck 1:\n', deck1.cards)  # deck1 no esya revuelta (no shuffled)
# print(deck1.cards[1][1]['value'])  # carta indice 1, el dict de ranks, el valor del rank
print('\nDeck 2:\n', deck2.cards)  # deck2 esta revuelta (suffled)


# en el deck hay solo 52 cartas, solo probamos que avise el error, probar con 51, 52 y 53
numCardsDealt = 53
print(f'\nSacamos {numCardsDealt} cartas del Deck 2:\n',
      deck2.dealCard(numCardsDealt))

respond = deck2.shuffleCards()

print('\nShuffle Deck 2:\n', respond, deck2.cards)

# ---------------------------------------------------- Clase hand
class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

# --------------------------------------------------Test
deck5 = Deck()
deck5.shuffleCards()     # Creamos un nuevo mazo y lo revolvemos

hand1 = Hand()
hand1.add_card(deck5.dealCard(2))   # Creamos una mano y le damos 2 cartas

mapaDelDeck = map(lambda n:str(n),deck5.cards)          # Trucoteca para visualizar los objetos dentro de una lista, aprovecahndo el __str__ que le pusimos a Card
print('\nDeck 5:\n',list(mapaDelDeck))                  # ya que si lo vieramos directamente se ve asi: [<main.object>, <main.object>, <main.object>]    

mapaDeHand = map(lambda n:str(n),hand1.cards)
print('\nMano 1:\n',list(mapaDeHand))
