from random import shuffle
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"



class Deck:
    def __init__(self,):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '1', '2', '3', '4', '5', '6', '7', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f" The deck of {self.count()} cards."

    def __iter__(self):
        return iter(self.cards)

    def __next__(self):
        pass

    def show_shuffled_cards(self):
        for card in d:
            print(card)

    def count(self):
        return len(self.cards)

    def _deal(self,num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt.")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hands(self, hand_size):
        return self._deal(hand_size)

    def shuffle_cards(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)




d = Deck()
d.shuffle_cards()

d.show_shuffled_cards()
help(d)

"""

d.shuffle_cards()
d.shuffle_cards()
d.shuffle_cards()
d.shuffle_cards()
me = d.deal_hands(7)
you = d.deal_hands(7)
dad = d.deal_hands(7)
print(dad)
print(you)
print(me)

"""