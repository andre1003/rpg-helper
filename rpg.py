# Imports
import os
from random import randint, uniform
import items
from character import Character
from ability import Ability
from utils import bcolors


# Roll a dice
def d(number: int):
    return randint(1, number)


# Calculate damage
def calculate_damage(attacker: Character, defender: Character, is_heavy_attack: bool, stamina_cost: int):
    print(25*'=-')

    print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} X {bcolors.RED}{defender.name}{bcolors.ENDC}\n\n')
    
    print(f'{bcolors.GREEN}{attacker.name} ataca!{bcolors.ENDC}\n')

    # Get attack intensity multiplier
    attack_intensity_multiplier = 1
    additional_defender_dice = 0
    if is_heavy_attack:
        attack_intensity_multiplier = 2
        additional_defender_dice = 1

    # Attacker AD
    attacker_ad_dice = 0
    for i in range(attacker.attack_dice_number):
        dice_value = d(attacker.attack_dice_value)
        attacker_ad_dice += dice_value

        print(f'{attacker.name} rolou 1d{attacker.attack_dice_value} para AD e tirou: \t{dice_value}')
    print(f'\t>> Total dos dados de ataque AD de {attacker.name}: {attacker_ad_dice}\n')
    
    # Attacker AP
    attacker_ap_dice = 0
    for i in range(attacker.attack_dice_number):
        dice_value = d(attacker.attack_dice_value)
        attacker_ap_dice += dice_value

        print(f'{bcolors.CYAN}{attacker.name} rolou 1d{attacker.attack_dice_value} para AP e tirou: \t{dice_value}{bcolors.ENDC}')
    print(f'\t{bcolors.CYAN}>> Total dos dados de ataque AP de {attacker.name}: {attacker_ap_dice}{bcolors.ENDC}\n\n\n\n')


    print(f'{bcolors.RED}{defender.name} defende!{bcolors.ENDC}\n')

    # Defender AD negation
    defender_ad_dice = 0
    for i in range(defender.defense_dice_number + additional_defender_dice):
        dice_value = d(defender.defense_dice_value)
        defender_ad_dice += dice_value

        print(f'{defender.name} rolou 1d{defender.defense_dice_value} para AD e tirou: \t{dice_value}')
    print(f'\t>> Total dos dados de defesa AD de {defender.name}: {defender_ad_dice}\n')

    # Defender AP negation
    defender_ap_dice = 0
    for i in range(defender.defense_dice_number + additional_defender_dice):
        dice_value = d(defender.defense_dice_value)
        defender_ap_dice += dice_value

        print(f'{bcolors.CYAN}{defender.name} rolou 1d{defender.defense_dice_value} para AP e tirou: \t{dice_value}{bcolors.ENDC}')
    print(f'\t{bcolors.CYAN}>> Total dos dados de defesa AP de {defender.name}: {defender_ap_dice}{bcolors.ENDC}\n\n\n\n')

    # Check if player have stamina
    if attacker.stamina - (5 * attack_intensity_multiplier) < 0:
        print('\nStamina insuficiente para o ataque!')
        return 0

    # Remove stamina cost
    attacker.stamina -= (stamina_cost * attack_intensity_multiplier)

    # Declare AD and AP final damage variables
    ad_damage = 0
    ap_damage = 0
    td_damage = attacker.true_damage

    # If attacker succeeds the AD attack, set ad_damage
    if attacker_ad_dice > defender_ad_dice:
        ad_damage = attacker.attack_damage - defender.attack_damage_negation

    # If attacker succeeds the AP attack, set ap_damage
    if attacker_ap_dice > defender_ap_dice:
        ap_damage = attacker.ability_power - defender.ability_power_negation


    # If the defender armor was greater than attacker AD, set ad_damage to 0
    if ad_damage <= 0:
        print(f'{bcolors.RED}{defender.name}{bcolors.ENDC} defendeu o Dano de Ataque!')
        ad_damage = 0
    else:
        print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} acertou o Dano de Ataque!')


    # If the defender armor was greater than attacker AP, set ap_damage to 0
    if ap_damage <= 0:
        print(f'{bcolors.RED}{defender.name}{bcolors.ENDC} defendeu o {bcolors.CYAN}Dano Mágico{bcolors.ENDC}!\n')
        ap_damage = 0
    else:
        print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} acertou o {bcolors.CYAN}Dano Mágico{bcolors.ENDC}!\n')


    # Calculate final damage
    final_damage = (ad_damage + ap_damage + td_damage) * attack_intensity_multiplier
    aux = 'Tipo de Ataque: Básico'
    if is_heavy_attack:
        aux = 'Tipo de Ataque: Pesado (dano dobrado)'
    print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} aplicou:\n\tDano do Ataque: {ad_damage}\n\tDano Mágico: {ap_damage}\n\tDano Verdadeiro: {td_damage}\n\t{aux}\n\t{bcolors.RED}Dano Total: {final_damage}{bcolors.ENDC}\n{bcolors.GREEN}\tGasto de Stamina: {(stamina_cost * attack_intensity_multiplier)}{bcolors.ENDC}')

    print(25*'=-')

    # Return final damage
    return final_damage


