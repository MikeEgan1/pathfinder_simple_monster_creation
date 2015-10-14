from pathfinder.models.arrays.array_factory import ArrayFactory


def main():
    cr = raw_input("Enter CR of monster:")
    print cr

    array_type = raw_input("Enter the array type of monster [combatant, expert, spellcaster]")
    array = ArrayFactory(cr, array_type)


if __name__ == "__main__":
    main()