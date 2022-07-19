import cards as cards
import re

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


class Player:

    def __init__(self,p_position):
        self.suit1 = None
        self.stack = cards.Stack()
        self.position = p_position

    def __str__(self):
        return self.position


    def play(self,players,co):
        # Input card
        print(co)
        card = players[self.position].stack.cards
        print(str(players[self.position])+" You have these cards.")
        print(card)
        player_card = input("Please enter your card "+str(players[self.position])+":")
        # Check Legality :
        digit = re.findall(r'\d+', player_card)
        player_card = (player_card[0], int(digit[0]))
        if co == 0:
            f = open("suit.txt", "w")
            f.write(player_card[0])
            f.close()

        f = open("suit.txt", "r")
        self.suit1 = f.read()
        if self.position != 0:
            # * Follow the suit/ or trump
            if self.suit1 != player_card[0]:
                # if illegal, ask to make a valid move
                print("Please enter a valid card.")
                self.play(players,co)
        # returns the card
        return player_card









class Board:

    # A deck first, with all 52 cards
    deck = cards.Deck()

    # Creating four players
    players = []
    players.append(Player('North'))
    players.append(Player('East'))
    players.append(Player('South'))
    players.append(Player('West'))


    class Trick:
        def __init__(self) -> None:
            self.leader = 0
            self.stack = cards.Stack()

        def compute_winner(self,trick):
            # * highest or trump wins
            winner = max(trick.stack.cards)
            return winner


        def set_leader(self, player_num):
            #  Winner is the leader
            f = open("leader.txt", "w")
            f.write(str(player_num))
            f.close()

        def play(self,players,trick):
            # take turns starting with leader,  clockwise


            f = open("leader.txt", "r")
            self.leader = f.read()
            turn = int(self.leader)
            for i in range(4):
                # leader takes the first turn
                card_played = Player(turn).play(players,i)
                # play the card - pop from player.cards.pop > curent_trick
                card = players[i].stack.cards
                input_card = [i for i in card if card_played == i]
                print("--input card--")
                print(input_card)
                if input_card:
                    card.remove(input_card[0])
                    trick.stack.cards.append(input_card[0])
                    print(trick.stack.cards)
                if i == 3:
                   print(trick.stack.cards)
                   winner = self.compute_winner(trick)
                   winner_index = trick.stack.cards.index(winner)
                   self.set_leader(winner_index)
                   print(str(players[winner_index]) + " Wins the Trick\n Now he is leader.")
                # moving turn to next player
                turn = turn + 1
                if turn > 3:
                    turn = 0

            # trick.set_leader ()


    # Generating 13 tricks
    tricks = []
    for i in range(13):
        tricks.append(Trick())

    def check_legality(self):
        # check card against 
        # leader's suite 
        # contract.denomination for trump
        pass

    # def choose_leader(self):
    #     # Selecting a leader
    #     while True:
    #         leader = int(input("Please nominate a leader: \n"+self.players))
    #         if leader not in [0,1,2,3]:
    #             print("Sorry, please enter the digit for the desired player.")
    #             continue
    #         else:
    #             break

    def deal(self):
        '''shuffle and distribute the cards amongst players'''
        # shuffle the cards
        self.deck.shuffle()
        # distribute cards amongst all players
        for player in self.players:
            for i in range(13):
                card = self.deck.cards.pop()
                player.stack.cards.append(card)
            player.stack.cards.sort()
            # print(player)


        # player = Player
        # player.players(hand)



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
        # loop through tricks
        # print(self.player)

        for trick in self.tricks:
            # play each trick
            trick.play(self.players,trick)

def main():

    # Getting the number of boards
    # boards = []
    # number_of_boards = int(input("How many boards would you like to play?"))
    # boards.extend(range(1, number_of_boards+1))
    # for board in boards:
    #     pass
        # deal
        # create hands, teams , move from deck to hands ,

        # playing boards, one by one

    board = Board()
    board.deal()
    # board.choose_leader()
    board.play()

if __name__ == '__main__':
    main()
