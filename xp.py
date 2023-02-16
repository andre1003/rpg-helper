xp = 200
xp_multiplier = 0.15
total_cost = xp

print(f'XP inicial: {xp}')
print(f'Multiplicador XP: {xp_multiplier}\n')


for i in range(99):
    if i + 1 == 20:
        xp_multiplier -= 0.06
    elif i + 1 == 50:
        xp_multiplier -= 0.05
    elif i + 1 == 80:
        xp_multiplier -= 0.025

    #if (i + 1) % 10 == 0:
    print(f'XP do nível {i+1} para {i + 2}: {xp}')
    print(f'Custo total de XP até o level {i + 2}: {total_cost}\n')

    xp += round(xp_multiplier * xp)
    if i + 1 < 99:
        total_cost += xp

print(f'Custo total de XP: {total_cost}')