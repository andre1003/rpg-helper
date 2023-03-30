# Imports
import os
import shutil
from random import randint, uniform
import items
from character import Character
from ability import Ability
from utils import bcolors, d
from combat import *
from creation import *




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

    # Get random number of coins and ores
    coins = randint(min_coins, max_coins)
    ores = randint(1, 3)

    # Get number of loots that the chest will have
    percents = (coin_percent, item_percent, ore_percent, weed_percent)
    maximum = sum(p > 0 for p in percents)
    loot_number = randint(1, maximum)

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
                print(f'+{coins} moedas')
                player.coins += coins
                
            # Items
            elif index == 1:
                item = items.get_item_at_index(player.character_class)
                print(f'+{item}')

            # Ore
            elif index == 2:
                ore = items.ores[randint(0, len(items.ores) - 1)]
                print(f'+{ores} de {ore.name}')
                items.items[player.character_class].append(ore)

            # Weed
            elif index == 3:
                print('+1 Erva de cura simples')

    print(25*'=-')

    # Press any key to continue
    input('\nPressione qualquer tecla para continuar...')


# Edit a character
def edit(all_characters: list, option: int):
    print()
    print(25*'-=')
    print()

    for i in range(len(all_characters)):
        print(f'{i} - {all_characters[i].name}')

    opt = int(input('\nQual personagem você quer alterar: ') or -1)
    if opt == -1:
        return

    character = all_characters[opt]

    # Status
    health = int(input(f'Adicionar Vida [{character.health} / {character.base_health}]: ') or 0)
    mana = int(input(f'Adicionar Mana [{character.mana} / {character.base_mana}]: ') or 0)
    stamina = int(input(f'Adicionar Stamina [{character.stamina} / {character.base_stamina}]: ') or 0)

    # Damage
    attack_damage = int(input(f'Adicionar Dano de Ataque [{character.attack_damage} / {character.base_attack_damage}]: ') or 0)
    ability_power = int(input(f'Adicionar Dano Mágico [{character.ability_power} / {character.base_ability_power}]: ') or 0)
    true_damage = int(input(f'Adicionar Dano Verdadeiro [{character.true_damage} / {character.base_true_damage}]: ') or 0)

    # Buff status
    if option == 1:
        character.buff_status(health, mana, stamina)
        character.buff_damage(attack_damage, ability_power, true_damage)

    # Edit permanently
    else:
        character.edit_status(health, mana, stamina)
        character.edit_damage(attack_damage, ability_power, true_damage)

    print()
    print(25*'-=')
    print()


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
def commertiant(players: list, no_charge: bool):
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
                if not no_charge:
                    players[opt].coins -= commertiant_items[option].price
                items.items[players[opt].character_class].append(commertiant_items[option])
                save(players)
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

    path = 'abilities/'
    if not os.path.exists(path):
        os.mkdir(path)

    ability = Ability(name, health_cost, mana_cost, stamina_cost, additional_attack_damage, additional_ability_power, additional_true_damage, additional_health, additional_mana, additional_stamina, is_unic_use, cooldown, affect_other_player, number_of_enemies_affected, no_dice, is_attack, min_dice_value)

    name = ability.name.replace(' ','_')
    file = open(f'{path}/{name}.txt', 'w')
    file.writelines(ability.get_data())
    file.close()

    return ability


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


