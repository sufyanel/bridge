import cards as cards 

class Player:

    def __init__(self, p_name):
        self.name = p_name
        self.stack = cards.Stack()
        self.position = None

    # def __str__(self):
    #     return self.name 

    def play(self, players, co):
        # Input card
        print(co)  # TODO  what is CO ????
        card = players[self.position].stack.cards
        print(str(players[self.position])+" You have these cards.")
        print(card)
        player_card = input("Please enter your card " +
                            str(players[self.position])+":")
        # Check Legality :
        #   * you must follow suit if you have it
        #   * if you don't have it, you may play any card

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
                self.play(players, co)
        # returns the card
        return player_card
