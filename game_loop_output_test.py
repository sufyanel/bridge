from typing import Any

# a simple turn taking game with four players and continuation and end rules
dealer = ""
x = 1

Boards = []
number_of_boards = int(input("How many boards would you like to play? "))
Boards.extend(range(1, number_of_boards + 1))

# for x in Boards:
while x < number_of_boards + 1:
    print()
    print("Board Number:", x)
    if (x % 16) == 1:
        dealer = "n"
        vul = "-"
    if (x % 16) == 2:
        dealer = "e"
        vul = "n"
    if (x % 16) == 3:
        dealer = "s"
        vul = "e"
    if (x % 16) == 4:
        dealer = "w"
        vul = "b"
    if (x % 16) == 5:
        dealer = "n"
        vul = "n"
    if (x % 16) == 6:
        dealer = "e"
        vul = "e"
    if (x % 16) == 7:
        dealer = "s"
        vul = "b"
    if (x % 16) == 8:
        dealer = "w"
        vul = "-"
    if (x % 16) == 9:
        dealer = "n"
        vul = "e"
    if (x % 16) == 10:
        dealer = "e"
        vul = "b"
    if (x % 16) == 11:
        dealer = "s"
        vul = "-"
    if (x % 16) == 12:
        dealer = "w"
        vul = "n"
    if (x % 16) == 13:
        dealer = "n"
        vul = "b"
    if (x % 16) == 14:
        dealer = "e"
        vul = "-"
    if (x % 16) == 15:
        dealer = "s"
        vul = "n"
    if (x % 16) == 0:
        dealer = "w"
        vul = "e"
    print("Dealer:", dealer, "Vulnerability:", vul)

    # def positions (/dealer):
    if dealer == "n":
        second = "e"
        third = "s"
        fourth = "w"
    if dealer == "e":
        second = "s"
        third = "w"
        fourth = "n"
    if dealer == "s":
        second = "w"
        third = "n"
        fourth = "e"
    if dealer == "w":
        second = "n"
        third = "r"
        fourth = "s"

    from random import sample

    # Create empty lists
    Cards = []

    # Value to begin and end for a complete deck
    Cards.extend(range(1, 53))

    # Randomize the complete deck
    rand_cards = sample(Cards, 52)

    # Select and sort the hands
    dealer_cards = rand_cards[0:13]
    dealer_cards.sort(reverse=True)

    second_player_cards = rand_cards[13:26]
    second_player_cards.sort(reverse=True)

    third_player_cards = rand_cards[26:39]
    third_player_cards.sort(reverse=True)

    fourth_player_cards = rand_cards[39:52]
    fourth_player_cards.sort(reverse=True)
    card_dict = {52: 'SA', 51: 'SK', 50: 'SQ', 49: 'SJ', 48: 'ST', 47: 'S9', 46: 'S8', 45: 'S7', 44: 'S6',
                 43: 'S5', 42: 'S4', 41: 'S3', 40: 'S2', 39: 'HA', 38: 'HK', 37: 'HQ', 36: 'HJ', 35: 'HT',
                 34: 'H9', 33: 'H8', 32: 'H7', 31: 'H6', 30: 'H5', 29: 'H4', 28: 'H3', 27: 'H2', 26: 'DA',
                 25: 'DK', 24: 'DQ', 23: 'DJ', 22: 'DT', 21: 'D9', 20: 'D8', 19: 'D7', 18: 'D6', 17: 'D5',
                 16: 'D4', 15: 'D3', 14: 'D2', 13: 'CA', 12: 'CK', 11: 'CQ', 10: 'CJ', 9: 'CT', 8: 'C9',
                 7: 'C8', 6: 'C7', 5: 'C6', 4: 'C5', 3: 'C4', 2: 'C3', 1: 'C2'}

    with open("output.txt", "a") as tst:
        tst.write("&" + dealer + "=")
        tst.close()
        for c in dealer_cards:
            print(card_dict.get(c), end=", ")
            with open("output.txt", "a") as tst:
                tst.write("".join(card_dict.get(c)))
                tst.close()
    print()
    with open("output.txt", "a") as tst:
        tst.write("&" + second + "=")
        tst.close()
        for c in second_player_cards:
            print(card_dict.get(c), end=", ")
            with open("output.txt", "a") as tst:
                tst.write("".join(card_dict.get(c)))
                tst.close()
    print()
    with open("output.txt", "a") as tst:
        tst.write("&" + third + "=")
        tst.close()
        for c in third_player_cards:
            print(card_dict.get(c), end=", ")
            with open("output.txt", "a") as tst:
                tst.write("".join(card_dict.get(c)))
                tst.close()
    print()
    with open("output.txt", "a") as tst:
        tst.write("&" + fourth + "=")
        tst.close()
        for c in fourth_player_cards:
            print(card_dict.get(c), end=", ")
            with open("output.txt", "a") as tst:
                tst.write("".join(card_dict.get(c)))
                tst.close()
    print()
    print()

    auction = []
    bids = ["1C", "1D", "1H", "1S", "1N", "2C", "2D", "2H", "2S", "2N", "3C", "3D", "3H", "3S", "3N", "4C", "4D",
            "4H", "4S", "4N", "5C", "5D", "5H", "5S", "5N", "6C", "6D", "6H", "6S", "6N", "7C", "7D", "7H", "7S",
            "7N"]
    calls = ["P"]
    contract = ()
    declarer: ""
    dealer_level = 0
    dealer_denomination = ""
    dealer_call = ()
    dealer_third_bids = {}
    dealer_third_declarer = ""
    denomination = ""
    fourth_player_call = ()
    i = 0
    last_bid = ""
    last_bidder = ""
    legal_bids = bids
    legal_calls = legal_bids + calls
    offered_contract = ""
    opening_leader = ""
    passes = 0
    second_fourth_bids = {}
    second_fourth_declarer = ""
    second_player_call = ()
    third_player_call = ()

    # iterating through the players for a single auction

    while i < 10000:
        i = i + 1
        #with open("output.txt", "a") as tst:
         #   tst.write("\n")
          #  tst.close()

        # dealer acts

        # testing user input for validity

        legal_calls = legal_bids + calls
        if (fourth_player_call in bids) or (
                second_player_call in bids and third_player_call == "P" and fourth_player_call == "P"):
            legal_calls.append("X")
        if (fourth_player_call == "X") or (
                second_player_call == "X" and third_player_call == "P" and fourth_player_call == "P"):
            legal_calls.append("XX")
        dealer_call = input(dealer + " calls: ")
        while dealer_call not in legal_calls:
            print(
                "That is not a valid call. Please enter your call in the form of <number><denomination> (for example: 4H).")
            dealer_call = input(dealer + " calls: ")
        while dealer_call not in legal_bids and dealer_call not in legal_calls:
            print(
                "That bid is insufficient. Please enter a bid of a higher ranked denomination at the same level or any denomination at a higher level.")
            dealer_call = input(dealer + " calls: ")
        print(dealer_call)
        auction.append(dealer_call)

        # assessing effect of dealer's action on state of the auction

        if dealer_call == "P":
            passes = passes + 1
        if dealer_call not in bids:
            legal_bids = bids
        if dealer_call != "P":
            passes = 0
        if dealer_call == "X":
            offered_contract = last_bid + "X"
        if dealer_call == "XX":
            offered_contract = last_bid + "XX"
        if dealer_call in bids:
            last_bid = dealer_call
            legal_bids = bids[bids.index(dealer_call) + 1:36]
            offered_contract = last_bid
            if dealer_call[1] not in dealer_third_bids:
                dealer_third_bids.update({dealer_call[1]: dealer})
                declarer = dealer_third_bids.get(dealer_call[1])
            if dealer_call[1] in dealer_third_bids:
                declarer = dealer_third_bids[dealer_call[1]]

        # reporting the effects of dealer's action on the auction

        if passes == 3:
            contract = offered_contract
            level = (int(contract[0]))
            denomination = (contract[1])
            print("The auction period is ended. The contract is " + contract + " by " + declarer + ".")
            print("The auction was", auction)
            with open("output.txt", "a") as tst:
                tst.write("&a=" + "".join(auction))
                tst.close()
            if declarer == "n":
                opening_leader = "e"
            elif declarer == "e":
                opening_leader = "s"
            elif declarer == "s":
                opening_leader = "w"
            elif declarer == "w":
                opening_leader = "n"
            print("Opening Leader: " + opening_leader)
            print()
            x = x + 1
            break

        # second player acts

        # testing user input for validity

        legal_calls = legal_bids + calls
        if (dealer_call in bids) or (third_player_call in bids and fourth_player_call == "P" and dealer_call == "P"):
            legal_calls.append("X")
        if (dealer_call == "X") or (third_player_call == "X" and fourth_player_call == "P" and dealer_call == "P"):
            legal_calls.append("XX")
        second_player_call = input(second + " calls: ")
        while second_player_call not in legal_calls:
            print(
                "That is not a valid call. Please enter your call in the form of <number><denomination> (for example: 4H).")
            second_player_call = input(second + " calls: ")
        while second_player_call not in legal_bids and second_player_call not in legal_calls:
            print(
                "That bid is insufficient. Please enter a bid of a higher ranked denomination at the same level or any denomination at a higher level.")
            second_player_call = input(second + " calls: ")
        print(second_player_call)
        auction.append(second_player_call)

        # assessing effect of second player's action on state of the auction

        if second_player_call == "P":
            passes = passes + 1
        if second_player_call not in bids:
            legal_bids = bids
        if second_player_call != "P":
            passes = 0
        if second_player_call == "X":
            offered_contract = last_bid + "X"
        if second_player_call == "XX":
            offered_contract = last_bid + "XX"
        if second_player_call in bids:
            last_bid = second_player_call
            legal_bids = bids[bids.index(second_player_call) + 1:36]
            offered_contract = last_bid
            if second_player_call[1] not in second_fourth_bids:
                second_fourth_bids.update({second_player_call[1]: second})
                declarer = second_fourth_bids.get(second_player_call[1])
            if second_player_call[1] in second_fourth_bids:
                declarer = second_fourth_bids[second_player_call[1]]

        # reporting the effects of second player's action on the auction

        if passes == 3:
            contract = offered_contract
            level = (int(contract[0]))
            denomination = (contract[1])
            print("The auction period is ended. The contract is " + contract + " by " + declarer + ".")
            print("The auction was", auction)
            with open("output.txt", "a") as tst:
                tst.write("&a=" + "".join(auction))
                tst.close()
            if declarer == "n":
                opening_leader = "e"
            elif declarer == "e":
                opening_leader = "s"
            elif declarer == "s":
                opening_leader = "w"
            elif declarer == "w":
                opening_leader = "n"
                print("Opening Leader: " + opening_leader)
                print()
            x = x + 1
            break

        # third player acts

        # testing user input for validity

        legal_calls = legal_bids + calls
        if (second_player_call in bids) or (
                fourth_player_call in bids and dealer_call == "P" and second_player_call == "P"):
            legal_calls.append("X")
        if (second_player_call == "X") or (
                fourth_player_call == "X" and dealer_call == "P" and second_player_call == "P"):
            legal_calls.append("XX")
        third_player_call = input(third + " calls: ")
        while third_player_call not in legal_calls:
            print(
                "That is not a valid call. Please enter your call in the form of <number><denomination> (for example: 4H).")
            third_player_call = input(third + " calls: ")
        while third_player_call not in legal_bids and third_player_call not in legal_calls:
            print(
                "That bid is insufficient. Please enter a bid of a higher ranked denomination at the same level or any denomination at a higher level.")
            third_player_call = input(third + " calls: ")
        print(third_player_call)
        auction.append(third_player_call)

        # assessing effect of third player's action on state of the auction

        if third_player_call == "P":
            passes = passes + 1
        if third_player_call not in bids:
            legal_bids = bids
        if third_player_call != "P":
            passes = 0
        if third_player_call == "X":
            offered_contract = last_bid + "X"
        if third_player_call == "XX":
            offered_contract = last_bid + "XX"
        if third_player_call in bids:
            last_bid = third_player_call
            legal_bids = bids[bids.index(third_player_call) + 1:36]
            offered_contract = last_bid
            if third_player_call[1] not in dealer_third_bids:
                dealer_third_bids.update({third_player_call[1]: third})
                declarer = dealer_third_bids.get(third_player_call[1])
            if third_player_call[1] in dealer_third_bids:
                declarer = dealer_third_bids[third_player_call[1]]

        # reporting the effects of third player's action on the auction

        if passes == 3 and i > 1:
            contract = offered_contract
            level = (int(contract[0]))
            denomination = (contract[1] + " by " + declarer)
            print("The auction period is ended. The contract is " + contract + " by " + declarer + ".")
            print("The auction was", auction)
            with open("output.txt", "a") as tst:
                tst.write("&a=" + "".join(auction))
                tst.close()
            if declarer == "n":
                opening_leader = "e"
            elif declarer == "e":
                opening_leader = "s"
            elif declarer == "s":
                opening_leader = "w"
            elif declarer == "w":
                opening_leader = "n"
            print("Opening Leader: " + opening_leader)
            print()
            x = x + 1
            break

        # fourth player acts

        # testing user input for validity

        legal_calls = legal_bids + calls
        if (third_player_call in bids) or (
                dealer_call in bids and second_player_call == "P" and third_player_call == "P"):
            legal_calls.append("X")
        if (third_player_call == "X") or (
                dealer_call == "X" and second_player_call == "P" and third_player_call == "P"):
            legal_calls.append("XX")
        fourth_player_call = input(fourth + " calls: ")
        while fourth_player_call not in legal_calls:
            print(
                "That is not a valid call. Please enter your call in the form of <number><denomination> (for example: 4H).")
            fourth_player_call = input(fourth + " calls: ")
        while fourth_player_call not in legal_bids and fourth_player_call not in legal_calls:
            print(
                "That bid is insufficient. Please enter a bid of a higher ranked denomination at the same level or any denomination at a higher level.")
            fourth_player_call = input(fourth + " calls: ")
        print(fourth_player_call)
        auction.append(fourth_player_call)

        # assessing effect of fourth player's action on state of the auction

        if fourth_player_call == "P":
            passes = passes + 1
            if passes == 4:
                print("The auction period is ended and the hand has been PASSed out.")
                with open("output.txt", "a") as tst:
                    tst.write("&a=" + "".join(auction))
                    tst.close()

                x = x + 1
                break
        if fourth_player_call not in bids:
            legal_bids = bids
        if fourth_player_call != "P":
            passes = 0
        if fourth_player_call == "X":
            offered_contract = last_bid + "X"
        if fourth_player_call == "XX":
            offered_contract = last_bid + "XX"
        if fourth_player_call in bids:
            last_bid = fourth_player_call
            legal_bids = bids[bids.index(fourth_player_call) + 1:36]
            offered_contract = last_bid
            if fourth_player_call[1] not in second_fourth_bids:
                second_fourth_bids.update({fourth_player_call[1]: fourth})
                declarer = second_fourth_bids.get(fourth_player_call[1])
            if fourth_player_call[1] in second_fourth_bids:
                declarer = second_fourth_bids[fourth_player_call[1]]

        # reporting the effects of fourth player's action on the auction

        if passes == 3:
            contract = offered_contract
            level = (int(contract[0]))
            denomination = (contract[1])
            print("The auction period is ended. The contract is " + contract + " by " + declarer + ".")
            print("The auction was", auction)
            with open("output.txt", "a") as tst:
                tst.write("".join(auction))
                tst.close()
            if declarer == "n":
                opening_leader = "e"
            elif declarer == "e":
                opening_leader = "s"
            elif declarer == "s":
                opening_leader = "w"
            elif declarer == "w":
                opening_leader = "n"
            print("Opening Leader: " + opening_leader)
            print()
            x = x + 1
            break

    i = i + 1
x = x + 1