# Calculate damage from ability
def calculate_damage_ability(attacker: Character, defender: Character, ability: Ability, players: list, current_turn: int, current_combat_abilities: list):
    print()
    print(25*'-=')
    
    # Get dice number, if needed
    dice_number = 0
    if not ability.no_dice:
        dice_number = attacker.attack_dice_number + attacker.additional_ability_dice

    # Get the greater dice value
    dice_value = 0
    for i in range(dice_number):
        value = d(attacker.attack_dice_value)
        if value > dice_value:
            dice_value = value

    # If ability did not cast
    if not ability.check_success(dice_value):
        print(f'\n{bcolors.RED}A habilidade falhou no casting...{bcolors.ENDC}\n')
        print()
        print(25*'-=')
        return 0

    # If ability is unic use and have already been used
    was_ability_used = False
    for used_ability in current_combat_abilities:
        if ability in used_ability:
            was_ability_used = True
            break

    if ability.is_unic_use and was_ability_used:
        print('\nA habilidade já foi utilizada!\n')
        print()
        print(25*'-=')
        return 0

    # Check this ability last use
    last_ability_use = -1
    for used_ability in current_combat_abilities:
        if ability in used_ability:
            last_ability_use = used_ability[0]
    
    # If ability is in cooldown
    if last_ability_use > 0:
        turn_difference = current_turn - last_ability_use
        if turn_difference <= 0 or turn_difference < ability.cooldown:
            print('\nA habilidade ainda está em cooldown!\n')
            print()
            print(25*'-=')
            return 0

    # If player can cast the ability
    if attacker.health <= ability.health_cost or attacker.mana < ability.mana_cost or attacker.stamina < ability.stamina_cost:
        print(f'\n{attacker.name} não pode castar a habilidade. Não cumpre os requisitos de casting!\n')
        print()
        print(25*'-=')
        return 0
    
    # Remove ability cost
    attacker.health -= ability.health_cost
    attacker.mana -= ability.mana_cost
    attacker.stamina -= ability.stamina_cost

    # Save the ability used on this combat
    current_combat_abilities.append((current_turn, ability))

    # Give the buff for all players
    if ability.affect_other_player:
        for player in players:
            player.buff_status(ability.additional_health, ability.additional_mana, ability.additional_stamina)
            player.buff_damage(ability.additional_attack_damage, ability.additional_ability_power, ability.additional_true_damage)

    if not ability.is_attack:
        print(f'\nA habilidade {bcolors.CYAN}{ability.name}{bcolors.ENDC} não ataca, portanto nenhum dano será causado!')
        return 0

    # Declare AD, AP and TD final damage variables
    ad_damage = (attacker.attack_damage + ability.additional_attack_damage) - defender.attack_damage_negation
    ap_damage = (attacker.ability_power + ability.additional_ability_power) - defender.ability_power_negation
    td_damage = attacker.true_damage + ability.additional_true_damage


    # If the defender armor was greater than attacker AD, set ad_damage to 0
    if ad_damage < 0:
        print(f'\n{bcolors.RED}{defender.name}{bcolors.ENDC} defendeu o Dano de Ataque!')
        ad_damage = 0
    else:
        print(f'\n{bcolors.GREEN}{attacker.name}{bcolors.ENDC} acertou o Dano de Ataque!')
    
    # If the defender armor was greater than attacker AP, set ap_damage to 0
    if ap_damage < 0:
        print(f'{bcolors.RED}{defender.name}{bcolors.ENDC} defendeu o {bcolors.CYAN}Dano Mágico{bcolors.ENDC}!\n')
        ap_damage = 0
    else:
        print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} acertou o {bcolors.CYAN}Dano Mágico{bcolors.ENDC}!\n')

    # Return final damage
    final_damage = ad_damage + ap_damage + td_damage
    print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} aplicou:\n\tDano do Ataque: {ad_damage}\n\tDano Mágico: {ap_damage}\n\tDano Verdadeiro: {td_damage}\n\t{bcolors.RED}Dano Total da Habilidade: {final_damage}{bcolors.ENDC}')
    print()
    print(25*'-=')

    return final_damage


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
    return Character(name, character_class, health, mana, stamina, attack_damage, ability_power, true_damage, attack_damage_negation, ability_power_negation, attack_dice_number, attack_dice_value, defense_dice_number, defense_dice_value, additional_ability_dice)


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
            new_player = Character(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7], content[8], content[9], content[10], content[11], content[12], content[13], content[14])
            
            # Load player's coins and XP
            new_player.coins = content[15]
            new_player.xp = content[16]

            # Add player to players list
            players.append(new_player)
            
    # Return players
    return  players


