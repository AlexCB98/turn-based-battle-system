class Character:

    def __init__(self, name, hp, attack_power):
        self.name         = name
        self.hp           = hp
        self.attack_power = attack_power

    def __str__(self):
        return f'{self.name} | HP: {self.hp} | Attack: {self.attack_power}'

    def attack(self, enemy):
        enemy.take_damage(self.attack_power)

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


