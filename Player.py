import random
from Card import Card
from Crests import Crests
from Crest import Crest
from Constants import FAITH_CARDS, HAND_LIMIT, PP_LIMIT, BOARD_LIMIT

class Player:

    def __init__(self, playerTwo, evoTurns, sevoTurns, deck):
        self.health = 20
        self.deck = deck
        self.hand: list[Card] = []
        self.crests = Crests()
        self.board: list[Card] = []
        self.pp = 0
        self.isPlayerTwo = playerTwo
        self.bonusPlayPoint = playerTwo
        self.evoTurnsLeft = evoTurns
        self.sevoTurnsLeft = sevoTurns
        self.evoCount = 2
        self.sevoCount = 2
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

    def playCard(self, card: Card):
        self.hand.remove(card)
        self.board.append(card)

    def updateHealth(self, offset):
        self.health += offset
    
    def evo(self, target:Card) -> bool:
        target.changeAttack(2)
        target.changeHealth(2)
        self.evoCount -= 1
        
    def sevo(self, target:Card) -> bool:
        target.changeAttack(3)
        target.changeHealth(3)
        self.sevoCount -= 1

    def __str__(self):
        W = 78

        def card_lines(card, idx):
            CW = 11
            name = (card.name[:CW-3] + "...") if len(card.name) > CW else card.name
            name = name.center(CW)
            stats = f"{card.attack}/{card.health}".center(CW)
            border = "+" + "-" * CW + "+"
            idx_str = f"#{idx}"
            cost_line = str(card.cost) + idx_str.rjust(CW - len(str(card.cost)))
            return [border, f"|{cost_line}|", f"|{name}|", f"|{stats}|", border]

        def render_row(cards, chunk_size=5, start_idx=0):
            if not cards:
                return f"|   {'(empty)':<{W-5}}|"
            chunks = [cards[i:i+chunk_size] for i in range(0, len(cards), chunk_size)]
            rows = []
            for chunk_idx, chunk in enumerate(chunks):
                boxes = [card_lines(c, start_idx + chunk_idx * chunk_size + i) for i, c in enumerate(chunk)]
                rows.append("\n".join(f"| {'  '.join(b[i] for b in boxes):<{W-3}}|" for i in range(len(boxes[0]))))
            return "\n".join(rows)

        sep = "+" + "-" * (W - 2) + "+"

        def row(text):
            return f"| {text:<{W-3}}|"

        crests = ", ".join(str(c) for c in self.crests.crest_list) or "(none)"

        return "\n".join([
            sep,
            row(f"Health: {self.health}   PP: {self.pp}/{PP_LIMIT}" + (f"   +1 Play Point: {'Available' if self.bonusPlayPoint else 'Used'}" if self.isPlayerTwo else "")),
            sep,
            row("BOARD"),
            render_row(self.board),
            sep,
            row("HAND"),
            render_row(self.hand),
            sep,
            row(f"Evo  — Turns Left: {self.evoTurnsLeft}   Remaining: {self.evoCount}"),
            row(f"Sevo — Turns Left: {self.sevoTurnsLeft}   Remaining: {self.sevoCount}"),
            row(f"Crests: {crests}"),
            sep,
        ])
