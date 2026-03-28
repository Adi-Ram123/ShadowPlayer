from itertools import cycle
from Deck import Deck
from Player import Player
from Constants import PP_LIMIT, BOARD_LIMIT

def main():
    deck_path = input("Enter path to deck file: ").strip()
    player1 = Player(False, 5, 7, Deck(deck_path))
    player2 = Player(True, 4, 6, Deck(deck_path))
    startGame(player1, player2)

def startGame(player1, player2):

    players = cycle([player1, player2])
    curPlayer = next(players)
    endGame = False
    turn = 1

    while not endGame:
        curPlayer.draw() # check later if drawn last card
        if curPlayer.evoTurnsLeft != 0:
            curPlayer.evoTurnsLeft -= 1
        if curPlayer.sevoTurnsLeft != 0:
            curPlayer.sevoTurnsLeft -= 1
        curPlayer.pp = min(turn, PP_LIMIT)

        while True:
            print(curPlayer)
            io = input("Play card or end turn: ")
            if io == 'end':
                break
            card = next((c for c in curPlayer.hand if c.name == io), None)
            if card and len(curPlayer.board) < BOARD_LIMIT and curPlayer.pp >= card.cost:
                curPlayer.playCard(card)
                curPlayer.pp -= card.cost
            else:
                print("Card not in hand or board full or not enough mana")
        
        curPlayer = next(players)
        if curPlayer == player1:
            turn += 1

    


if __name__ == "__main__":
    main()
