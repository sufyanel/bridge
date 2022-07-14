import cards as cards

class Board: 

    # A deck first, with all 52 cards 
    deck = cards.Deck()

    class Trick: 
        def __init__(self) -> None:
            self.stack = cards.Stack()

    tricks = Trick() for i in range(13]

    # Creating stacks of cards for each of the four hand positions
    north, east, west, south = (cards.Stack() for i in range(4))

    HANDS = [north, east, west, south]
    TEAMS = [(north, south), (east, west)]

    def deal(self):
        '''shuffle and distribute the cards amongst players'''
        # shuffle the cards 
        self.deck.shuffle()
        # distribute cards amongst all players
        for hand in self.HANDS: 
            for i in range(13): 
                card = self.deck.cards.pop()
                hand.cards.append(card) 
            hand.sort()

    def play(self): 
        '''Players taking turns through the tricks'''
        for trick in self.tricks:
            for hand in self.HANDS: 
                hand.play()
            

def main():
    game = Game()
    game.deal()

    # Getting the number of boards
    boards = []
    # number_of_boards = int(input("How many boards would you like to play?"))
    # boards.extend(range(1, number_of_boards+1))
    for board in boards:
        pass
        # deal
        # create hands, teams , move from deck to hands ,

        # playing boards, one by one


if __name__ == '__main__':
    main()
