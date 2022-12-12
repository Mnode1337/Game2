# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# V important we state that at_war == False ie no need to worry about
# this situation s-o we break out of the while loop
# otherwise at_war == True & we loop till we resolve the match up
# we start of the while loop assuming the conflict/worst case scenario
# is True (at_war == True) and we exit the loop only if
# at_war has been resolve ie at_war == False

# the fact that you can connect everything as how
# one class deal with another will make you a good programmer

'''

    07/12/2022
    created by @kehops

    in real world projects, we sketch the logic along the
    classes structures at the same time
'''
from card import Card
from random import shuffle
from deck import Deck
from player import Player

def main():

    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()

    # Nb: the shuffle meth doesn't return anything
    # everything happens with the list_cards
    new_deck.shuffle()

    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    game_on = True

    #counter
    round_number = 0
    while game_on:
        round_number += 1
        print(f'Round {round_number}')

        # a quick check to see if the player is out of card
        if len(player_one.all_cards) == 0:
            print('Player One, out of cards! Player Two wins!')
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print('Player Two, out of cards! Player Two wins!')
            game_on = False
            break

        # for the game to continue, start a new round
        # by removing one card
        # NB: player.remove_one() return all_cards minus one
        player_one_cards = []

        # instead of the removed card to be gone, it will be held by
        # the player_one_cards via append () meth
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        # NB: player.remove_one() return all_cards minus one
        player_two_cards.append(player_two.remove_one())



        at_war = True
        # we kinda assume that war could happen
        while at_war:
            # the player that won this war will hv two cards
            if player_one_cards[-1].value > player_two_cards[-1].value:
                # tht one card that have been removed n held will now b
                # added to one player over all_cards
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                # after doing this there is no more war or
                # comparison to do so we set at_war to false
                # and the game move to another round
                at_war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                at_war = False

            else:
                print('WAR!')
                if len(player_one.all_cards) < 5:
                    print("Player One unable to declare a war")
                    print("Player Two won")

                    game_on = False
                    break

                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to declare a war")
                    print("Player One won")

                    game_on = False
                    break
                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())



'''
    new_deck = Deck()
    card1 = new_deck.all_cards[1]
    bottom_card = new_deck.all_cards[-1]

    new_player = Player("Jose")

    new_player.add_cards(card1)

    print(new_player)

    
        print("\n")
        print(card1)
        print("\n")
        print(bottom_card)
        
        new_deck.shuffle()
        first_pick = new_deck.deal_one()
        print(first_pick)
'''




'''
    for card_obj in new_deck.all_cards:
    print(card_obj)
    print("\n")
'''



'''
two_hearts = Card("Hearts", "Two")
three_clubs = Card("Clubs", "Three")

result = three_clubs.value - two_hearts.value

if result < 0:
    print('three_clubs is less than two_hearts')
else:
    print('two_hearts is smaller')
'''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