# Create some random enemies
def create_enemies():
    # Create the default enemies
    goblin = Character('Goblin', 'None', 50, 0, 0, 5, 0, 0, 0, 0, 1, 6, 1, 6, 0)
    #mage_goblin = Character('Goblin Mago', 'None', 25, 0, 0, 0, 3, 0, 0, 0, 1, 6, 1, 6, 0)
    #big_goblin = Character('Goblin Grande', 'None', 300, 0, 0, 30, 0, 0, 0, 0, 1, 6, 1, 6, 0)
    #archer_goblin = Character('Goblin Arqueiro', 'None', 50, 0, 0, 15, 0, 0, 0, 0, 1, 6, 1, 6, 0)
    #armored_goblin = Character('Goblin de Armadura', 'None', 50, 0, 0, 5, 0, 0, 2, 2, 1, 6, 1, 6, 0)
    #armored_big_goblin = Character('Goblin Grande de Armadura', 'None', 300, 0, 0, 30, 0, 0, 15, 15, 1, 6, 1, 6, 0)

    # Return the list of enemies
    return [goblin]#, mage_goblin, big_goblin, archer_goblin, armored_goblin, armored_big_goblin]


# Create known abilities
def create_abilities(players: list):
    # Set initial variables
    path = 'saves/'
    abilities = list()

    # If there is no save file
    if not os.path.exists(path):
        # Create all known abilities
        invisibility = Ability('Invisibilidade', 0, 15, 0, 0, 0, 0, 0, 0, 0, True, 0, False, 0, True, False, 3)
        enchanting_beauty = Ability('Beleza Encantadora', 0, 13, 2, 0, 0, 0, 0, 0, 0, True, 0, False, 0, False, False, 3)
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
        abilities = [invisibility, enchanting_beauty, heavy_strike, barbarian_roar, mortal_fingering, simple_orb, simple_call]

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
                    ability = Ability(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7], content[8], content[9], content[10], content[11], content[12], content[13], content[14], content[15], content[16])
                    abilities.append(ability)

                    # Add the ability to the proper player
                    for player in players:
                        if player.name in directory:
                            player.add_ability(ability)

    # Return all abilities
    return abilities


# Create a random enemy
def create_random_enemy():
    # Set name
    name = str(input('Nome do personagem: '))
    character_class = 'Nenhuma'

    try:
        min_health = int(input('Mínimo de vida [default 50]: '))
    except:
        min_health = 50

    try:
        max_health = int(input('Máximo de vida [default 100]: '))
    except:
        max_health = 100

    is_mage = bool(input('É mago? [True/False]: '))

    # Set status
    health = randint(min_health, max_health)
    mana = 0
    stamina = 0

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
    return Character(name, character_class, health, mana, stamina, attack_damage, ability_power, true_damage, attack_damage_negation, ability_power_negation, dice_number, dice_value, dice_number, dice_value, additional_ability_dice)


# Define turn order
def define_order(players: list, enemies: list):
    # Get all players' names
    names = list()
    for player in players:
        names.append(player.name)

    # Get all enemies' names
    for enemy in enemies:
        names.append(enemy.name)

    # Roll 1d20 for each character and save it in a dictionary
    order = dict()
    for i in range(len(names)):
        dice = d(20)
        print(f'{bcolors.CYAN}{names[i]}{bcolors.ENDC} tirou {bcolors.GREEN}{dice}{bcolors.ENDC}')
        order[names[i]] = dice
    
    # Sort the dictionary and display the turn order
    print('\nA ordem do combate é:')
    order = sorted(order.items(), key=lambda x:x[1], reverse=True)
    for i in range(len(order)):
        print(f'{i+1}º - {order[i][0]}')

    return order
    

