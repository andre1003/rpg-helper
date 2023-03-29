from utils import bcolors
import os
from random import randint
import character


class Item:
    def __init__(self, name, description='', price=-1,
    additional_health=0, additional_mana=0, additional_stamina=0,
    additional_attack_damage=0, additional_ability_power=0, additional_true_damage=0, 
    additional_ad_negation=0, additional_ap_negation=0,
    stamina_cost=0,
    is_weapon=False):

        self.name = name
        self.description = description
        self.price = price
        
        self.additional_health = additional_health
        self.additional_mana = additional_mana
        self.additional_stamina = additional_stamina

        self.additional_attack_damage = additional_attack_damage
        self.additional_ability_power = additional_ability_power
        self.additional_true_damage = additional_true_damage

        self.additional_ad_negation = additional_ad_negation
        self.additional_ap_negation = additional_ap_negation

        self.stamina_cost = stamina_cost

        self.is_weapon = is_weapon

    def get_data(self):
        data = ''

        data += str(self.name) + '\n'
        data += str(self.description) + '\n'
        data += str(self.price) + '\n'
        
        data += str(self.additional_health) + '\n'
        data += str(self.additional_mana) + '\n'
        data += str(self.additional_stamina) + '\n'

        data += str(self.additional_attack_damage) + '\n'
        data += str(self.additional_ability_power) + '\n'
        data += str(self.additional_true_damage) + '\n'

        data += str(self.additional_ad_negation) + '\n'
        data += str(self.additional_ap_negation) + '\n'

        data += str(self.stamina_cost) + '\n'

        data += str(self.is_weapon)

        return data




items = {
    'Bárbaro': [
        Item(name='Machado Grande', additional_attack_damage=3, stamina_cost=3, is_weapon=True),
        Item(name='Adagas Curtas', additional_attack_damage=1, stamina_cost=1, is_weapon=True),
        Item(name='Armadura de Prata Pesada', additional_ad_negation=5, additional_ap_negation=5, is_weapon=False),
    ],


    'Bardo': [
        Item(name='Faca Pequena', additional_attack_damage=1, stamina_cost=1, is_weapon=True),
        Item(name='Roupa de Bardo', additional_ad_negation=1, additional_ap_negation=1, is_weapon=False),
    ],
    
    
    'Druida': [
        Item(name='Trapo Simples', additional_ap_negation=2, is_weapon=False),
    ],
    
    
    'Mago': [
        Item(name='Cajado Simples', additional_ability_power=2, stamina_cost=2, is_weapon=True),
        Item(name='Manto Furado', additional_ad_negation=1, additional_ap_negation=2, is_weapon=False),
    ],
    
    
    'Paladino': [
        Item(name='Espada Média', additional_attack_damage=5, stamina_cost=3, is_weapon=True),
        Item(name='Escudo Médio', additional_ad_negation=5, additional_ap_negation=4, is_weapon=False),
    ],
}


loot_items = {
    'Bárbaro': [
        Item(name='', additional_attack_damage=0, stamina_cost=0, is_weapon=True),
    ],


    'Bardo': [
        Item(name='', additional_attack_damage=0, stamina_cost=0, is_weapon=True),
    ],
    
    
    'Druida': [
        Item(name='', additional_attack_damage=0, stamina_cost=0, is_weapon=True),
    ],
    
    
    'Mago': [
        Item(name='', additional_attack_damage=0, stamina_cost=0, is_weapon=True),
    ],
    
    
    'Paladino': [
        Item(name='', additional_attack_damage=0, stamina_cost=0, is_weapon=True),
    ],
}




merchant_items = [
    Item(name='Erva de cura simples', description='Erva usada para fabricar poções de cura simples', price=5),
    Item(name='Faca de dissecar cega', description='Faca para dissecar animais de caça', price=15),
    Item(name='Pedra de afiar espadas', description='Pedra usada para afiars espadas, deixando-as mais fortes temporariamente', price=35),
    Item(name='Erva de cura de envenamento', description='Erva usada para realizar elixires de cura de envenenamento', price=5),
    Item(name='Álcool', description='Álcool pode ter diversas utilidades, como limpeza de armas e armaduras, fabricação de poções e elixires, etc.', price=12),
]

market_items = [
    Item(name='Maçã', description='Recupera 2 HP', price=2),
    Item(name='Banana', description='Recupera 2 HP', price=2),
    Item(name='Carne de cervo', description='Recupera 20 HP e 5 de mana', price=40),
    Item(name='Carne de boi', description='Recupera 25 HP e 25 de mana', price=55),
    Item(name='Vinho', description='Recupera 5 HP e 10 de mana', price=10),
]

