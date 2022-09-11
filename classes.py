from ast import Return
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
                # basicamente estamos creando objetos carta y luego appendeando esos objetos al Deck.cards (queda una lista de objetos)
                self.cards.append(Card(suit, rank))
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

# NOTA: se ven como listas de objetos, si se desea "ver claramente" abajo hay un ejemplo de como visualizarlo
# deck1 no esta revuelta (no shuffled) (ya que es una lista de objetos, solo podemos ver 1 objeto bien a la vez, abajo hay un truco para ver todos)
print('Deck 1:\n', deck1.cards[0])
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

    def calculate_value(self):     # suma las cartas
        self.value = 0
        hasAce = False

        for card in self.cards:
            if card.rank['rank'] == 'A':
                hasAce = True                      # avisa si leyo una A
            self.value += card.rank['value']       # se suma normal, luego lo arreglamos

        if hasAce and self.value > 21:       # si existia una A y se pasa de 21, hacemos que solo valga 1, restandole 10
            self.value -= 10

    def get_value(self):
        self.calculate_value()                # retorna el valor de las cartas primero llamando a calculate_value, y ahi si
        return self.value

    def is_blackjack(self):
        self.get_value()
        if self.value == 21:
            return "IT'S A BLACKJACK"
        return "It's not a BlackJack"


# --------------------------------------------------Test
deck5 = Deck()
deck5.shuffleCards()     # Creamos un nuevo mazo y lo revolvemos

hand1 = Hand()
# Creamos una mano y le damos 2 cartas (por ser blackjack)
hand1.add_card(deck5.dealCard(2))

# Trucoteca para visualizar los objetos dentro de una lista, aprovecahndo el __str__ que le pusimos a Card
mapaDelDeck = map(lambda n: str(n), deck5.cards)
# ya que si lo vieramos directamente se ve asi: [<main.object>, <main.object>, <main.object>]
print('\nDeck 5:\n', list(mapaDelDeck))

mapaDeHand = map(lambda n: str(n), hand1.cards)
print('\nMano 1:\n', list(mapaDeHand))

sumOfHand = hand1.get_value()
print(f'The sum of the cards is {sumOfHand}')
print(hand1.is_blackjack())