# Loot a chest
def loot_chest():
    # Define percents
    coin_percent = float(input('Chance de dropar moeda: '))
    item_percent = float(input('Chance de dropar item: '))
    ore_percent = float(input('Chance de dropar minério: '))
    weed_percent = float(input('Chance de dropar erva: '))

    print()

    # Define min and max coins
    min_coins = int(input('Mínimo de moedas: '))
    max_coins = int(input('Máximo de moedas: '))

    # Get random number of coins
    coins = randint(min_coins, max_coins)
    ores = randint(1, 3)

    # Get number of loots that the chest will have
    percents = (coin_percent, item_percent, ore_percent, weed_percent)
    loot_number = randint(1, 4)

    # Display it on screen
    print(f'\nO baú tem {loot_number} loots!\n')

    # Initialize loot variables
    loot = 0
    loots_index = list()

    # Loop players
    for player in players:
        print(25*'=-')
        print(f'\nLoot de {bcolors.GREEN}{player.name}{bcolors.ENDC}')

        # Get all loot index
        while(loot < loot_number):
            index = randint(0, 3)
            if index in loots_index:
                continue

            value = uniform(0.0, 100.0)
            
            if value <= percents[index]:
                loot += 1
                loots_index.append(index)

        # Give the loot to the player
        for index in loots_index:
            print(end='\n')

            # Coins
            if index == 0:
                print('O baú contem moedas!')
                print(f'+{coins} moedas')
                
            # Items
            elif index == 1:
                print('O baú contem items!')
                item = items.get_item_at_index(player.character_class, randint(0, 7))
                print(f'+ {item}')

            # Ore
            elif index == 2:
                ore = items.ores[randint(0, len(items.ores) - 1)]
                print(f'+ {ores} de {ore}')

            # Weed
            elif index == 3:
                print('Erva de cura simples')

    print(25*'=-')

    # Press any key to continue
    input('\nPressione qualquer tecla para continuar...')


# Edit a character
def edit(all_characters: list):
    print()
    print(25*'-=')
    print()

    for i in range(len(all_characters)):
        print(f'{i} - {all_characters[i].name}')

    option = int(input('\nQual personagem voce quer alterar: '))

    character = all_characters[option]

    # Status
    health = int(input('Adicionar Vida: '))
    mana = int(input('Adicionar Mana: '))
    stamina = int(input('Adicionar Stamina: '))

    # Damage
    attack_damage = int(input('Adicionar Dano de Ataque: '))
    ability_power = int(input('Adicionar Dano Mágico: '))
    true_damage = int(input('Adicionar Dano Verdadeiro: '))

    character.buff_status(health, mana, stamina)
    character.buff_damage(attack_damage, ability_power, true_damage)

    print()
    print(25*'-=')
    print()


# Combat handler
def combat(current_turn: int, players: list, enemies: list, current_combat_abilities: list):
    # Get all characters
    all_characters = players.copy() + enemies.copy()

    # Edit a character, if needed
    opt = 2
    while opt == 2:
        opt = int(input('1 - Iniciar a Luta\n2 - Alterar o Status de Personagem\n\nSua Escolha: '))
        if opt == 2:
            edit(all_characters)

        elif opt == -2:
            return -2

        else:
            print()
            print(25*'-=')
            print()


    # Start combat
    print('Iniciando o combate. Os combatentes são:\n')
            
    # Display it on screen
    for i in range(len(all_characters)):
        print(f'{i} - {all_characters[i].name}')

    print()

    # Get the attacker and the defender
    attacker_index = int(input('Escolha o atacante: '))
    if attacker_index == -1:
        return
    elif attacker_index == -2:
        return -2
    attacker = all_characters[attacker_index]
    defender = all_characters[int(input('Escolha o defensor: '))]

    print()

    # Set damage
    damage = 0

    # If the attacker have any ability, check if it will use it or not
    if len(attacker.character_abilities) > 0:
        op = int(input('O atacante usará uma habilidade? [1 - True/0 - False]: '))
        if op == 1:
            print('\nHabilidades do atacante:\n')
            for i in range(len(attacker.character_abilities)):
                print(f'{i} - {attacker.character_abilities[i].name}')

            index = int(input('\nQual habilidade o atacante vai usar: '))
            damage += calculate_damage_ability(attacker, defender, attacker.character_abilities[index], players, current_turn, current_combat_abilities)

    # Check if attacker will perform a normal attack
    if defender.health > 0 and int(input('\nO atacante vai realizar um ataque normal? [1 - True/0 - False]: ')) == 1:
        option = int(input('É um ataque pesado? [1 - True/0 - False]: '))
        is_heavy_attack = False
        print()

        if option == 1:
            is_heavy_attack = True

        additional_ad = 0
        additional_ap = 0
        additional_td = 0
        stamina_cost = 2
        if attacker in enemies:
            stamina_cost = 0

        if attacker.character_class in items.items:
            print(f'{bcolors.GREEN}Armas do Atacante{bcolors.ENDC}\n')
            attacker_items = list()
            for char_class in items.items:
                if char_class == attacker.character_class:
                    attacker_items = items.items[char_class]

            count = 0
            for i in range(len(attacker_items)):
                if attacker_items[i].is_weapon:
                    print(f'{i} - {attacker_items[i].name}')
                    count+=1

            if count == 0:
                print(f'{bcolors.RED}O atacante não tem nenhum arma!{bcolors.ENDC}')
            else:
                option = int(input('\nQual arma o atacante usará: '))

                additional_ad = attacker_items[option].additional_attack_damage
                additional_ap = attacker_items[option].additional_ability_power
                additional_td = attacker_items[option].additional_true_damage
                stamina_cost = attacker_items[option].stamina_cost

                attacker.buff_damage(additional_ad, additional_ap, additional_td)

        damage += calculate_damage(attacker, defender, is_heavy_attack, stamina_cost)
        attacker.debuff_damage(additional_ad, additional_ap, additional_td)
    else:
        print()
        print(25*'-=')

    # Decrease defender health
    defender.decrease_health(damage)

    # If defender dies, remove it from the list
    if defender.health == 0:
        if defender in enemies:
            print(f'\n{bcolors.RED}{defender.name} morreu!{bcolors.ENDC}')
            enemies.remove(defender)
            del(defender)

            xp = randint(int(input('Mínimo de XP: ') or 10), int(input('Máximo de XP: ') or 20))
            coins = randint(int(input('\nMínimo de Moedas: ') or 0), int(input('Máximo de Moedas: ') or 0))

            print()
            print(25*'-=')
            print(f'\nRecompensas\n\n{bcolors.CYAN}+{xp} XP{bcolors.ENDC}\n{bcolors.WARNING}+{coins} moedas{bcolors.ENDC}')

            for player in players:
                player.coins += coins
                player.xp += xp
        else:
            print(f'\n{bcolors.GREEN}{defender.name} {bcolors.RED}morreu!{bcolors.ENDC}')

    # Press any key to continue
    input('\nPressione qualquer tecla para continuar...')


