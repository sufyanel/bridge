from random import sample

# some constants of cards
SUITS = {"c": "Clubs",
         "d": "Diamonds",
         "h": "Hearts",
         "s": "Spades"}

RANKS = {1: "Ace",
         2: "Two",
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
         13: "King"}


class Card:
    '''card: has two attributes, a suit and a rank'''

    def __init__(self, suit, rank):
        '''Creates a card with a valid suit and rank'''
        # checks against the suits and ranks constants, if not in the valid ones, raise exception
        if suit not in SUITS.keys():
            raise Exception("Not a valid suit")
        if rank not in RANKS.keys():
            raise Exception("Not a valid rank")

        # if suit and rank is valid, create the card
        self.suit = suit
        self.rank = rank

    def __str__(self):
        '''Method to turn card to a string'''
        return RANKS[self.rank]+" of "+SUITS[self.suit]


class Stack:
    '''A stack of cards'''
    cards = []

    def __str__(self) -> str:
        '''Returns string of all cards in the stack, by complete name'''
        return ('\n'.join(map(str, self.cards)))

    def shuffle(self):
        '''Shuffles the stack'''
        self.cards = sample(self.cards, 52)

    def sort(self):
        '''Sorts cards in the stack'''
        self.cards = self.cards.sort

class Deck(Stack):
    '''A stack of all 52 cards of 13 unique ones in each of four suits'''

    def __init__(self) -> None:
        '''Initializing all 52 cards'''
        for suit in SUITS.keys():
            for rank in RANKS.keys():
                self.cards.append(Card(suit, rank))


def main():
    deck = Deck()
    print("here's my deck:")
    print(deck)
    print("Shuffling .........................")
    deck.shuffle()
    print(len(deck.cards))


if __name__ == '__main__':
    main()
