import random

class Card():
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.value}{self.suit}"
        
    def __repr__(self):
        return f"{self.value}{self.suit}"

class Deck():
    def __init__(self):
        self.suits = ["♠","♣","♥","♦"]
        self.values = [f"{x}" for x in range(2,11)]
        self.values += ['J','Q','K','A']
        self.cards = [Card(value,suit) for suit in self.suits for value in self.values]
        self.shuffle()

    def shuffle(self):
        for _ in range(random.randint(1,100)):
            random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            self.__init__()
            self.shuffle()

if __name__ == "__main__":
    pass