# Assing an ability to a character
def assign_ability(abilities: list, character: Character):
    print('\nHabilidades para atribuir:\n')
    for i in range(len(abilities)):
        print(f'{i} - {abilities[i].name}')

    ability = int(input('\nHabilidade para atribuir: '))

    character.add_ability(abilities[ability])

    print(f'\n\nHabilidade {bcolors.CYAN}{abilities[ability].name}{bcolors.ENDC} atribuida à {bcolors.GREEN}{character.name}{bcolors.ENDC}')


# Remove all temporary buffs
def remove_buffs(current_combat_abilities: list, players: list):
    for ability in current_combat_abilities:
        if not ability[1].is_attack:
            for player in players:
                player.debuff_damage(ability[1].additional_attack_damage, ability[1].additional_ability_power, ability[1].additional_true_damage)


# Reset stamina of all players
def reset_stamina(players: list):
    for player in players:
        player.stamina = player.base_stamina


# Commertiant handler
def commertiant(players: list):
    while True:
        clear()
        print('Compra e Venda')

        # Print options
        index = 1
        for commertiant in items.merchants:
            print(f'{index} - {commertiant}')
            index += 1
        print()

        # Get the commertiant type
        option = int(input('Qual o tipo de comerciante: '))

        print()

        # Init commertiant items
        commertiant_items = list()

        # Merchant
        if option == 1:
            print(25*'-=')
            print(f'\n{bcolors.GREEN}MERCADOR{bcolors.ENDC}\n')
            commertiant_items = items.merchant_items

        # Market
        elif option == 2:
            print(25*'-=')
            print(f'\n{bcolors.GREEN}MERCADO{bcolors.ENDC}\n')
            commertiant_items = items.market_items

        # Big market
        elif option == 3:
            print(25*'-=')
            print(f'\n{bcolors.GREEN}MERCADÃO{bcolors.ENDC}\n')
            commertiant_items = items.big_market_items

        # Blacksmith
        elif option == 4:
            print(25*'-=')
            print(f'\n{bcolors.GREEN}FERREIRO{bcolors.ENDC}\n')
            commertiant_items = items.blacksmith_items

        # Stable
        elif option == 5:
            print(25*'-=')
            print(f'\n{bcolors.GREEN}ESTÁBULO{bcolors.ENDC}\n')
            commertiant_items = items.stable_items  

        # Alchemist
        elif option == 6:
            print(25*'-=')
            print(f'\n{bcolors.GREEN}ALQUIMISTA{bcolors.ENDC}\n')
            commertiant_items = items.alchemist_items

        # Jewelry
        elif option == 7:
            print(25*'-=')
            print(f'\n{bcolors.GREEN}JOALHERIA{bcolors.ENDC}\n')
            commertiant_items = items.jewelry_items

        # Show items and prices
        index = 0
        for item in commertiant_items:
            price = f'{item.price:,}'.replace(',', '.')
            description = item.description or '[O item não possui descrição]'
            print(f'{index} - {bcolors.CYAN}{item.name}{bcolors.ENDC} - {bcolors.YELLOW}${price}{bcolors.ENDC}\n{description}\n')
            index += 1

        # Check if any player wants to buy an item
        option = int(input('\nQual item o jogador deseja adicionar [-1 para voltar]: '))
        if option != -1:
            print()
            for i in range(len(players)):
                print(f'{i} - {players[i].name}')
            opt = int(input('\nQual jogador quer comprar o item: '))

            # If the player has enougth money to buy the item
            if players[opt].coins >= commertiant_items[option].price:
                # Decrease player's coins and add the item to the player's inventory
                players[opt].coins -= commertiant_items[option].price
                items.items[players[opt].character_class].append(commertiant_items[option])
                print(f'{bcolors.CYAN}{commertiant_items[option].name}{bcolors.ENDC} adicionado ao inventário de {bcolors.GREEN}{players[opt].name}{bcolors.ENDC}')

            # Check if player want to keep buying
            option = int(input('\nDeseja continuar comprando? [1 - True/0 - False]:  ') or 1)

        if option != 1:
            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')
            break


