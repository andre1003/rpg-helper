import os
from random import randint, uniform
import items


# Terminal colors class
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Character class
class Character:
    # Name
    name = "Generic Name"

    # Class
    character_class = ""

    # Status
    health = 100
    mana = 100
    stamina = 100

    # Damage
    attack_damage = 0
    ability_power = 0
    true_damage = 0

    # Damage negation
    attack_damage_negation = 0
    ability_power_negation = 0

    # Attack dice
    attack_dice_number = 1
    attack_dice_value = 6

    # Defence dice
    defense_dice_number = 1
    defense_dice_value = 6

    # Additional dice for ability
    additional_ability_dice = 1


    # Constructor
    def __init__(self, name, character_class, health, mana, stamina, attack_damage, ability_power, true_damage, attack_damage_negation, ability_power_negation, attack_dice_number, attack_dice_value, defense_dice_number, defense_dice_value, additional_ability_dice):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.attack_damage = attack_damage
        self.ability_power = ability_power
        self.true_damage = true_damage
        self.attack_damage_negation = attack_damage_negation
        self.ability_power_negation = ability_power_negation
        self.attack_dice_number = attack_dice_number
        self.attack_dice_value = attack_dice_value
        self.defense_dice_number = defense_dice_number
        self.defense_dice_value = defense_dice_value
        self.additional_ability_dice = additional_ability_dice


    # Set status
    def set_status(self, health, mana, stamina):
        self.health = health
        self.mana = mana
        self.stamina = stamina

    # Set damage
    def set_damage(self, attack_damage, ability_power, true_damage):
        self.attack_damage = attack_damage
        self.ability_power = ability_power
        self.true_damage = true_damage

    # Set damage negation
    def set_damage_negation(self, attack_damage_negation, ability_power_negation):
        self.attack_damage_negation = attack_damage_negation
        self.ability_power_negation = ability_power_negation

    # Set dice
    def set_dice(self, attack_dice_number, attack_dice_value, defence_dice_number, defence_dice_value, additional_ability_dice):
        self.attack_dice_number = attack_dice_number
        self.attack_dice_value = attack_dice_value
        self.defence_dice_number = defence_dice_number
        self.defence_dice_value = defence_dice_value
        self.additional_ability_dice = additional_ability_dice

    def show_details(self):
        print(f'Nome: {self.name}')
        print(f'Classe: {self.character_class}')
        print()
        print(f'{bcolors.RED}Vida: {self.health}{bcolors.ENDC}')
        print(f'{bcolors.CYAN}Mana: {self.mana}{bcolors.ENDC}')
        print(f'{bcolors.GREEN}Stamina: {self.stamina}{bcolors.ENDC}')
        print()
        print(f'{bcolors.RED}Dano de Ataque: {self.attack_damage}{bcolors.ENDC}')
        print(f'{bcolors.CYAN}Dano Mágico: {self.ability_power}{bcolors.ENDC}')
        print(f'Dano Verdadeiro: {self.true_damage}')
        print()
        print(f'{bcolors.RED}Negação de Dano de Ataque: {self.attack_damage_negation}{bcolors.ENDC}')
        print(f'{bcolors.CYAN}Negação de Dano Mágico: {self.ability_power_negation}{bcolors.ENDC}')
        print()
        print(f'{bcolors.RED}Dados de Ataque: {self.attack_dice_number}d{self.attack_dice_value}{bcolors.ENDC}')
        print(f'{bcolors.CYAN}Dados de Defesa: {self.defense_dice_number}d{self.defense_dice_value}{bcolors.ENDC}')
        print()
        print(f'{bcolors.WARNING}Quantidade de Dados Adicionais para Habilidade: {self.additional_ability_dice}{bcolors.ENDC}')





# Roll a dice
def d(number: int):
    return randint(1, number)


# Calculate damage
def calculate_damage(attacker: Character, defender: Character):
    print(25*'=-')

    print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} X {bcolors.RED}{defender.name}{bcolors.ENDC}\n\n')
    
    print(f'{bcolors.GREEN}{attacker.name} ataca!{bcolors.ENDC}\n')

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
    for i in range(defender.defense_dice_number):
        dice_value = d(defender.defense_dice_value)
        defender_ad_dice += dice_value

        print(f'{defender.name} rolou 1d{defender.defense_dice_value} para AD e tirou: \t{dice_value}')
    print(f'\t>> Total dos dados de defesa AD de {defender.name}: {defender_ad_dice}\n')

    # Defender AP negation
    defender_ap_dice = 0
    for i in range(defender.defense_dice_number):
        dice_value = d(defender.defense_dice_value)
        defender_ap_dice += dice_value

        print(f'{bcolors.CYAN}{defender.name} rolou 1d{defender.defense_dice_value} para AP e tirou: \t{dice_value}{bcolors.ENDC}')
    print(f'\t{bcolors.CYAN}>> Total dos dados de defesa AP de {defender.name}: {defender_ap_dice}{bcolors.ENDC}\n\n\n\n')


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
    if ad_damage < 0:
        print(f'{bcolors.RED}{defender.name}{bcolors.ENDC} defendeu o Dano de Ataque!')
        ad_damage = 0
    else:
        print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} acertou o Dano de Ataque!')


    # If the defender armor was greater than attacker AP, set ap_damage to 0
    if ap_damage < 0:
        print(f'{bcolors.RED}{defender.name}{bcolors.ENDC} defendeu o {bcolors.CYAN}Dano Mágico{bcolors.ENDC}!\n')
        ap_damage = 0
    else:
        print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} acertou o {bcolors.CYAN}Dano Mágico{bcolors.ENDC}!\n')


    # Calculate final damage
    final_damage = ad_damage + ap_damage + td_damage
    print(f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} aplicou:\n\tDano do Ataque: {ad_damage}\n\tDano Mágico: {ap_damage}\n\tDano Verdadeiro: {td_damage}\n\t{bcolors.RED}Dano Total: {final_damage}{bcolors.ENDC}')

    print(25*'=-')

    # Return final damage
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

    # Set dice
    attack_dice_number = int(input('Quantidade de Dados de Ataque: '))
    attack_dice_value = int(input('Valor dos Dados de Ataque: '))

    defense_dice_number = int(input('Quantidade de Dados de Defesa: '))
    defense_dice_value = int(input('Valor dos Dados de Defesa: '))

    additional_ability_dice = int(input('Quantidade de Dados Adicionais para Habilidade: '))

    # Return character
    return Character(name, character_class, health, mana, stamina, attack_damage, ability_power, true_damage, attack_damage_negation, ability_power_negation, attack_dice_number, attack_dice_value, defense_dice_number, defense_dice_value, additional_ability_dice)


