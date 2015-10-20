from pathfinder.exceptions.array_exceptions import InvalidArrayTypeException
from pathfinder.models.arrays.combatant import Combatant
import json

class ArrayFactory:
    def __init__(self):
        pass

    def getArray(self, cr, array_type):
        with open("json/menus/array_types.json") as file:
            array_types = json.load(file)

            if array_type not in array_types:
                raise InvalidArrayTypeException()

            if array_type == 'combatant':
                return Combatant(cr)