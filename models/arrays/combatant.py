from pathfinder.models.arrays.monster_array import MonsterArray
import json

class Combatant(MonsterArray):
   def __init__(self, cr):
        if not isinstance(cr, (int, long)):
           cr = 0

        with open("json/combatant.json", "r") as file:
            combatant = json.load(file)
            super(Combatant, self).__init__(cr, combatant[str(cr)])

