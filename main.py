from character import Character

player_1 = Character('Player_1', 500, 30)
enemy_1  = Character('Goblin', 700, 10)

player_1.show_status()
enemy_1.show_status()

player_1.attack(enemy_1)
enemy_1.attack(player_1)

print('\n')

player_1.show_status()
enemy_1.show_status()