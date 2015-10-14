from pathfinder.exceptions.array_exceptions import InvalidArrayTypeException
from pathfinder.models.arrays.combatant import Combatant

ARRAY_TYPES = [1, 2 ,3]

class ArrayFactory:
    def __init__(self):
        pass

    def getArray(self, cr, array_type):
        if array_type not in ARRAY_TYPES:
            raise InvalidArrayTypeException()

        if array_type == 1:
            return Combatant(cr)