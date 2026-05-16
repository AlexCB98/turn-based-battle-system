from character import Character
from inventory import Inventory

player_1 = Character('Player_1', 500, 30)
enemy_1  = Character('Goblin', 700, 21)

inventory = Inventory(3, 50)

while player_1.is_alive() and enemy_1.is_alive():

    player_1.show_status()
    enemy_1.show_status()

    action = int(input('1. Attack / 2. Heal  : '))

    if action == 1:
        print(f'{player_1.name} attack {enemy_1.name}')
        player_1.attack(enemy_1)
        enemy_1.show_status()
        print('\n')
    else:
        print(f'\n{player_1.name} used a potion.\n')
        inventory.use_potion(player_1)
        print(f'\nPotions left: {inventory.potion_count * "🧪"}\n')
        player_1.show_status()
        inventory.show_inventory()
        print('\n')


    if enemy_1.is_alive():
        print(f'{enemy_1.name} attacks {player_1.name}')
        enemy_1.attack(player_1)
        player_1.show_status()
        print('\n')

if player_1.is_alive():
    print(f'{player_1.name} wins!')
else:
    print(f'{enemy_1.name} wins!')