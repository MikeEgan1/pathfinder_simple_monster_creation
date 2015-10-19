from pathfinder.models.arrays.array_factory import ArrayFactory
from pathfinder.models.monster.monster import Monster
import json

def get_ability_score_string():
    with open("json/ability_scores.json") as file:
        ability_scores = json.load(file)

        ability_score_string = ""
        count = 1

        for score in ability_scores:
            ability_score_string = ability_score_string + "\n" + str(count) + ". " + score

        return ability_score_string

def main():
    monster = Monster()

    cr = raw_input("Enter CR of monster:")
    print cr

    array_type = raw_input("Enter the array type of monster\n 1. combatant\n 2. expert\n 3. spellcaster\n")
    factory = ArrayFactory()
    array = factory.getArray(cr, array_type)

    monster.applyArray(array)

    ability_scores = get_ability_score_string()

    high_mod = raw_input("Which Ability Modifier gets +" + str(array.getMasterAbilityMod()) + ability_score_string)

    great_mod = raw_input("Which Ability Modifier gets +" + str(array.getGreatAbilityMod()) + "\n 1. Strength\n 2. Dexterity \n 3. Constitution\n 4. Intelligence\n 5. Wisdom\n 6. Charisma")

    good_mod = raw_input("Which Ability Modifier gets +" + str(array.getGoodAbilityMod()) + "\n 1. Strength\n 2. Dexterity \n 3. Constitution\n 4. Intelligence\n 5. Wisdom\n 6. Charisma")


    if(high_mod == 1):
        monster.setStrngth(array.getMasterAbilityMod())

if __name__ == "__main__":
    main()