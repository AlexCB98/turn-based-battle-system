class Inventory:

    def __init__(self, potion_count, healing_amount):
        self.potion_count   = potion_count
        self.healing_amount = healing_amount

    def __str__(self):
        return f'Potions: {self.potion_count} | Healing: {self.healing_amount}'

    def show_inventory(self):
        print(self)

    def use_potion(self, character):
        if self.potion_count > 0:
            character.heal(self.healing_amount)
            self.potion_count -= 1
        else:
            print('\n ** No potions left! **\n')