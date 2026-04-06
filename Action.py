from Constants import BOARD_LIMIT

class Action:
    def __init__(self, game):
        self.game = game

    def playCard(self, index: int) -> bool:
        player = self.game.curPlayer
        if index < 0 or index >= len(player.hand):
            return False
        card = player.hand[index]
        if player.pp < card.cost:
            return False
        if len(player.board) >= BOARD_LIMIT:
            return False
        player.playCard(card)
        player.pp -= card.cost
        return True

    def attack(self, attacker_idx: int, target_idx: int) -> bool:
        player = self.game.curPlayer
        opponent = self.game.player2 if player == self.game.player1 else self.game.player1

        if attacker_idx < 0 or attacker_idx >= len(player.board):
            return False
        if target_idx < 0 or target_idx >= len(opponent.board):
            return False

        attacker = player.board[attacker_idx]
        target = opponent.board[target_idx]

        target.changeHealth(-attacker.attack)
        attacker.changeHealth(-target.attack)

        if target.health <= 0:
            opponent.board.remove(target)
        if attacker.health <= 0:
            player.board.remove(attacker)

        return True

    def useBonus(self):
        player = self.game.curPlayer
        if not player.bonusPlayPoint:
            return False
        player.bonusPlayPoint = False
        player.pp += 1
        self.game.bonusActivated = True
        return True
