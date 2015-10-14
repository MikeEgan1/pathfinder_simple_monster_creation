from pathfinder.exceptions.array_expections import InvalidArrayTypeException
from pathfinder.arrays.combatant import Combatant

class array_factory:

    ARRAY_TYPES = ['combatant', 'expert', 'spellcaster']

    def __init__(self, cr, array_type):
        if array_type not in ARRAY_TYPES:
            throw InvalidArrayTypeException

        if array_type == 'combatant':
            return Combatant(cr)