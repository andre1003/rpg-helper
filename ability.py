from utils import bcolors

class Ability:
    # Name
    name = ''

    # Cost
    health_cost = 0
    mana_cost = 0
    stamina_cost = 0

    # Damage
    additional_attack_damage = 0
    additional_ability_power = 0
    additional_true_damage = 0

    # Status
    additional_health = 0
    additional_mana = 0
    additional_stamina = 0

    # Cooldown
    is_unic_use = False
    cooldown = 1

    # Uses
    affect_other_player = False
    number_of_enemies_affected = 0
    no_dice = False
    is_attack = False

    # Chance
    min_dice_value = 1

    # Constructor
    def __init__(self, name, health_cost, mana_cost, stamina_cost, additional_attack_damage, additional_ability_power, additional_true_damage, additional_health, additional_mana, additional_stamina, is_unic_use, cooldown, affect_other_player, number_of_enemies_affected, no_dice, is_attack, min_dice_value):
        self.name = name

        self.health_cost = health_cost
        self.mana_cost = mana_cost
        self.stamina_cost = stamina_cost

        self.additional_attack_damage = additional_attack_damage
        self.additional_ability_power = additional_ability_power
        self.additional_true_damage = additional_true_damage

        self.additional_health = additional_health
        self.additional_mana = additional_mana
        self.additional_stamina = additional_stamina

        self.is_unic_use = is_unic_use

        self.cooldown = cooldown

        self.affect_other_player = affect_other_player
        self.number_of_enemies_affected = number_of_enemies_affected

        self.no_dice = no_dice

        self.is_attack = is_attack

        self.min_dice_value = min_dice_value

    # Check ability cast success
    def check_success(self, dice_value: int):
        return self.min_dice_value <= dice_value or self.no_dice

    def show_ability_details(self):
        print(f'Habilidade: {bcolors.CYAN}{self.name}{bcolors.ENDC}')
        print()
        print(f'{bcolors.RED}Custo em Vida: {self.health_cost}{bcolors.ENDC}')
        print(f'{bcolors.CYAN}Custo em Mana: {self.mana_cost}{bcolors.ENDC}')
        print(f'{bcolors.GREEN}Custo em Stamina: {self.stamina_cost}{bcolors.ENDC}')
        print()
        print(f'{bcolors.RED}Dano de Ataque Adicional: {self.additional_attack_damage}{bcolors.ENDC}')
        print(f'{bcolors.CYAN}Dano Mágico Adicional: {self.additional_ability_power}{bcolors.ENDC}')
        print(f'Dano Verdadeiro Adicional: {self.additional_true_damage}')
        print()
        print(f'{bcolors.RED}Vida Adicional: {self.additional_health}{bcolors.ENDC}')
        print(f'{bcolors.CYAN}Mana Adicional: {self.additional_mana}{bcolors.ENDC}')
        print(f'{bcolors.GREEN}Stamina Adicional: {self.additional_stamina}{bcolors.ENDC}')
        print()
        is_unic_use = 'Não'
        if self.is_unic_use:
            is_unic_use = 'Sim'
        print(f'É Uso Único: {is_unic_use}')
        print()
        print(f'Cooldown (em turnos): {self.cooldown}')
        print()
        affect_other_player = 'Não'
        if self.affect_other_player:
            affect_other_player = 'Sim'
        print(f'Afeta Outros Jogadores: {affect_other_player}')
        print(f'Número de Inimigos Afetados (não funciona atualmente): {self.number_of_enemies_affected}')
        print()
        no_dice = 'Sim'
        if self.no_dice:
            no_dice = 'Não'
        print(f'{bcolors.WARNING}Precisa de Dado: {no_dice}{bcolors.ENDC}')
        print()
        is_attack = 'Não'
        if self.is_attack:
            is_attack = 'Sim'
        print(f'{bcolors.RED}É Um Ataque: {is_attack}{bcolors.ENDC}')
        print()
        print(f'Valor Mínimo do Dado para Acerto: {self.min_dice_value}')

    # Get all ability data
    def get_data(self):
        data = ''

        data += str(self.name) + '\n'

        data += str(self.health_cost) + '\n'
        data += str(self.mana_cost) + '\n'
        data += str(self.stamina_cost) + '\n'

        data += str(self.additional_attack_damage) + '\n'
        data += str(self.additional_ability_power) + '\n'
        data += str(self.additional_true_damage) + '\n'

        data += str(self.additional_health) + '\n'
        data += str(self.additional_mana) + '\n'
        data += str(self.additional_stamina) + '\n'

        data += str(self.is_unic_use) + '\n'

        data += str(self.cooldown) + '\n'

        data += str(self.affect_other_player) + '\n'
        data += str(self.number_of_enemies_affected) + '\n'

        data += str(self.no_dice) + '\n'

        data += str(self.is_attack) + '\n'

        data += str(self.min_dice_value) + '\n'

        return data