# Display all players
def display_players(players: list):
    print('Jogadores existentes:\n')
    print(f'Nome\t\t   {bcolors.RED}Vida\t\t   {bcolors.CYAN}Mana\t\t {bcolors.GREEN}Stamina{bcolors.ENDC}\t AD\t AP\t TD\n')
    for player in players:
        print(f'{player.name}\t\t{bcolors.RED}{player.health:3d} / {player.base_health:3d}\t{bcolors.CYAN}{player.mana:3d} / {player.base_mana:3d}\t{bcolors.GREEN}{player.stamina:3d} / {player.base_stamina:3d}{bcolors.ENDC}\t{player.attack_damage:3d}\t{player.ability_power:3d}\t{player.true_damage:3d}')

    print('\n')


# Decision
def decision():
    master_dice_value = int(input('Valor do dado do mestre: '))
    player_charisma = int(input('Carisma do jogador: '))
    player_power = 0

    while True:
        player_charisma -= 15

        if player_charisma >= 0:
            player_power += 2
        else:
            break

    master_dice = d(master_dice_value - player_power)
    player_dice = d(20)

    print(f'\nDado do {bcolors.RED}Mestre{bcolors.ENDC} (1d{master_dice_value - player_power}): {bcolors.RED}{master_dice}{bcolors.ENDC}')
    print(f'Dado do {bcolors.GREEN}Jogador{bcolors.ENDC} (1d20): {bcolors.GREEN}{player_dice}{bcolors.ENDC}\n')

    print(25*'-=')
    print()

    if player_dice >= master_dice:
        print(f'A decisão do jogador {bcolors.GREEN}ACONTECE{bcolors.ENDC}')

    else:
        print(f'A decisão do jogador {bcolors.RED}FALHA{bcolors.ENDC}')


# Create a new ability
def create_ability():
    name = input('Nome da Habilidade: ')

    health_cost = int(input('\nCusto de Vida: '))
    mana_cost = int(input('Custo de Mana: '))
    stamina_cost = int(input('Custo de Stamina: '))

    additional_attack_damage = int(input('\nDano de Ataque Adicional: '))
    additional_ability_power = int(input('Dano Mágico Adicional: '))
    additional_true_damage = int(input('Dano Verdadeiro Adicional: '))

    additional_health = int(input('\nVida Adicional: '))
    additional_mana = int(input('Mana Adicional: '))
    additional_stamina = int(input('Stamina Adicional: '))

    option = int(input('\nUso Único por Combate [1 - True/0 - False]: '))
    is_unic_use = False
    if option == 1:
        is_unic_use = True

    cooldown = int(input('Cooldown (em turnos): '))

    option = int(input('Afeta Outro Jogaores [1 - True/0 - False]: '))
    affect_other_player = False
    if option == 1:
        affect_other_player = True

    number_of_enemies_affected = int(input('Número de Inimigos Afetados: '))

    option = int(input('\nNão Precisa de Dado [1 - True/0 - False]: '))
    no_dice = False
    if option == 1:
        no_dice = True

    option = int(input('\nÉ um ataque [1 - True/0 - False]: '))
    is_attack = False
    if option == 1:
        is_attack = True

    min_dice_value = int(input('Valor mínimo para castar a habilidade: '))

    return Ability(name, health_cost, mana_cost, stamina_cost, additional_attack_damage, additional_ability_power, additional_true_damage, additional_health, additional_mana, additional_stamina, is_unic_use, cooldown, affect_other_player, number_of_enemies_affected, no_dice, is_attack, min_dice_value)


