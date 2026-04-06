from itertools import cycle
from Deck import Deck
from Player import Player
from Action import Action
from Constants import PP_LIMIT

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self._players = cycle([player1, player2])
        self.curPlayer = next(self._players)
        self.turn = 1
        self.endGame = False
        self.bonusActivated = False

    def nextPlayer(self):
        self.curPlayer = next(self._players)
        if self.curPlayer == self.player1:
            self.turn += 1

def main():
    deck_path = input("Enter path to deck file: ").strip()
    player1 = Player(False, 5, 7, Deck(deck_path))
    player2 = Player(True, 4, 6, Deck(deck_path))
    startGame(player1, player2)

def checkWinConditions(game):
    p1_dead = game.player1.health <= 0
    p2_dead = game.player2.health <= 0
    if p1_dead and p2_dead:
        print("Draw!")
    elif p1_dead:
        print("Player 2 Wins!")
    elif p2_dead:
        print("Player 1 Wins!")
    else:
        return False
    game.endGame = True
    return True

def startGame(player1, player2):
    game = Game(player1, player2)
    action = Action(game)

    while not game.endGame:
        if len(game.curPlayer.deck.deckList) == 0:
            winner = "Player 2" if game.curPlayer == player1 else "Player 1"
            print(f"{winner} Wins!")
            game.endGame = True
            break
        game.curPlayer.draw()
        if game.curPlayer.evoTurnsLeft != 0:
            game.curPlayer.evoTurnsLeft -= 1
        if game.curPlayer.sevoTurnsLeft != 0:
            game.curPlayer.sevoTurnsLeft -= 1

        if game.turn == 6 and game.curPlayer == player2:
            game.curPlayer.bonusPlayPoint = True

        game.curPlayer.pp = min(game.turn, PP_LIMIT)

        while True:
            print(game.curPlayer)
            io = input("Play card or end turn: ")
            if io == 'end':
                break
            if io == 'bonus':
                action.useBonus()
                continue
            if not io.isdigit():
                print("Enter a card index number")
                continue
            if not action.playCard(int(io)):
                print("Card not in hand or board full or not enough mana")

        if checkWinConditions(game):
            break

        if game.bonusActivated and game.curPlayer.pp > 0:
            game.curPlayer.bonusPlayPoint = True
            game.curPlayer.pp -= 1
        game.bonusActivated = False

        game.nextPlayer()

if __name__ == "__main__":
    main()
