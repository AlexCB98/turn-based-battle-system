from random import randint

class Character:

    def __init__(self, name, hp, attack_power):
        self.name         = name
        self.hp           = hp
        self.attack_power = attack_power

    def __str__(self):
        return f'{self.name} | HP: {self.hp} | Attack: {self.attack_power}'

    def attack(self, enemy):
        random_dmg = randint(self.attack_power, self.attack_power + 20)
        enemy.take_damage(random_dmg)
        print(f'{self.name} attacks {enemy.name} for {random_dmg} damage!')

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(self)