# Show all players invetories
def show_inventories(players: list):
    # Loop players
    for player in players:
        # Display player name, coins and XP
        print(f'Inventário de {bcolors.GREEN}{player.name}{bcolors.ENDC}\n')
        print(f'\t{bcolors.CYAN}XP: {player.xp}{bcolors.ENDC}\n\t{bcolors.YELLOW}Moedas: {player.coins}{bcolors.ENDC}\n')

        # Loop player items, displaying each one of them
        for item in items.items[player.character_class]:
            price = f' - {bcolors.YELLOW}SEM PREÇO{bcolors.ENDC}'
            if item.price != -1:
                price = f' - {bcolors.YELLOW}${item.price:,}{bcolors.ENDC}'.replace(',', '.')
            description = item.description or '[Item sem descrição]'
            print(f'\t{bcolors.CYAN}{item.name}{bcolors.ENDC}{price}\n\t{description}\n')
        print(25*'-=')
        print()


# Save game data
def save(players: list):
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
        

# Clear screen
def clear():
    # Clearing the Screen
    # posix is os name for Linux or mac
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')


# Display main options
def options():
    print(
    f'{bcolors.CYAN}'+
    f'1  - Criar jogador\n'
    f'2  - Criar inimigo\n'+
    f'3  - Criar habilidade\n'+
    f'4  - Criar item\n\n'+
    f'{bcolors.RED}'+
    f'5  - Excluir jogador\n'+
    f'6  - Excluir inimigo\n'+
    f'7  - Excluir todos os inimigos\n\n'+
    f'{bcolors.GREEN}'+
    f'8  - Visualizar todos os personagens\n'+
    f'9  - Visualizar um jogador\n'+
    f'10 - Visualizar um inimigo\n'+
    f'11 - Visualizar todas as habilidades\n'+
    f'12 - Visualizar inventários\n\n'+
    f'{bcolors.ENDC}'+
    f'13 - Atribuir habilidade\n'+
    f'14 - Combate\n'+
    f'15 - Compra e venda\n'+
    f'16 - Abrir baú\n'+
    f'17 - Definir turno\n'+
    f'18 - Decisão probabilística\n\n'+
    

    f'0  - Sair\n'
    )




