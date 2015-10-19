from pathfinder.models.arrays.array_factory import ArrayFactory
from pathfinder.models.monster.monster import Monster


def main():
    monster = Monster()

    cr = raw_input("Enter CR of monster:")
    print cr

    array_type = raw_input("Enter the array type of monster\n 1. combatant\n 2. expert\n 3. spellcaster\n")
    factory = ArrayFactory()
    array = factory.getArray(cr, array_type)

    monster.applyArray(array)

    high_mod = raw_input("Which Ability Modifier gets +" + str(array.getMasterAbilityMod()) + "\n 1. Strength\n 2. Dexterity \n3. Constitution\n 4. Intelligence\n 5. Wisdom\n 6. Charisma")

    if(high_mod == 1):
        monster.setStrngth(array.getMasterAbilityMod())

    great_mod = raw_input("Which Ability Modifier gets +" + str(array.getGreatAbilityMod()) + "\n 1. Strength\n 2. Dexterity \n3. Constitution\n 4. Intelligence\n 5. Wisdom\n 6. Charisma"))

    good_mod = raw_input("Which Ability Modifier gets +" + str(array.getGoodAbilityMod()) + "\n 1. Strength\n 2. Dexterity \n3. Constitution\n 4. Intelligence\n 5. Wisdom\n 6. Charisma"))

if __name__ == "__main__":
    main()