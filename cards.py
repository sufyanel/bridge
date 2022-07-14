from random import sample

# some constants of cards
SUITS = {"c": "Clubs",
         "d": "Diamonds",
         "h": "Hearts",
         "s": "Spades"}

RANKS = {2: "Two",
         3: "Three",
         4: "Four",
         5: "Five",
         6: "Six",
         7: "Seven",
         8: "Eight",
         9: "Nine",
         10: "Ten",
         11: "Jack",
         12: "Queen",
         13: "King",
         14: "Ace"}

class Stack:
    '''A stack of cards'''

    def __init__(self):
        self.cards = []

    def __str__(self):
        '''Returns string of all cards in the stack, by complete name'''
        # getting full names of ranks and suits from the constant RANKS & SUITS dictionaries,
        # lambda function formats them pretty, like Eight of Spades
        # using the join, all list is converted to a single string with New line character: '\n'
        return '\n'.join(map(lambda card: RANKS[card[1]]+' of '+SUITS[card[0]], self.cards))

    def shuffle(self):
        '''Shuffles the stack'''
        self.cards = sample(self.cards, len(self.cards))

    def sort(self):
        '''Sorts cards in the stack'''
        # Sort Rank wise 
        self.cards.sort(key=lambda c:c[1])
        # Sort Suit Wise 
        self.cards.sort(key=lambda c:c[0])

class Deck(Stack):
    '''A stack of all 52 cards of 13 unique ones in each of four suits'''

    def __init__(self) -> None:
        '''Initializing all 52 cards'''
        super().__init__()

        for suit in SUITS.keys():
            for rank in RANKS.keys():
                self.cards.append((suit, rank))

