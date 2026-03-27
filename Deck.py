import csv
from Card import Card

class Deck:
    def __init__(self, txt_file):
        self.deckList = []
        self.count = 0
        self.populateDeck(txt_file)

    def populateDeck(self, txt_file):
        with open(txt_file, "r") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.rsplit(" ", 1)
            raw_name = parts[0]
            freq = int(parts[1])
            card_name = raw_name

            card_data = self.queryCard(card_name)
            if card_data is None:
                print(f"Card not found: {card_name}")
                continue

            for _ in range(freq):
                self.addCard(card_data["name"], card_data["cost"], card_data["attack"],
                             card_data["health"], card_data["tribes"])

    def queryCard(self, name):
        script_dir = __import__("os").path.dirname(__import__("os").path.abspath(__file__))
        csv_path = __import__("os").path.join(script_dir, "shadowverse_cards.csv")
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["name"].lower() == name.lower():
                    return {
                        "name": row["name"],
                        "cost": int(row["cost"]) if row["cost"] else 0,
                        "attack": int(row["attack"]) if row["attack"] else 0,
                        "health": int(row["health"]) if row["health"] else 0,
                        "tribes": row["tribes"]
                    }
        return None
    
    def addCard(self, name, cost, attack, health, tribes):
        card = Card(name=name, cost=cost, attack=attack, health=health, tribes=tribes)
        self.deckList.append(card)
        self.count += 1

    def removeCard(self, card: Card):
        self.deckList.remove(card)
        self.count -= 1

    def __str__(self):
        freq = {}
        for card in self.deckList:
            freq[card.name] = freq.get(card.name, 0) + 1
        return "\n".join(f"{name} x{count}" for name, count in freq.items())

    
    