# Level up system
def level_up(players: list):
    initial_xp = 200
    xp_multiplier = 0.15
    damage_multiplier = 0.15

    for player in players:
        if player.name == 'Celaena':
            damage_multiplier = 0.153
        elif player.name == 'Ryze' or player.name == 'Nikolag':
            damage_multiplier = 0.155

        level = int(input(f'\nQual o nível de {player.name}: '))

        file = open('xp-cost.txt', 'r')
        content = file.readlines()
        file.close()

        content = [int(i) for i in content]

        while player.xp >= content[level-1]:
            player.xp -= content[level-1]
            level += 1

            if 50 > level >= 20:
                damage_multiplier -= 0.06

            elif 80 > level >= 50:
                damage_multiplier -= 0.05

            elif level >= 80:
                damage_multiplier -= 0.025

            player.attack_damage += round(damage_multiplier * player.attack_damage)
            player.ability_power += round(damage_multiplier * player.ability_power)
            player.true_damage += round(damage_multiplier * player.true_damage)

        print(f'{bcolors.CYAN}{player.name}{bcolors.ENDC} upou para o nível {bcolors.GREEN}{level}{bcolors.ENDC}')

        save(players)


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
    f'18 - Decisão probabilística\n'+
    f'19 - Salvar dados\n'+
    f'20 - Editar jogadores\n'+
    f'21 - Adicionar moedas e XP\n'+
    f'22 - Definir moedas e XP\n'+
    f'23 - Adicionar item\n'+
    f'24 - Resetar atributos\n' +
    f'25 - Recarregar inimigos (pasta temp)\n\n' +
    

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
    items.load_items(players)


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

            # If there is no temp directory, create it
            path = 'temp/'
            if not os.path.exists(path):
                os.mkdir(path)

            op = bool(input('Criação longa? [True/False]: '))

            if op:
                new_enemy = create_character()
            else:
                new_enemy = create_random_enemy()

            # Create player directory if needed
            path = f'temp/{new_enemy.name}/'
            if not os.path.exists(path):
                os.mkdir(path)

            # Save player data
            file = open(f'{path}enemy.txt', 'w')
            file.writelines(new_enemy.get_data())
            file.close()
                
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

            path = 'temp/' + enemies[index].name
            if os.path.exists(path):
                shutil.rmtree(path)

            enemies.remove(enemies[index])

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Remove all enemies
        elif choice == 7:
            clear()
            print('Limpar Lista de Inimigos')

            shutil.rmtree('temp/')
            os.mkdir('temp/')
            
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

        # Show inventories
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
            path = 'temp/'
            if not os.path.exists(path):
                os.mkdir(path)

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
                result = combat(current_turn, players, enemies, current_combat_abilities, order)
                if result == -2:
                    break
                elif result > 0:
                    order.remove(order[result])

                # Increase player order index
                index += 1

                # If all the enemies dies, stop combat
                if not enemies:
                    # Clear temporary files
                    shutil.rmtree('temp/')
                    break

            # Remove all temporary buffs, given by the abilities, and reset stamina
            remove_buffs(current_combat_abilities, players)
            reset_stamina(players)
                      
        # Buy and sell system
        elif choice == 15:
            commertiant(players, False)

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

        # Save
        elif choice == 19:
            clear()
            print('Savando Dados...\n')

            save(players)

            print('Dados salvos!\n')

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Edit a player
        elif choice == 20:
            clear()
            print('Editar Jogador\n')

            # Remove items buffs
            items.remove_items_buffs(players)

            # Edit players
            while True:
                edit(players, 2)
                opt = int(input('\nDeseja editar outro jogador? [1 - True/0 - False] ') or 0)
                if opt == 0:
                    break

            # Apply items buffs
            items.apply_items_buffs(players)

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Add coins and XP
        elif choice == 21:
            clear()
            print('Adicionar XP e Moedas\n')

            add_coins = int(input('Moedas para adicionar: '))
            add_xp = int(input('XP para adicionar: '))

            print()

            for i in range(len(players)):
                print(f'{i} - {players[i].name}')

            index = int(input('\nIndex do jogador [-1 para todos]: '))

            if index == -1:
                for player in players:
                    player.coins += add_coins
                    player.xp += add_xp
            else:
                players[index].coins += add_coins
                players[index].xp += add_xp

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Set coins and XP
        elif choice == 22:
            clear()
            print('Set de XP e Moedas\n')

            xp = int(input('XP: '))
            coins = int(input('Moedas: '))

            print()

            for i in range(len(players)):
                print(f'{i} - {players[i].name}')

            index = int(input('\nIndex do jogador [-1 para todos]: '))

            if index == -1:
                for player in players:
                    player.coins = coins
                    player.xp = xp
            else:
                players[index].coins = coins
                players[index].xp = xp

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Add item to inventory
        elif choice == 23:
            commertiant(players, True)

        # Reset stats
        elif choice == 24:
            clear()
            print('Resetar Atributos\n')

            # Remove item buffs
            items.remove_items_buffs(players)

            # Check wich status should be reset
            restore_health = int(input('Restaurar vida? [1 - True / 0 - False] (Padrão é False): ') or 0)
            restore_mana = int(input('Restaurar mana? [1 - True / 0 - False] (Padrão é True): ') or 1)
            restore_stamina = int(input('Restaurar stamina? [1 - True / 0 - False] (Padrão é True): ') or 1)

            print('\nOs seguintes atributos serão resetados:\n')

            if restore_health == 1:
                print(f'{bcolors.RED}Vida{bcolors.ENDC}')

            if restore_mana == 1:
                print(f'{bcolors.CYAN}Mana{bcolors.ENDC}')

            if restore_stamina == 1:
                print(f'{bcolors.GREEN}Stamina{bcolors.ENDC}')

            print()

            # Reset status
            for player in players:
                if restore_health == 1:
                    player.health = player.base_health

                if restore_mana == 1:
                    player.mana = player.base_mana

                if restore_stamina == 1:
                    player.stamina = player.base_stamina

            # Reapply item buffs
            items.apply_items_buffs(players)

            print('\nAtributos resetados com sucesso!')

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Reload temp directory
        elif choice == 25:
            clear()
            print('Carregar Inimigos\n')

            enemies = create_enemies()

            print('Inimigos existentes:\n')
            for enemy in enemies:
                print(enemy.name)

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        elif choice == 26:
            clear()
            print('Carregar Inimigos')

            items.remove_items_buffs(players)
            level_up(players)
            items.apply_items_buffs(players)

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')