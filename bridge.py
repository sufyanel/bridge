import cards as cards

'''
Starting with the dealer and proceeding clockwise around the table, 
each player may bid a level one to seven and denomination (Clubs, Diamonds, Hearts, Spades or No Trump). 
At his turn a player may make a legal bid or he may call Pass or in certain circumstances, double, or in even more limited circumstances, redouble. 
This is called the "auction period" and it ends when three players in a row choose to Pass (or on the initial round, if all four players Pass). 
At the end of the auction period, a "contract" is established and this sets the rules for the "play period" of the game. (I have already coded the auction rules.)


one player is assigned the role of "declarer" by the rules applicable to the auction period and 
the player seated to his immediate left must make an opening lead; that is, choose the first card to be played. 
Each player "plays" a card in turn and when all four players have played a card, that constitutes a "trick." 
There are codable rules to determine what cards may legally be played and to determine which player "wins" the trick. 
The player that wins a trick, is the leader to the immediately subsequent trick. 
This process continues in groups of four card (each a "trick") until all players have played all 13 cards in their hand(s). 
At that point the "hand" or "deal" is complete and we move on to the next hand.

Glossary 
---------
"Board" = deal =  hand

STUCK AT
---------
This process of selecting cards to play
determining which cards may be legally played
which card has won the trick 

In short, I want the code to allow the leader to select any card currently held, 
then test the other three players for legal plays and allow them to make any legal play, 
then assign the status of leader for the next trick to the winner of the current trick, 
and then measure the result (tricks taken) against the number of tricks required.

'''


class Game: # board 

    # A deck first, with all 52 cards
    deck = cards.Deck()

    # Creating stacks of cards for each of the four hand positions
    north, east, west, south = (cards.Stack() for i in range(4))

    # replace hands(stack) with a class called player which has to have play method, choosing leader and is_leader, having name or description. 
    HANDS = [north, east, west, south]
    TEAMS = [(north, south), (east, west)]

    def check_legality(self): 
        # check card against 
        # leader's suite 
        # contract.denomination for trump 

    class Player: 

        def play(self):
 
                # Input card 
                # play the card - pop from player.cards.pop > curent_trick 
                # Check Legality :
                # * Follow the suit/ or trump
                # if illegal, ask to make a valid move 
                # returns the card 

    class Trick:
        def __init__(self) -> None:
            self.stack = cards.Stack()
            
        def compute_winner(self): 
            # self.winner = player 
            # * highest or trump wins
            pass 

        def get_winner(self): 
            return self.winner 

        def set_leader(self): 
            #  Winner is the leader

        def play(self): 
            # take turns starting with leader,  clockwise
                # player.play()
                # trick.compute_winner ()
                # trick.set_leader ()

    tricks = (Trick() for i in range(13))

    def choose_leader(self):
        # Selecting a leader
        while True:
            leader = int(input("Please nominate a leader: 0 North, 1 East, 2 West, 3 South: \n"))
            if leader not in [0,1,2,3]:
                print("Sorry, please enter the digit for the desired player.")
                continue
            else:
                break
        print(self.HANDS[leader]," is the leader")

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

    def auction(self):
        # players take turns to bid
        # Bidding :
        # * take turns clockwise, starting with the dealer
        # * input :
        #   * a pass
        #   * double -- ignore / pass for now 
        #   * redouble -- ignore / pass for now 
        #   * a bid, where inputs are:
        #      * a level (1-7)
        #      * denomination (Trump suit or no trump)
        # auction ends when :
        #   * 4 pass in first round
        #   * 3 pass in a row
        # establish contract : (auction rules in original.py)
        pass

    def play(self):
        '''Players taking turns through the tricks'''
        # loop through tricks (list of card stacks)
        # play each trick (trick.play 


        for trick in self.tricks:
            for hand in self.HANDS:
                hand.play()


def main():

    # Getting the number of boards
    boards = []
    # number_of_boards = int(input("How many boards would you like to play?"))
    # boards.extend(range(1, number_of_boards+1))
    for board in boards:
        pass
        # deal
        # create hands, teams , move from deck to hands ,

        # playing boards, one by one

    game = Game()
    game.deal()
    game.choose_leader()


if __name__ == '__main__':
    main()
