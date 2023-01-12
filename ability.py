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