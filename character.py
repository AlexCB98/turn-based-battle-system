class Character:

    def __init__(self, name, hp, attack_power):
        self.name         = name
        self.hp           = hp
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.hp -= self.attack_power