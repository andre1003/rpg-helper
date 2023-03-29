import shutil
from character import *
from utils import d
import items
from rpg import edit
from creation import save




# Calculate damage
def calculate_damage(attacker: Character, defender: Character, is_heavy_attack: bool, stamina_cost: int):
    print(25 * '=-')

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

        print(
            f'{bcolors.CYAN}{attacker.name} rolou 1d{attacker.attack_dice_value} para AP e tirou: \t{dice_value}{bcolors.ENDC}')
    print(
        f'\t{bcolors.CYAN}>> Total dos dados de ataque AP de {attacker.name}: {attacker_ap_dice}{bcolors.ENDC}\n\n\n\n')

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

        print(
            f'{bcolors.CYAN}{defender.name} rolou 1d{defender.defense_dice_value} para AP e tirou: \t{dice_value}{bcolors.ENDC}')
    print(
        f'\t{bcolors.CYAN}>> Total dos dados de defesa AP de {defender.name}: {defender_ap_dice}{bcolors.ENDC}\n\n\n\n')

    # Check if player have stamina
    if attacker.stamina - (stamina_cost * attack_intensity_multiplier) < 0:
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
    print(
        f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} aplicou:\n\tDano do Ataque: {ad_damage}\n\tDano Mágico: {ap_damage}\n\tDano Verdadeiro: {td_damage}\n\t{aux}\n\t{bcolors.RED}Dano Total: {final_damage}{bcolors.ENDC}\n{bcolors.GREEN}\tGasto de Stamina: {(stamina_cost * attack_intensity_multiplier)}{bcolors.ENDC}')

    print(25 * '=-')

    # Return final damage
    return final_damage




# Calculate damage from ability
def calculate_damage_ability(attacker: Character, defender: Character, ability: Ability, players: list,
                             current_turn: int, current_combat_abilities: list):
    print()
    print(25 * '-=')

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
        print(25 * '-=')
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
        print(25 * '-=')
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
            print(25 * '-=')
            return 0

    # If player can cast the ability
    if attacker.health <= ability.health_cost or attacker.mana < ability.mana_cost or attacker.stamina < ability.stamina_cost:
        print(f'\n{attacker.name} não pode castar a habilidade. Não cumpre os requisitos de casting!\n')
        print()
        print(25 * '-=')
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
            player.buff_damage(ability.additional_attack_damage, ability.additional_ability_power,
                               ability.additional_true_damage)

    if not ability.is_attack:
        print(
            f'\nA habilidade {bcolors.CYAN}{ability.name}{bcolors.ENDC} não ataca, portanto nenhum dano será causado!')
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
    print(
        f'{bcolors.GREEN}{attacker.name}{bcolors.ENDC} aplicou:\n\tDano do Ataque: {ad_damage}\n\tDano Mágico: {ap_damage}\n\tDano Verdadeiro: {td_damage}\n\t{bcolors.RED}Dano Total da Habilidade: {final_damage}{bcolors.ENDC}')
    print()
    print(25 * '-=')

    return final_damage




# Combat handler
def combat(current_turn: int, players: list, enemies: list, current_combat_abilities: list, order: list):
    # Get all characters
    all_characters = players.copy() + enemies.copy()

    # Edit a character, if needed
    opt = 2
    while opt == 2:
        opt = int(input(
            '1 - Iniciar a Luta\n2 - Alterar o Status de Personagem\n3 - Pular Turno\n-2 - Sair do Combate\n\nSua Escolha: '))
        if opt == 2:
            edit(all_characters, 1)

        elif opt == 3:
            return -1

        elif opt == -2:
            return -2

        else:
            print()
            print(25 * '-=')
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
            damage += calculate_damage_ability(attacker, defender, attacker.character_abilities[index], players,
                                               current_turn, current_combat_abilities)

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
                    count += 1

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
        print(25 * '-=')

    temp_path = 'temp/' + defender.name + '/'
    # Decrease defender health
    defender.decrease_health(damage)

    if defender in enemies:
        file = open(temp_path + 'enemy.txt', 'r')
        content = file.readlines()
        file.close()

        content[2] = str(defender.health) + '\n'

        file = open(temp_path + 'enemy.txt', 'w')
        file.writelines(content)
        file.close()

    remove_index = -1

    # If defender dies, remove it from the list
    if defender.health == 0:
        for i in range(len(order)):
            if defender.name == order[i][0]:
                remove_index = i
                break

        if defender in enemies:
            print(f'\n{bcolors.RED}{defender.name} morreu!{bcolors.ENDC}')
            shutil.rmtree('temp/' + defender.name)

            enemies.remove(defender)
            del (defender)

            xp = int(input('XP [Enter para 0]: ') or 0)
            coins = int(input('Moedas [Enter para 0]: ') or 0)

            print()
            print(25 * '-=')
            print(
                f'\nRecompensas\n\n{bcolors.CYAN}+{xp} XP{bcolors.ENDC}\n{bcolors.WARNING}+{coins} moedas{bcolors.ENDC}')

            for player in players:
                player.coins += coins
                player.xp += xp

        else:
            print(f'\n{bcolors.GREEN}{defender.name} {bcolors.RED}morreu!{bcolors.ENDC}')

    # Save player stats
    save(players)

    # Press any key to continue
    input('\nPressione qualquer tecla para continuar...')

    return remove_index