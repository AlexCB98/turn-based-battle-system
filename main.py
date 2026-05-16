from character import Character

player_1 = Character('Player_1', 500, 30)
enemy_1  = Character('Goblin', 700, 10)

while player_1.is_alive() and enemy_1.is_alive():
    print(f'{player_1.name} attack {enemy_1.name}')
    player_1.attack(enemy_1)
    enemy_1.show_status()

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