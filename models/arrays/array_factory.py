from pathfinder.exceptions.array_exceptions import InvalidArrayTypeException
from pathfinder.models.arrays.combatant import Combatant

class array_factory:

    ARRAY_TYPES = ['combatant', 'expert', 'spellcaster']

    def __init__(self, cr, array_type):
        if array_type not in ARRAY_TYPES:
            raise InvalidArrayTypeException()

        if array_type == 'combatant':
            return Combatant(cr)