
'''
    Player class should be able to:
        hold a player current list of cards
        a player should be able to add or remove a cards from their hand

        aka list of Card obj

        listItem.extend(anotherListItem)
        .extend() takes a list as arg and merge tht list with an existing one

        what should a brand new created player have as attr
        and what kind of actions do you and player to perform
'''


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
       return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        if type(new_cards) == list:
            # List of multiple Card objs
            self.all_cards.extend(new_cards)
        else:
            # For a single card obj
            self.all_cards.append(new_cards)

    def __str__(self):
        # f string to essentially fillout information
        return f'Player {self.name} has {len(self.all_cards)} cards.'