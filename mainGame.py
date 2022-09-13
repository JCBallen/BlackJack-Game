
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

    def dealCard(self, quantity=1):  # defaut entrega 1 carta
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
print('Deck 1:\n', deck1.cards[0], '(Solo mostramos 1 carta del deck)\n')
print('\nDeck 2:\n', deck2.cards)  # deck2 esta revuelta (suffled)


# en el deck hay solo 52 cartas, solo probamos que avise el error, probar con 51, 52 y 53
numCardsDealt = 53
print(f'\nSacamos {numCardsDealt} cartas del Deck 2:\n',
      deck2.dealCard(numCardsDealt))

# solo recibe algo cuando hay 1 o menos cartas en el deck
respond = deck2.shuffleCards()

print('\nShuffle Deck 2:\n', respond, deck2.cards)

# ---------------------------------------------------- Clase hand


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        # este valor es la suma de las cartas, cuanto vale su mano
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def get_value(self):     # suma las cartas
        self.value = 0
        hasAce = False

        for card in self.cards:
            if card.rank['rank'] == 'A':
                hasAce = True                      # avisa si leyo una A
            # se suma normal, luego lo arreglamos
            self.value += card.rank['value']

        if hasAce and self.value > 21:       # si existia una A y se pasa de 21, hacemos que solo valga 1, restandole 10
            self.value -= 10

        return self.value                    # retorna el valor de la suma

    def is_blackjack(self):
        val = self.get_value()
        return True if val == 21 else False

    def display(self, show_all_dealer_cards=False):
        # Ojo que aqui hay, FStrings, Ternary Operators, Triple Quotes
        # Los triple quotes permiten que su interior este con cualquier indentacion
        print(f'''
{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            # Recordar que el dealer tiene una carta oculta y la otra visible
            # si usamos '\' backslash al final de una linea esta continuara en la siguiente
            # para no tener lineas tan largas
            if index == 0 and self.dealer \
                    and not show_all_dealer_cards and not self.is_blackjack():
                print("*hidden*")
            else:
                print(card)

        if not self.dealer:
            print('\nValue:', self.get_value())


# --------------------------------------------------Test
deck5 = Deck()
deck5.shuffleCards()     # Creamos un nuevo mazo y lo revolvemos

hand1 = Hand()
# Creamos una mano y le damos 2 cartas (asi como en blackjack)
hand1.add_card(deck5.dealCard(2))

# Trucoteca para visualizar los objetos dentro de una lista, aprovecahndo el __str__ que le pusimos a Card
# ya que si lo vieramos directamente se ve asi: [<main.object>, <main.object>, <main.object>]
mapaDelDeck = map(lambda n: str(n), deck5.cards)
# basicamente tomamos la carta y le aplicamos el str(), funciona por el metodo __str__ de la clase Card
print('\nDeck 5:\n', list(mapaDelDeck))

hand1.display()

# ---------------------------------------------- GAME CLASS


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        # Queremos asegurarnos que ingrese un valor numerico mayor a 0
        while games_to_play <= 0:
            try:
                games_to_play = int(
                    input('How many games do you wanna play? '))           # este lanza error si es string
                if games_to_play < 0:
                    # este lanza error si es negativo
                    raise
            except Exception as e:
                print('Must be a positive integer')

        while game_number < games_to_play:
            game_number += 1
            main_deck = Deck()
            main_deck.shuffleCards()   # Creamos y revolvemos las cartas

            player_hand = Hand()      # Creamos las manos
            dealer_hand = Hand(True)  # Seteamos el dealer to true

            # Repartimos 2 cartas a cada uno
            player_hand.add_card(main_deck.dealCard(2))
            dealer_hand.add_card(main_deck.dealCard(2))

            print()
            print('*' * 30)
            print(f'Game {game_number} of {games_to_play}')
            print('*' * 30)
            player_hand.display()
            dealer_hand.display()

            # Verificamos que no haya un ganador desde ya la primera reparticion
            if self.check_winner(player_hand, dealer_hand):
                continue

            # Si no se dio ganador de primeras procedemos al 'Hit' o 'Stand'
            choice = ''

            while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                # Preguntamos que quiere hacer
                choice = input('Hit or Stand?').lower()
                print()
                while choice not in ['s', 'h', 'stand', 'hit']:
                    choice = input(
                        "Type 's' or 'h' or 'stand' or 'hit'").lower()  # Por si se equivoco, le mostramos como debe escribir las opciones
                    print()
                if choice in ['hit', 'h']:
                    # en el metodo dealCard pusimos default 1
                    player_hand.add_card(main_deck.dealCard())
                    player_hand.display()

            # Verificamos si hay un ganador ahora
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:                       # el dealer tiene que llegar a 17
                dealer_hand.add_card(main_deck.dealCard())
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            # Verificamos si hay un ganador ahora
            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your Hand:", player_hand_value)
            print("Dealer's Hand:", dealer_hand_value)

            # Aqui ya deberia haber un ganador asi que no lo ponemos en if y enviamos el game_over=True
            self.check_winner(player_hand, dealer_hand, True)

        print('\nThank for playing!')

    def check_winner(self, player_hand, dealer_hand):
        if player_hand.get_value() > 21:
            print('You Busted, Dealer Wins! 😥')
            return True
        if dealer_hand.get_value() > 21:
            print('Dealer Busted, You Win! 😎')
            return True
        if player_hand.get_value() == 21 and dealer_hand.get_value() == 21:
            print("It's a tie!")
            return True
        if player_hand.is_blackjack():
            print("You have a BlackJack, You Win 😎")
            return True
        if dealer_hand.is_blackjack():
            print("Dealer has BlackJack, Dealer Wins! 😥")
            return True
        if player_hand.get_value() > dealer_hand.get_value() and player_hand.get_value() <= 21:
            print('You Win! 😎')
            return True
        if player_hand.get_value() == dealer_hand.get_value():
            print("It's a tie!")
            return True
        if dealer_hand.get_value() > player_hand.get_value() and dealer_hand.get_value() <= 21:
            print('Dealer Win! 😥')
            return True

        return False

    def final_results(self, player_hand, dealer_hand):
        print("Final Results")
        print("Your Hand:", player_hand.get_value())
        print("Dealer's Hand:", dealer_hand.get_value())


g = Game()
g.play()