big_market_items = [
    Item(name='Pedra de encantamento mágico de arma simples', description='Pedra usada para inflingir dano mágico em uma determinada arma', price=210),
    Item(name='Cimitarra', description='Inflinge 15 de Dano de Ataque e 3 de Dano Verdadeiro adicionais', price=150),
    Item(name='Cajado de Orvalho superior', description='Aumenta a Mana em 12 pontos e infinge 15 de Dano Mágico adicional', price=1200),
    Item(name='Anel de Cura Superior', description='Aplica um cura de 15 HP no usuário em cada turno. Ao final de cada combate, recupera 40 HP para todos os jogadores', price=500),
    Item(name='Barraca de acampamento simples', description='Útil para longas viagens. Abriga 1 pessoa', price=120),
]

blacksmith_items = [
    Item(name='Espada Curva Fortificada', description='Causa 7 de Dano de Ataque adicional ao custo de 1 de stamina', additional_attack_damage=7, stamina_cost=1, is_weapon=True, price=2000),
    Item(name='Machado Grande Superior', description='Causa 15 de Dano de Ataque adicional ao custo de 5 de stamina', additional_attack_damage=15, stamina_cost=5, is_weapon=True, price=3000),
    Item(name='Cajado de Ouro Simples', description='Causa 5 de Dano Mágico adicional ao custo de 5 de stamina', additional_ability_power=5, stamina_cost=5, is_weapon=True, price=2500),
    Item(name='Adaga Dracônica Superior', description='Causa 10 de Dano de Ataque, Dano Mágico e Dano Verdadeiro adicional ao custo de 4 de stamina', additional_attack_damage=10, additional_ability_power=10, additional_true_damage=10, stamina_cost=4, is_weapon=True, price=23000),
    Item(name='Selo de Dedo Real', description='Causa 25 de Dano de Ataque e Dano Mágico adicional ao custo de 5 de stamina', additional_attack_damage=25, additional_ability_power=25, stamina_cost=5, is_weapon=True, price=20000),
    Item(name='Elmo de Prata Smaragdoriano Fortificado', description='Adiciona 20 de Negação de Dano de Ataque', additional_ad_negation=20, is_weapon=False, price=9000),
    Item(name='Peitoral de Prata Smaragdoriano Fortificado', description='Adiciona 25 de Negação de Dano de Ataque e Negação de Dano Mágico', additional_ad_negation=25, additional_ap_negation=25, is_weapon=False, price=18000),
    Item(name='Grevas de Prata Smaragdoriana Fortificada', description='Adiciona 15 de Negação de Dano de Ataque', additional_ad_negation=15, is_weapon=False, price=7500),
]

stable_items = [
    Item(name='Pangaré', description='Consegue andar uma distância considerável (50m) sem se cansar', price=3000),
    Item(name='Cavalo treinado', description='Consegue andar uma longa distância (100m) sem se cansar', price=6000),
    Item(name='Burro de carga', description='Consegue levar uma carga considerável de itens (20 itens)', price=3500),
    Item(name='Cavalo de elite', description='Consegue andar livremente sem se cansar (sem limite)', price=50000),
    Item(name='Carroça com 4 cavalos', description='Consegue levar cargas muito pesadas (100 itens) sem se cansar', price=250000),
]

alchemist_items = [
    Item(name='Erva de cura simples', description='Erva usada para fabricar poções de cura simples', price=2),
    Item(name='Erva de cura de envenenamento', description='Erva usada para realizar elixires de cura de envenenamento', price=5),
    Item(name='Receita de poção de cura', description='Receita para fabricar poção de cura', price=50),
    Item(name='Receita de poção de força', description='Receita para fabricar poção de força', price=65),
    Item(name='Kit de poções básicas', description='Kit contendo 5 poções de cura simples e 5 poções de mana simples', price=250),
]

jewelry_items = [
    Item(name='Minério de prata refinado', description='Usado para forjar espadas e escudos e armaduras', price=100),
    Item(name='Minério de ouro refinado', description='Usado para fabricar itens diversos', price=1500),
    Item(name='Colar de diamante', description='Sem nenhuma utilidade específica, mas é muito bonito!', price=350000),
    Item(name='Minério de diamante bruto', description='Precisa ser refinado para ser utilizado', price=5000),
    Item(name='Rubi', description='Jóia extremamente rara de se encontrar. Pode ser utilizada em alguns itens mágicos', price=120000),
]




