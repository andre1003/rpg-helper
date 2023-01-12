from utils import bcolors
from ability import Ability


# Character class
class Character:
    # # Name
    # name = "Generic Name"

    # # Class
    # character_class = ""

    # # Status
    # health = 100
    # mana = 100
    # stamina = 100

    # # Base Status
    # base_health = 100
    # base_mana = 100
    # base_stamina = 100

    # # Damage
    # attack_damage = 0
    # ability_power = 0
    # true_damage = 0

    # # Base Damage
    # base_attack_damage = 0
    # base_ability_power = 0
    # base_true_damage = 0

    # # Damage negation
    # attack_damage_negation = 0
    # ability_power_negation = 0

    # # Attack dice
    # attack_dice_number = 1
    # attack_dice_value = 6

    # # Defence dice
    # defense_dice_number = 1
    # defense_dice_value = 6

    # # Additional dice for ability
    # additional_ability_dice = 1

    


    # Constructor
    def __init__(self, name, character_class, health, mana, stamina, attack_damage, ability_power, true_damage, attack_damage_negation, ability_power_negation, attack_dice_number, attack_dice_value, defense_dice_number, defense_dice_value, additional_ability_dice):
        self.name = name
        self.character_class = character_class
        
        self.health = health
        self.mana = mana
        self.stamina = stamina

        self.base_health = health
        self.base_mana = mana
        self.base_stamina = stamina

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


        # Abilities
        self.character_abilities = list()


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
        if self.character_abilities:
            print()
            print('Habilidades: ', end='')
            for ability in self.character_abilities:
                print(ability.name, end='')
                if self.character_abilities.index(ability) != len(self.character_abilities) - 1:
                    print(', ', end='')
        
        print()

    def decrease_health(self, health_to_decrease):
        self.health -= health_to_decrease

        if self.health < 0:
            self.health = 0


    def buff_status(self, health, mana, stamina):
        self.health += health
        self.mana += mana
        self.stamina += stamina

    def buff_damage(self, attack_damage, ability_power, true_damage):
        self.attack_damage += attack_damage
        self.ability_power += ability_power
        self.true_damage += true_damage


    def debuff_status(self, health, mana, stamina):
        self.health -= health
        self.mana -= mana
        self.stamina -= stamina

    def debuff_damage(self, attack_damage, ability_power, true_damage):
        self.attack_damage -= attack_damage
        self.ability_power -= ability_power
        self.true_damage -= true_damage

    def add_ability(self, ability: Ability):
        self.character_abilities.append(ability)