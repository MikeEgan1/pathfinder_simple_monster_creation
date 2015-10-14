from pathfinder.models.arrays.monster_array import MonsterArray
from pathfinder.models.arrays.combatant_data import combatant_data

class Combatant(MonsterArray):
   def __init__(self, cr):
        if not isinstance(cr, (int, long)):
           cr = 0

        import ipdb
        ipdb.set_trace()

        super(Combatant, self).__init__(cr, combatant_data[cr])

