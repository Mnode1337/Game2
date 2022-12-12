'''

    Deck class should be able to:
    instantiate a new deck
        Create all 52 Card obj
        Hold as a list of Card obj

    Shuffle a Deck through a meth call

    *** Random library -> shuffle() ****

    Deal cards from the Deck obj
        The famous Pop() meth

'''

from card import Card
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
    '''
        This class is having an attr tht is another class instance
        user input is not required to instantiate a new deck
        all new deck will have the same attr nothing should differentiate.
        2 new decks that will require user input...
    '''
    def __init__(self):


        self.all_cards = []

        # for each iteration create a suit
        for suit in suits:
            # for each suit rank
            for rank in ranks:
                # create a card obj
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


