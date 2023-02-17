xp = 200

xp_multiplier = 0.15
damage_multiplier = 0.155

total_cost = xp

ad = int(input('AD: '))
ap = int(input('AP: '))
td = int(input('TD: '))

print(f'XP inicial: {xp}')
print(f'Multiplicador XP: {xp_multiplier}\n')


for i in range(99):
    if i + 1 == 20:
        xp_multiplier -= 0.06
        damage_multiplier -= 0.06
    elif i + 1 == 50:
        xp_multiplier -= 0.05
        damage_multiplier -= 0.05
    elif i + 1 == 80:
        xp_multiplier -= 0.025
        damage_multiplier -= 0.025

    if (i + 1) % 10 == 0:
        print(f'XP do nível {i+1} para {i + 2}: {xp}')
        print(f'Custo total de XP até o level {i + 2}: {total_cost}')
        print(f'Dano de Ataque: {ad}')
        print(f'Dano de Habilidade: {ap}')
        print(f'Dano Verdadeiro: {td}\n')

    xp += round(xp_multiplier * xp)

    ad += round(damage_multiplier * ad)
    ap += round(damage_multiplier * ap)
    td += round(damage_multiplier * td)

    if i + 1 < 99:
        total_cost += xp

print(f'Custo total de XP: {total_cost}')
print(f'Dano de Ataque total: {ad}')
print(f'Dano de Habilidade total: {ap}')
print(f'Dano Verdadeiro total: {td}')
print(f'Dano Total Bruto: {ad + ap + td}')