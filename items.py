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
    ('Erva de cura simples', 5),
    ('Faca de dissecar cega', 15),
    ('Pedra de afiar espadas', 35),
    ('Erva de cura de envenamento', 5),
    ('Álcool', 12),
]

market_items = [
    ('Maçã', 2),
    ('Banana', 2),
    ('Carne de cervo', 40),
    ('Carne de boi', 55),
    ('Vinho', 10),
]

big_market_items = [
    ('Pedra de encantamento mágico de arma simples', 210),
    ('Cimitarra', 150),
    ('Cajado de Orvalho superior', 1200),
    ('Anel de Cura Superior', 500),
    ('Barraca de acampamento simples', 120),
]

blacksmith_items = [
    ('Restaurar espada', 25),
    ('Restaurar machado', 25),
    ('Restaurar cajado', 25),
    ('Restaurar armadura', 30),
    ('Aprimorar escudo de Paladino', 500),
]

stable_items = [
    ('Pangaré', 3000),
    ('Cavalo treinado', 6000),
    ('Burro de carga', 3500),
    ('Cavalo de elite', 50000),
    ('Carroça com 4 cavalos', 250000),
]

alchemist_items = [
    ('Erva de cura simples', 2),
    ('Erva de cura de envenenamento', 5),
    ('Receita de poção de cura', 50),
    ('Receita de poção de força', 65),
    ('kit de poções básicas', 250),
]

jewelry_items = [
    ('Minério de prata refinado', 100),
    ('Minério de ouro refinado', 1500),
    ('Colar de diamante', 350000),
    ('Minério de diamante bruto', 5000),
    ('Rubi', 120000),
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