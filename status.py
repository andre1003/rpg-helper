health = int(input('Vida: '))
mana = int(input('Mana: '))
stamina = int(input('Stamina: '))

multiplier = 0.05

for i in range(100):
    print(f'Level: {i+1}')
    print(f'Vida: {health}')
    print(f'Mana: {mana}')
    print(f'Stamina: {stamina}\n')

    health += round(multiplier * health)
    mana += round(multiplier * mana)
    stamina += round(multiplier * stamina)