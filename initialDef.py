import os
import random

# Clearing the Screen
os.system('cls')


cards = []
suits = ['hearts', 'diamonds', 'spades', 'clubs']
ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# rank = 'k'
# value = 10
# print(f'Your card is {rank} of {suits[1]} with value {value}')

# suits.append('snakes')
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


shuffleCards(cards)
cards_picked = dealCard(cards, 3)

# Miramos/chequeamos que efectivamente las cartas elejidas se hayan "sacado" fuera del deck
check_if_not_in_deck = map(lambda n: n in cards_picked, cards)   # va preguntando por cada carta si existe esa misma en las pickeadas (True si coincide una carta de las pickeadas con el deck)
print('Correctamente salieron de la baraja' if any(check_if_not_in_deck) == False else 'Hay cartas repetidas en la baraja') 
# print(check_if_not_in_deck)
print(cards_picked)

# card1, card2, card3 = cards_picked    # desacoplamos la lista en variables individuales
cardTaken = cards_picked[1]     # tomamos arbitrariamente la carta 2
rank_card_taken = cardTaken[0]

# Asignamos los valores a las cartas A, J, Q, K
if rank_card_taken == 'A':
    value = 11
elif rank_card_taken == 'J' or rank_card_taken == 'Q' or rank_card_taken == 'K':
    value = 10
else:
    value = rank_card_taken

# rank_dict = {
#     'A': 1,
#     2: 2,
#     3: 3,
#     4: 4,
#     5: 5,
#     6: 6,
#     7: 7,
#     8: 8,
#     9: 9,
#     10: 10,
#     'J': 10,
#     'Q': 10,
#     'K': 10
# }


print('Value of Card 2:', value)
