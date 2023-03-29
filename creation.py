import os
import shutil
from character import Character
from ability import Ability
import items


# Create a character
def create_character():
    # Set name
    name = str(input('Nome do personagem: '))
    character_class = str(input('Classe do personagem: '))

    # Set status
    health = int(input('Vida: '))
    mana = int(input('Mana: '))
    stamina = int(input('Stamina: '))

    # Set damage
    attack_damage = int(input('Dano de Ataque: '))
    ability_power = int(input('Dano Mágico: '))
    true_damage = int(input('Dano Verdadeiro: '))

    # Set damage negation
    attack_damage_negation = int(input('Negação de Dano de Ataque: '))
    ability_power_negation = int(input('Negação de Dano Mágico: '))

    # Set attack dice
    attack_dice_number = int(input('Quantidade de Dados de Ataque: '))
    attack_dice_value = int(input('Valor dos Dados de Ataque: '))

    # Set defense dice
    defense_dice_number = int(input('Quantidade de Dados de Defesa: '))
    defense_dice_value = int(input('Valor dos Dados de Defesa: '))

    # Set ability dice
    additional_ability_dice = int(input('Quantidade de Dados Adicionais para Habilidade: '))

    # Return character
    return Character(name, character_class, health, mana, stamina, attack_damage, ability_power, true_damage,
                     attack_damage_negation, ability_power_negation, attack_dice_number, attack_dice_value,
                     defense_dice_number, defense_dice_value, additional_ability_dice)


# Create known players
def create_players():
    # Set initial variables
    players = list()
    path = 'saves/'

    # If there are no save file
    if not os.path.exists(path):
        # Create all players
        spark = Character("Spark", "Druida", 59, 39, 59, 7, 29, 5, 5, 7, 1, 8, 1, 8, 1)
        nikolag = Character("Nikolag", "Bárbaro", 43, 33, 22, 16, 7, 5, 7, 3, 1, 12, 1, 12, 1)
        celaena = Character("Celaena", "Bardo", 42, 50, 11, 10, 15, 2, 5, 5, 1, 8, 1, 8, 1)
        ryze = Character("Ryze", "Mago", 73, 34, 49, 8, 13, 4, 3, 7, 1, 6, 1, 6, 1)
        flugel = Character("Flugel", "Paladino", 93, 14, 32, 20, 18, 6, 7, 3, 1, 10, 1, 10, 1)

        # Create a list of players
        players = [celaena, flugel, nikolag, ryze, spark]

        # Give the coins and XP from 1st section
        for player in players:
            player.coins = 500
            player.xp = 785

    # If there are save files
    else:
        # Loop all directories
        for directory in os.listdir(path):
            # If it is Items or Commertiants directory, continue
            if 'Items' in directory or 'Commertiants' in directory:
                continue

            # Get player raw content
            file = open(f'{path + directory}/player.txt', 'r')
            content = file.readlines()
            file.close()

            # Configure player content
            for i in range(len(content)):
                # Remove all '\n'
                content[i] = content[i].replace('\n', '')

                # Convert the needed content to integer
                if i > 1:
                    content[i] = int(content[i])

            # Create new player
            new_player = Character(content[0], content[1], content[2], content[3], content[4], content[5], content[6],
                                   content[7], content[8], content[9], content[10], content[11], content[12],
                                   content[13], content[14])

            # Load player's coins and XP
            new_player.coins = content[15]
            new_player.xp = content[16]

            # Add player to players list
            players.append(new_player)

    # Return players
    return players


# Create some random enemies
def create_enemies():
    temp_enemies = list()
    path = 'temp/'

    if os.path.exists(path):
        temp_enemies = list()

        # Loop all directories
        for directory in os.listdir(path):
            # If it is Items or Commertiants directory, continue
            if 'Items' in directory or 'Commertiants' in directory:
                continue

            # Get player raw content
            file = open(f'{path + directory}/enemy.txt', 'r')
            content = file.readlines()
            file.close()

            # Configure player content
            for i in range(len(content)):
                # Remove all '\n'
                content[i] = content[i].replace('\n', '')

                # Convert the needed content to integer
                if i > 1:
                    content[i] = int(content[i])

            # Create new enemy
            new_enemy = Character(content[0], content[1], content[2], content[3], content[4], content[5], content[6],
                                  content[7], content[8], content[9], content[10], content[11], content[12],
                                  content[13], content[14])

            # Add player to players list
            temp_enemies.append(new_enemy)

    else:
        os.mkdir(path)
    return temp_enemies


