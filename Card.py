class Card:
    def __init__(self, name, cost, attack, health, tribes):
        # Base stats
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.tribes = tribes

        # Attributes
        self.evo = False
        self.super_evo = False
        self.attack_count = 1
        self.ward = False
        self.rush = False
        self.intimidate = False
        self.bane = False
        self.drain = False
        self.aura = False
        self.barrier = False
    
    def changeAttack(self, offset: int):
        self.attack += offset

    def changeHealth(self, offset: int):
        self.health += offset

    def __str__(self):
        return f"{self.name} {self.attack}/{self.health}"