ores = [
    Item(name='Minério de cobre', description='Deve ser refinado para ser utilizado', price=30),
    Item(name='Minério de ferro', description='Deve ser refinado para ser utilizado', price=45),
    Item(name='Minério de prata', description='Deve ser refinado para ser utilizado', price=60),
    Item(name='Minério de ouro', description='Deve ser refinado para ser utilizado', price=95),
    Item(name='Minério de diamante', description='Deve ser refinado para ser utilizado', price=175),
    Item(name='Minério de rubi', description='Deve ser refinado para ser utilizado', price=250),
    Item(name='Minério de esmeralda', description='Deve ser refinado para ser utilizado', price=390),
    Item(name='Minério de safira', description='Deve ser refinado para ser utilizado', price=500),
]


merchants = (
    'Mercador',
    'Mercado',
    'Mercadão',
    'Ferreiro',
    'Estábulo',
    'Alquimista',
    'Joalheiro'
)

item_levels = (
    'Simples',
    'Fortificado',
    'Superior',
    'Real',
    'Mestre',
    'Grão-Mestre',
    'Obra-Prima',
    'Supremo',
    'Divino'
)




# Get player item at index
def get_item_at_index(character_class:str):
    return loot_items[character_class][randint(0, len(loot_items[character_class]))]


# Create an item
def create_item():
    # Item info
    name = input('Insira o nome do item: ')
    description = input('Insira a descrição do item: ')
    price = int(input('Insira o valor do item: '))
    item = Item(name=name, description=description, price=price)

    print()

    # Get the correct commertiant to add the item
    for i in range(len(merchants)):
        print(f'{i} - {merchants[i]}')
    option = int(input('\nQual mercador irá vender o item: '))

    # Merchant
    if option == 0:
        merchant_items.append(item)
    
    # Market
    elif option == 1:
        market_items.append(item)

    # Big market
    elif option == 2:
        big_market_items.append(item)

    # Blacksmith
    elif option == 3:
        blacksmith_items.append(item)

    # Stable
    elif option == 4:
        stable_items.append(item)

    # Alchemist
    elif option == 5:
        alchemist_items.append(item)

    # Jewelry
    elif option == 6:
        jewelry_items.append(item)

    # Display success message
    print(f'\nO item {bcolors.CYAN}{name}{bcolors.ENDC} foi adicionado ao inventário do {bcolors.GREEN}{merchants[option]}{bcolors.ENDC}')


# Save all player items
def save_player_items():
    # Check if path exists and create it if needed
    path = 'saves/Items/'
    if not os.path.exists(path):
        os.mkdir(path)

    # Loop character classes
    for char_class in items:
        # Loop player items
        for item in items[char_class]:
            # Create the directory if needed
            if not os.path.exists(path + f'{char_class}/'):
                os.mkdir(path + f'{char_class}/')

            # Save item
            name = path + f'{char_class}/' + item.name.replace(' ', '_') + '.txt'
            file = open(name, 'w')
            file.writelines(item.get_data())
            file.close()
    

# Load all player items from files, if possible
def load_player_items():
    # Check if path exists and exit if it does not
    path = 'saves/Items/'
    if not os.path.exists(path):
        return
    
    # Loop characters class
    for char_class in items:
        item_list = list()

        # Loop items
        for item in os.listdir(path + char_class + '/'):
            print(item)
            # Get item raw content
            file = open(path + char_class + '/' + item, 'r')
            content = file.readlines()
            file.close()

            # Configure content
            for i in range(len(content)):
                # Remove all '\n'
                content[i] = content[i].replace('\n', '')

                # Convert the needed content to integer
                if i > 1 and i < len(content) - 1:
                    content[i] = int(content[i])

                # Convert the needed content to boolean
                elif i == len(content) - 1:
                    if content[i] == 'True':
                        content[i] = True
                    else:
                        content[i] = False

            # Create new item and add it o item list
            new_item = Item(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7], content[8], content[9], content[10], content[11], content[12])
            item_list.append(new_item)
        
        # Assing the list to the dictionary
        items[char_class] = item_list


