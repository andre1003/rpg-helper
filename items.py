from utils import bcolors


items = {
    'Bárbaro': [
        'Espada curva',
        'Espada longa',
        'Lança de pedra',
        'Arco e flecha',

        'Tanga simples',
        'Ombreira de pele de urso',
        'Perneiras de couro',
        'Capuz de tecido simples',
    ],


    'Bardo': [
        'Bandolim',
        'Flauta',
        'Violino',
        'Macumba',

        'Manto de bardo cortês',
        'Manto de bardo de elite',
        'Manto de bardo rasgado',
        'Manto de fugitivo',
    ],
    
    
    'Bruxo': [

    ],
    
    
    'Druida': [
        'Faca',
        'Adaga curta',
        'Lança',
        'Bastão de madeira',

        'Manto de lã simples',
        'Manto de couro',
        'Roupas de camponês',
        'Roupas nobres',
    ],
    
    
    'Mago': [
        'Cajado de madeira Ancestral',
        'Cajado de osso',
        'Cajado de ferro',
        'Orbe simples',

        'Manto ragasdo',
        'Manto de mago da floresta',
        'Manto de mago de elite',
        'Manto de mago da água',
    ],
    
    
    'Paladino': [
        'Escudo grande',
        'Espada longa',
        'Alabarda',
        'Machado grande',

        'Armadura dourada',
        'Armadura de bronze de elite',
        'Armadura de couro leve',
        'Armadura real de Smargdus',
    ],
}


def get_item_at_index(character_class:str , index: int):
    return items[character_class][index]




merchant_items = [
    ('Erva de cura simples', 'Erva usada para fabricar poções de cura simples', 5),
    ('Faca de dissecar cega', 'Faca para dissecar animais de caça', 15),
    ('Pedra de afiar espadas', 'Pedra usada para afiars espadas, deixando-as mais fortes temporariamente', 35),
    ('Erva de cura de envenamento', 'Erva usada para realizar elixires de cura de envenenamento', 5),
    ('Álcool', 'Álcool pode ter diversas utilidades, como limpeza de armas e armaduras, fabricação de poções e elixires, etc.', 12),
]

market_items = [
    ('Maçã', 'Recupera 2 HP', 2),
    ('Banana', 'Recupera 2 HP', 2),
    ('Carne de cervo', 'Recupera 20 HP e 5 de mana', 40),
    ('Carne de boi', 'Recupera 25 HP e 25 de mana', 55),
    ('Vinho', 'Recupera 5 HP e 10 de mana', 10),
]

big_market_items = [
    ('Pedra de encantamento mágico de arma simples', 'Pedra usada para inflingir dano mágico em uma determinada arma', 210),
    ('Cimitarra', 'Inflinge 15 de Dano de Ataque e 3 de Dano Verdadeiro adicionais', 150),
    ('Cajado de Orvalho superior', 'Aumenta a Mana em 12 pontos e infinge 15 de Dano Mágico adicional', 1200),
    ('Anel de Cura Superior', 'Aplica um cura de 15 HP no usuário em 5 de HP em cada turno. Ao final de cada combate, recupera 40 HP para todos os jogadores', 500),
    ('Barraca de acampamento simples', 'Útil para longas viagens. Abriga 1 pessoa', 120),
]

blacksmith_items = [
    ('Restaurar espada', 'Restaura uma espada quebrada', 25),
    ('Restaurar machado', 'Restaura um machado quebrado', 25),
    ('Restaurar cajado', 'Restaura um cajado quebrado', 25),
    ('Restaurar armadura', 'Restaura uma peça de armadura quebrada', 30),
    ('Aprimorar escudo de Paladino', 'Aprimora o escudo de um Paladino até o nível Superior', 500),
]

stable_items = [
    ('Pangaré', 'Consegue andar uma distância considerável (50m) sem se cansar', 3000),
    ('Cavalo treinado', 'Consegue andar uma longa distância (100m) sem se cansar', 6000),
    ('Burro de carga', 'Consegue levar uma carga considerável de itens (20 itens)', 3500),
    ('Cavalo de elite', 'Consegue andar livremente sem se cansar (sem limite)', 50000),
    ('Carroça com 4 cavalos', 'Consegue levar cargas muito pesadas (100 itens) sem se cansar', 250000),
]

alchemist_items = [
    ('Erva de cura simples', 'Erva usada para fabricar poções de cura simples', 2),
    ('Erva de cura de envenenamento', 'Erva usada para realizar elixires de cura de envenenamento', 5),
    ('Receita de poção de cura', 'Receita para fabricar poção de cura', 50),
    ('Receita de poção de força', 'Receita para fabricar poção de força', 65),
    ('Kit de poções básicas', 'Kit contendo 5 poções de cura simples e 5 poções de mana simples', 250),
]

jewelry_items = [
    ('Minério de prata refinado', 'Usado para forjar espadas e escudos e armaduras', 100),
    ('Minério de ouro refinado', 'Usado para fabricar itens diversos', 1500),
    ('Colar de diamante', 'Sem nenhuma utilidade específica, mas é muito bonito!', 350000),
    ('Minério de diamante bruto', 'Precisa ser refinado para ser utilizado', 5000),
    ('Rubi', 'Jóia extremamente rara de se encontrar. Pode ser utilizada em alguns itens mágicos', 120000),
]




ores = [
    'Minério de cobre',
    'Minério de ferro',
    'Minério de prata',
    'Minério de ouro',
    'Minério de diamante',
    'Minério de rubi',
    'Minério de esmeralda',
    'Minério de safira',
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

item_levels= (
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


def create_item():
    name = input('Insira o nome do item: ')
    description = input('Insira a descrição do item: ')
    price = int(input('Insira o valor do item: '))
    item = (name, description, price)

    print()

    for i in range(len(merchants)):
        print(f'{i} - {merchants[i]}')
    option = int(input('\nQual mercador irá vender o item: '))

    if option == 0:
        merchant_items.append(item)
    
    elif option == 1:
        market_items.append(item)

    elif option == 2:
        big_market_items.append(item)

    elif option == 3:
        blacksmith_items.append(item)

    elif option == 4:
        stable_items.append(item)

    elif option == 5:
        alchemist_items.append(item)

    elif option == 6:
        jewelry_items.append(item)

    print(f'\nO item {bcolors.CYAN}{name}{bcolors.ENDC} foi adicionado ao inventário do {bcolors.GREEN}{merchants[option]}{bcolors.ENDC}')