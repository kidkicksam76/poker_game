import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades', 'Stars']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck_of_cards = [f"{rank} of {suit}" for suit in suits for rank in ranks]

random.shuffle(deck_of_cards)
print(deck_of_cards)
