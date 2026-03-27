from Deck import Deck
from Player import Player

def main():
    deck_path = input("Enter path to deck file: ").strip()
    deck = Deck(deck_path)
    player = Player(deck)
    print(deck)
    print()
    print(player)

if __name__ == "__main__":
    main()