# Create known abilities
def create_abilities(players: list):
    # Set initial variables
    path = 'saves/'
    abilities = list()

    # If there is no save file
    if not os.path.exists(path):
        # Create all known abilities
        invisibility = Ability('Invisibilidade', 0, 15, 0, 0, 0, 0, 0, 0, 0, True, 0, False, 0, True, False, 3)
        enchanting_beauty = Ability('Beleza Encantadora', 0, 13, 2, 0, 0, 0, 0, 0, 0, True, 0, False, 0, False, False,
                                    3)
        mortal_fingering = Ability('Dedilhado Mortal', 0, 10, 5, 5, 5, 10, 0, 0, 0, True, 0, True, 0, True, False, 0)
        heavy_strike = Ability('Corte Pesado', 0, 2, 7, 13, 2, 5, 0, 0, 0, False, 1, False, 1, False, True, 4)
        barbarian_roar = Ability('Rugido Bárbaro', 0, 0, 15, 15, 0, 5, 0, 0, 0, False, 1, False, 1, False, True, 4)
        simple_orb = Ability('Orbe Simples', 0, 15, 0, 0, 15, 5, 0, 0, 0, False, 1, False, 0, False, True, 3)
        simple_call = Ability('Chamado Simples', 0, 5, 10, 10, 5, 5, 0, 0, 0, False, 1, False, 1, False, True, 3)

        # Assign the abilities to each player
        players[0].add_ability(mortal_fingering)
        players[1].add_ability(simple_call)
        players[2].add_ability(heavy_strike)
        players[3].add_ability(simple_orb)
        players[2].add_ability(barbarian_roar)
        players[4].add_ability(invisibility)
        players[4].add_ability(enchanting_beauty)

        # Create abilities list
        abilities = [invisibility, enchanting_beauty, heavy_strike, barbarian_roar, mortal_fingering, simple_orb,
                     simple_call]

    # If there are save files
    else:
        # Loop all directories
        for directory in os.listdir(path):
            # If it is Item or Commertiants directory, continue
            if 'Item' in directory or 'Commertiants' in directory:
                continue

            # Loop all files inside player's directory
            for item in os.listdir(path + directory):
                # If file is an ability
                if item != 'player.txt':
                    # Get ability raw content
                    file = open(path + directory + '/' + item, 'r')
                    content = file.readlines()
                    file.close()

                    # Configure ability content
                    for i in range(len(content)):
                        # Remove all '\n'
                        content[i] = content[i].replace('\n', '')

                        # Convert all needed content to integer
                        if (i > 0 and i < 10) or (i == 11) or (i == 13) or (i == 16):
                            content[i] = int(content[i])

                    # Convert the needed content to boolean
                    if content[10] == 'True':
                        content[10] = True
                    else:
                        content[10] = False

                    # Convert the needed content to boolean
                    if content[12] == 'True':
                        content[12] = True
                    else:
                        content[12] = False

                    # Convert the needed content to boolean
                    if content[14] == 'True':
                        content[14] = True
                    else:
                        content[14] = False

                    # Convert the needed content to boolean
                    if content[15] == 'True':
                        content[15] = True
                    else:
                        content[15] = False

                    # Create the ability and add to abilities list
                    ability = Ability(content[0], content[1], content[2], content[3], content[4], content[5],
                                      content[6], content[7], content[8], content[9], content[10], content[11],
                                      content[12], content[13], content[14], content[15], content[16])
                    abilities.append(ability)

                    # Add the ability to the proper player
                    for player in players:
                        if player.name in directory:
                            player.add_ability(ability)

    abilities_path = 'abilities/'
    if os.path.exists(abilities_path):
        for item in os.listdir(abilities_path):
            file = open(abilities_path + item, 'r')
            content = file.readlines()
            file.close()

            # Configure ability content
            for i in range(len(content)):
                # Remove all '\n'
                content[i] = content[i].replace('\n', '')

                # Convert all needed content to integer
                if (i > 0 and i < 10) or (i == 11) or (i == 13) or (i == 16):
                    content[i] = int(content[i])

            # Convert the needed content to boolean
            if content[10] == 'True':
                content[10] = True
            else:
                content[10] = False

            # Convert the needed content to boolean
            if content[12] == 'True':
                content[12] = True
            else:
                content[12] = False

            # Convert the needed content to boolean
            if content[14] == 'True':
                content[14] = True
            else:
                content[14] = False

            # Convert the needed content to boolean
            if content[15] == 'True':
                content[15] = True
            else:
                content[15] = False

            # Create the ability and add to abilities list
            ability = Ability(content[0], content[1], content[2], content[3], content[4], content[5], content[6],
                              content[7], content[8], content[9], content[10], content[11], content[12], content[13],
                              content[14], content[15], content[16])
            abilities.append(ability)

    # Return all abilities
    return abilities


# Create a random enemy
def create_random_enemy():
    # Set name
    name = str(input('Nome do personagem: '))
    character_class = 'Nenhuma'

    health = int(input('Vida do personagem [Padrão é 50]: ') or 50)

    is_mage = bool(input('É mago? [True/False]: '))

    # Set status
    mana = 0
    stamina = health

    # Set damage
    attack_damage = int(health / 10)
    ability_power = 0
    true_damage = 0

    if is_mage:
        ability_power = int(attack_damage / 2)

    # Set damage negation
    attack_damage_negation = 0
    ability_power_negation = 0

    # Set dice
    dice_number = 1
    dice_value = 6

    additional_ability_dice = 0

    # Return character
    return Character(name, character_class, health, mana, stamina, attack_damage, ability_power, true_damage,
                     attack_damage_negation, ability_power_negation, dice_number, dice_value, dice_number, dice_value,
                     additional_ability_dice)


# Save game data
def save(players: list):
    # Remove items buffs
    items.remove_items_buffs(players)

    # Create the saves directory if needed
    if not os.path.exists('saves/'):
        os.mkdir('saves/')

    # Loop players
    for player in players:
        # Create player directory if needed
        path = f'saves/{player.name}/'
        if not os.path.exists(path):
            os.mkdir(path)

        # Save player data
        file = open(f'{path}player.txt', 'w')
        file.writelines(player.get_data())
        file.close()

        # Save all player's abilities
        for ability in player.character_abilities:
            name = ability.name.replace(' ','_')
            file = open(f'{path}/{name}.txt', 'w')
            file.writelines(ability.get_data())
            file.close()

    # Save items
    items.save_items()

    # Remove items buffs
    items.apply_items_buffs(players)