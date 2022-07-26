import cards as cards
import player as pl
import re  # TODO: get rid of this nonssense

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


class Board:

    # A deck first, with all 52 cards
    deck = cards.Deck()

    # Partnership
    # joined with results of auction?

    # I need a Contract for a board , which is set by

    class Bid:
        def __init__(self):
            self.denomination = None
            self.level = None

    class Trick:
        def __init__(self) -> None:
            self.leader = 0
            self.stack = cards.Stack()

        def compute_winner(self, trick):
            # * highest or trump wins
            # if there's a trump suit , then the highest trump
            # has to be suit of the trick , highest rank wins
            winner = max(trick.stack.cards)

            return winner

        def set_leader(self, player_num):
            #  Winner is the leader
            f = open("leader.txt", "w")
            f.write(str(player_num))
            f.close()

        def play(self, players, trick):
            # take turns starting with leader,  clockwise

            f = open("leader.txt", "r")

            self.leader = f.read()

            turn = int(self.leader)

            for i in range(4):
                # leader takes the first turn
                card_played = players[turn].play()
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
                    print(str(players[winner_index]) +
                          " Wins the Trick\n Now he is leader.")
                # moving turn to next player
                turn = turn + 1
                if turn > 3:
                    turn = 0

            # trick.set_leader ()

    def next_player(num):
        '''keeps us looping through 0,1,2,3'''
        if num >= 4:
            return 0 
        else: 
            return num + 1 

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
        '''shuffle and distribute the cards amongst the players'''
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
        # This is going to set the contract
        # declarer is determined here

        # players take turns to CALL

        # CALL  :
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

        tricks = []

        # Running  13 tricks
        for i in range(13):
            trick = Trick()
            tricks.append(trick)
            trick.play(self)

        for trick in self.tricks:
            # play each trick
            trick.play(self.players, trick)


def main():

    # Sessions has several tables
    # each table has 3 or so boards
    # on each table we have one Rounds

    # First, we got to have four players
    players = []

    # TODO: input names instead of hard code
    players.append(pl.Player('Jim'))
    players.append(pl.Player('Sufi'))
    players.append(pl.Player('Ali'))
    players.append(pl.Player('James'))

    # TODO: introduce partnerships of players , this can last several boards so ... needs to be outta board

    # Getting the number of boards
    boards = []
    number_of_boards = int(input("How many boards would you like to play?"))
    boards.extend(range(1, number_of_boards+1))

    # Play board after board
    for board_num, board in enumerate(boards, start=1):

        print("Playing board: "+str(board_num))

        # Set Dealer & Positions 
        # printing players
        for player_num, player in enumerate(players, start=1):
            print(player_num , player.name)

        # if it's the first board, input the dealer
        if board_num == 1:
         # input a dealer
            while True:
                dealer = int(input("Kindly select a dealer: "))
                    # ensure it's a valid player number
                if dealer not in range(1, 4):
                    print("Enter a valid player number, please!")
                    continue
                else:
                    break
            # assign North to dealer on the first board 
            players[dealer].position = 'N'
            # align all other players on their positions
            next_player = Board.next_player(dealer)
            players[next_player].position = 'E'
            next_player = Board.next_player(next_player)
            players[next_player].position = 'S'
            next_player = Board.next_player(next_player)
            players[next_player].position = 'W'                            
        else: 
        # and then on subsequent boards E,S,W, and looping so on 
            dealer = next_player(dealer) 

 

        # deal the cards
        # board.deal()
        # board.auction()
        # board.play() #
        # Todo : count number of tricks each partnership wins

    # create hands, teams , move from deck to hands ,


if __name__ == '__main__':
    main()