# Save all commertiant items
def save_commertiant_items():
    # Check if path exists and create it if needed
    path = 'saves/Commertiants/'
    if not os.path.exists(path):
        os.mkdir(path)

    # Loop commertiants and create the needed paths
    for commertiant in merchants:
        if not os.path.exists(path + commertiant + '/'):
            os.mkdir(path + commertiant + '/')

    # Save merchant items
    for item in merchant_items:
        name = item.name.replace(' ', '_')
        file = open(path + merchants[0] + f'/{name}.txt', 'w')
        file.writelines(item.get_data())
        file.close()

    # Save market items    
    for item in market_items:
        name = item.name.replace(' ', '_')
        file = open(path + merchants[1] + f'/{name}.txt', 'w')
        file.writelines(item.get_data())
        file.close()

    # Save big market items
    for item in big_market_items:
        name = item.name.replace(' ', '_')
        file = open(path + merchants[2] + f'/{name}.txt', 'w')
        file.writelines(item.get_data())
        file.close()

    # Save blacksmith items
    for item in blacksmith_items:
        name = item.name.replace(' ', '_')
        file = open(path + merchants[3] + f'/{name}.txt', 'w')
        file.writelines(item.get_data())
        file.close()

    # Save stable items
    for item in stable_items:
        name = item.name.replace(' ', '_')
        file = open(path + merchants[4] + f'/{name}.txt', 'w')
        file.writelines(item.get_data())
        file.close()

    # Save alchemist items
    for item in alchemist_items:
        name = item.name.replace(' ', '_')
        file = open(path + merchants[5] + f'/{name}.txt', 'w')
        file.writelines(item.get_data())
        file.close()

    # Save jewelry items
    for item in jewelry_items:
        name = item.name.replace(' ', '_')
        file = open(path + merchants[6] + f'/{name}.txt', 'w')
        file.writelines(item.get_data())
        file.close()


# Load all commertiant items, if possible
def load_commertiant_items():
    # Check if path exists and exit if it does not
    path = 'saves/Commertiants/'
    if not os.path.exists(path):
        return

    # Clear all commertiant lists
    merchant_items.clear()
    market_items.clear()
    big_market_items.clear()
    blacksmith_items.clear()
    stable_items.clear()
    alchemist_items.clear()
    jewelry_items.clear()

    # Loop all commertiants
    for commertiant in merchants:
        # Loop all items
        for item in os.listdir(path + commertiant):
            # Get item raw content
            file = open(path + commertiant + f'/{item}', 'r')
            content = file.readlines()
            file.close()

            # Configure item content
            for i in range(len(content)):
                # Remove all '\n'
                content[i] = content[i].replace('\n', '')

                # Convert the needed content to integer 
                if i > 1 and i < len(content) - 1:
                    content[i] = int(content[i])

                # Convert the needed content to boolean
                elif i == len(content) - 1:
                    if content[i] == 'True':
                        content[i] = True
                    else:
                        content[i] = False

            # Create new item
            new_item = Item(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7], content[8], content[9], content[10], content[11], content[12])

            # Add the new item to merchant
            if commertiant == merchants[0]:
                merchant_items.append(new_item)

            # Add the new item to market            
            elif commertiant == merchants[1]:
                market_items.append(new_item)

            # Add the new item to big market
            elif commertiant == merchants[2]:
                big_market_items.append(new_item)

            # Add the new item to blacksmith
            elif commertiant == merchants[3]:
                blacksmith_items.append(new_item)

            # Add the new item to stable
            elif commertiant == merchants[4]:
                stable_items.append(new_item)

            # Add the new item to alchemist
            elif commertiant == merchants[5]:
                alchemist_items.append(new_item)

            # Add the new item to jewelry
            elif commertiant == merchants[6]:
                jewelry_items.append(new_item)


# Apply items buffs
def apply_items_buffs(players: list):
    for player in players:
        for item in items[player.character_class]:
            if item.is_weapon:
                continue

            player.buff_status(item.additional_health, item.additional_mana, item.additional_stamina)

            player.buff_damage(item.additional_attack_damage, item.additional_ability_power, item.additional_true_damage)

            player.attack_damage_negation += item.additional_ad_negation
            player.ability_power_negation += item.additional_ap_negation


# Remove items buffs
def remove_items_buffs(players: list):
    for player in players:
        for item in items[player.character_class]:
            if item.is_weapon:
                continue

            player.debuff_status(item.additional_health, item.additional_mana, item.additional_stamina)

            player.debuff_damage(item.additional_attack_damage, item.additional_ability_power, item.additional_true_damage)

            player.attack_damage_negation -= item.additional_ad_negation
            player.ability_power_negation -= item.additional_ap_negation


# Save all items
def save_items():
    save_player_items()
    save_commertiant_items()


# Load all items
def load_items(players: list):
    load_player_items()
    #load_commertiant_items()
    apply_items_buffs(players)