# Create known players
def create_players():
    # Create players
    spark = Character("Spark", "Druida", 59, 39, 59, 7, 29, 5, 5, 7, 1, 8, 1, 8, 1)
    nikolag = Character("Nikolag", "Bárbaro", 43, 33, 22, 16, 7, 5, 7, 3, 1, 12, 1, 12, 1)
    celaena = Character("Celaena", "Bardo", 42, 50, 11, 10, 15, 2, 5, 5, 1, 8, 1, 8, 1)
    ryze = Character("Ryze", "Mago", 73, 34, 49, 8, 13, 4, 3, 7, 1, 6, 1, 6, 1)
    flugel = Character("Flugel", "Paladino", 93, 14, 32, 20, 18, 6, 7, 3, 1, 10, 1, 10, 1)

    # Return players
    return  [spark, nikolag, celaena, ryze, flugel]


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
    for character in order:
        print(character[0])

    # Press any key to continue
    input('\nPressione qualquer tecla para continuar...')
    

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


# Combat handler
def combat(players: list, enemies:list):
    all_chacters = players.copy() + enemies.copy()
            
    for i in range(len(all_chacters)):
        print(f'{i} - {all_chacters[i].name}')

    print()

    attacker = all_chacters[int(input('Escolha o atacante: '))]
    defender = all_chacters[int(input('Escolha o defensor: '))]

    print()

    damage = calculate_damage(attacker, defender)

    # Press any key to continue
    input('\nPressione qualquer tecla para continuar...')


# Commertiant handler
def commertiant():
    # Get the commertiant type
    option = input('Qual o tipo de comerciante: ').upper()

    print()

    # Init commertiant items
    commertiant_items = list()

    # Merchant
    if option == 'MERCADOR':
        commertiant_items = items.merchant_items

    # Market
    elif option == 'MERCADO':
        commertiant_items = items.market_items

    # Big market
    elif option == 'MERCADÃO' or option == 'MERCADAO':
        commertiant_items = items.big_market_items

    # Blacksmith
    elif option == 'FERREIRO':
        commertiant_items = items.blacksmith_items

    # Stable
    elif option == 'ESTÁBULO' or option == 'ESTABULO':
        commertiant_items = items.stable_items  

    # Alchemist
    elif option == 'ALQUIMISTA':
        commertiant_items = items.alchemist_items

    # Jewelry
    elif option == 'JOALHERIA':
        commertiant_items = items.jewelry_items

    # Show items and prices
    for item in commertiant_items:
        price = f'{item[1]:,}'.replace(',', '.')
        print(f'{item[0]} - ${price}')

    # Press any key to continue
    input('\nPressione qualquer tecla para continuar...')


# Display all players
def display_players(players: list):
    print('Jogadores existentes:\n')
    for player in players:
        print(player.name)

    print('\n')


# Decision


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
    print('1  - Adicionar jogador\n2  - Adicionar inimigo\n3  - Definir turno\n4  - Remover jogador\n5  - Remover inimigo\n6  - Limpar inimigos\n7  - Combate\n8  - Abrir baú\n9  - Compra e venda\n10 - Mostrar todos os personagens\n11 - Visualizar um jogador\n12 - Visualizar um inimigo\n0  - Sair\n')




# Main code
if __name__ == '__main__':
    players = create_players()
    enemies = list()

    while(True):
        clear()

        display_players(players)

        options()

        choice = int(input('Sua escolha: '))
        
        # Exit
        if choice == 0:
            clear()
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

        # Define turn order
        elif choice == 3:
            clear()
            print('Definição de Turno\n')
            define_order(players, enemies)

        # Remove a player
        elif choice == 4:
            clear()
            print('Remoção de Jogador')
            
            for i in range(len(players)):
                print(f'{i} - {players[i].name}')
            
            index = int(input('\nQual jogador você deseja remover: '))
            players.remove(players[index])

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Remove an enemy
        elif choice == 5:
            clear()
            print('Remoção de Inimigo')
            
            for i in range(len(enemies)):
                print(f'{i} - {enemies[i].name}')
            
            index = int(input('\nQual inimigo você deseja remover: '))
            enemies.remove(enemies[index])

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')

        # Clean enemies list
        elif choice == 6:
            clear()
            print('Limpar Lista de Inimigos')

            enemies.clear()

            # Press any key to continue
            input('\nPressione qualquer tecla para continuar...')
            
        # Combat
        elif choice == 7:
            clear()
            print('Combate')
            combat(players, enemies)
            
        # Open a chest
        elif choice == 8:
            clear()
            print('Abrir Baú')
            loot_chest()

        # Buy and sell system
        elif choice == 9:
            clear()
            print('Compra e Venda')
            commertiant()

        # Display all character
        elif choice == 10:
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
        elif choice == 11:
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
        elif choice == 12:
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