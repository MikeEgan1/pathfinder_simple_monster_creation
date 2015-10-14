from pathfinder.models.arrays.array_factory import ArrayFactory
from pathfinder.models.monster.monster import Monster


def main():
    monster = Monster()

    import ipdb
    ipdb.set_trace()

    cr = raw_input("Enter CR of monster:")
    print cr

    array_type = raw_input("Enter the array type of monster\n 1. combatant\n 2. expert\n 3. spellcaster\n")
    factory = ArrayFactory()
    array = factory.getArray(cr, array_type)

    monster.applyArray(array)


if __name__ == "__main__":
    main()