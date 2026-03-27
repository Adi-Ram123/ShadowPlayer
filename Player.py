import random
from Card import Card
from Deck import Deck
from Crests import Crests
from Crest import Crest
from Constants import FAITH_CARDS, HAND_LIMIT

class Player:

    def __init__(self, deck: Deck):
        self.health = 20
        self.deck = deck
        self.hand: list[Card] = []
        self.crests = Crests()
        self.drawInitialHand()
        self.checkFaith()

    def drawInitialHand(self):
        for _ in range(5):
            self.draw()

    def draw(self):
        card = random.choice(self.deck.deckList)
        self.deck.removeCard(card)
        if len(self.hand) < HAND_LIMIT:
            self.hand.append(card)

    def checkFaith(self):
        existing = {c.name for c in self.crests.crest_list}
        for card in self.deck.deckList:
            if card.name in FAITH_CARDS and card.name not in existing:
                self.crests.addCrest(Crest(name=card.name, count=0, isFaith=True))
                existing.add(card.name)

    def updateHealth(self, offset):
        self.health += offset

    def __str__(self):
        hand = "\n".join(str(card) for card in self.hand)
        crests = ", ".join(str(crest) for crest in self.crests.crest_list)
        return f"Health: {self.health}\nPlayer Hand:\n{hand}\nCrest List: {crests}"