# Main code
if __name__ == '__main__':
    print(bcolors.ENDC)

    # Create or load player
    players = create_players()

    # Create default enemies
    enemies = create_enemies()

    # Create or load abilities
    abilities = create_abilities(players)

    # Load all items
    items.load_items()

    # Start app execution
    while(True):
        clear()

        display_players(players)

        options()

        choice = int(input('Sua escolha: ') or 0)
        
        # Exit
        if choice == 0:
            clear()
            save(players)
            break

        # Create player
        elif choice == 1:
            clear()

            print('Criação de Jogador\n')
            new_player = create_character()
            players.append(new_player)

        # Create enemy
        elif choice == 2:
            clear()

            print('Criação de Inimigo\n')
            op = bool(input('Criação longa? [True/False]: '))

            if op:
                new_enemy = create_character()
            else:
                new_enemy = create_random_enemy()
                
            enemies.append(new_enemy)

        # Create an ability
        elif choice == 3:
            clear()
            print('Nova Habilidade\n')

            abilities.append(create_ability())

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Create Item
        elif choice == 4:
            clear()
            print('Criar Item\n')

            items.create_item()

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Remove a player
        elif choice == 5:
            clear()
            print('Remoção de Jogador')
            
            for i in range(len(players)):
                print(f'{i} - {players[i].name}')
            
            index = int(input('\nQual jogador você deseja remover: '))
            players.remove(players[index])

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Remove an enemy
        elif choice == 6:
            clear()
            print('Remoção de Inimigo')
            
            for i in range(len(enemies)):
                print(f'{i} - {enemies[i].name}')
            
            index = int(input('\nQual inimigo você deseja remover: '))
            enemies.remove(enemies[index])

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Remove all enemies
        elif choice == 7:
            clear()
            print('Limpar Lista de Inimigos')

            enemies.clear()

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # See all character
        elif choice == 8:
            clear()

            if players:
                print(f'{bcolors.GREEN}Jogadores{bcolors.ENDC}\n')
                
                for player in players:
                    print(player.name)

            if enemies:
                print(f'\n{bcolors.RED}Inimigos{bcolors.ENDC}\n')

                for enemy in enemies:
                    print(enemy.name)

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # See a player
        elif choice == 9:
            clear()
            print('Visualizar Jogador\n')

            for i in range(len(players)):
                print(f'{i} - {players[i].name}')
            
            index = int(input('\nQual jogador você deseja ver os detalhes [-1 para voltar]: '))

            if index == -1:
                continue

            print()
            players[index].show_details()

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # See an enemy
        elif choice == 10:
            clear()
            print('Visualizar Inimigo\n')

            for i in range(len(enemies)):
                print(f'{i} - {enemies[i].name}')
            
            index = int(input('\nQual inimigo você deseja ver os detalhes [-1 para voltar]: '))

            if index == -1:
                continue

            print()
            enemies[index].show_details()

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # See all abilities
        elif choice == 11:
            clear()
            print('Todas as Habilidades\n')

            option = int(input('Visualização completa ou simplificada? [1 - Completa/0 - Simplificada]: ') or 0)
            print()

            if option == 1:
                for ability in abilities:
                    print(25*'-=')
                    print()
                    ability.show_ability_details()
                    print()

                print(25*'-=')

            else:
                for ability in abilities:
                    print(ability.name)
                
            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        elif choice == 12:
            clear()
            print('Inventários\n')

            show_inventories(players)
            
            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Assign ability
        elif choice == 13:
            clear()
            print('Atribuir Habilidade\n')

            if int(input('Atribuir a um jogador? [1 - True/0 - False]: ')) == 1:                
                print('\nJogadores para atribuir:\n')
                for i in range(len(players)):
                    print(f'{i} - {players[i].name}')

                index = int(input('\nJogador para atribuir: '))                                               
                assign_ability(abilities, players[index])
            else:
                print('\nInimigos para atribuir:\n')
                for i in range(len(enemies)):
                    print(f'{i} - {enemies[i].name}')

                index = int(input('\nInimigo para atribuir: '))
                assign_ability(abilities, enemies[index])

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Combat
        elif choice == 14:
            current_turn = 0
            current_combat_abilities = list()

            clear()
            print('Definição de Turno\n')

            order = define_order(players, enemies)

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')
            index = 0

            while True:
                # Increase current turn and handle player order index
                current_turn += 1
                if index == len(order):
                    index = 0

                # Setup header (characters order)
                clear()
                print('Combate')
                print(f'\nTurno Atual - {current_turn}\n')

                # Separator
                print(25*'-=')
                print('\nOrdem\n')

                for i in range(len(order)):
                    print(f'{i+1}º - {order[i][0]}')

                print(f'\nVez de {bcolors.WARNING}{order[index][0]}{bcolors.ENDC}')


                # Separator
                print()
                print(25*'-=')


                # Display all players info
                print(f'\n{bcolors.GREEN}Jogadores{bcolors.ENDC}\n')
                print(f'   {bcolors.RED}Vida\t\t   {bcolors.CYAN}Mana\t\t {bcolors.GREEN}Stamina{bcolors.ENDC}\t AD\t AP\t TD\tNome\n')
                for player in players:
                    print(f'{bcolors.RED}{player.health:3d} / {player.base_health:3d}\t{bcolors.CYAN}{player.mana:3d} / {player.base_mana:3d}\t{bcolors.GREEN}{player.stamina:3d} / {player.base_stamina:3d}{bcolors.ENDC}\t{player.attack_damage:3d}\t{player.ability_power:3d}\t{player.true_damage:3d}\t{player.name}')


                # Display all enemies info
                print(f'\n{bcolors.RED}Inimigos{bcolors.ENDC}\n')
                print(f'   {bcolors.RED}Vida\t\t   {bcolors.CYAN}Mana\t\t {bcolors.GREEN}Stamina{bcolors.ENDC}\t AD\t AP\t TD\tNome\n')
                for enemy in enemies:
                    print(f'{bcolors.RED}{enemy.health:3d} / {enemy.base_health:3d}\t{bcolors.CYAN}{enemy.mana:3d} / {enemy.base_mana:3d}\t{bcolors.GREEN}{enemy.stamina:3d} / {enemy.base_stamina:3d}{bcolors.ENDC}\t{enemy.attack_damage:3d}\t{enemy.ability_power:3d}\t{enemy.true_damage:3d}\t{enemy.name}')


                # Separator
                print()
                print(25*'-=')
                print()


                # Combat handler
                result = combat(current_turn, players, enemies, current_combat_abilities)
                if result == -2:
                    break

                # Increase player order index
                index += 1

                # If all the enemies dies, stop combat
                if not enemies:
                    break

            # Remove all temporary buffs, given by the abilities, and reset stamina
            remove_buffs(current_combat_abilities, players)
            reset_stamina(players)
                      
        # Buy and sell system
        elif choice == 15:
            commertiant(players)

        # Open a chest
        elif choice == 16:
            clear()
            print('Abrir Baú')
            loot_chest()

        # Define turn order
        elif choice == 17:
            clear()
            print('Definição de Turno\n')
            define_order(players, enemies)

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Probabilistic decision
        elif choice == 18:
            clear()
            print('Decisão Probabilística\n')

            decision()

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        elif choice == 19:
            clear()
            print('Savando Dados...\n')

            save(players)

            print('Dados salvos!\n')

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')