from pathfinder.models.arrays.monster_array import MonsterArray
from pathfinder.models.arrays.combatant_data import combatant_data

class Combatant(MonsterArray):
   def __init__(self, cr):
       if not isinstance(cr, (int, long)):
           cr = 0

       array = combatant_data[cr]

       self.armor_class = array['armor_class']
       self.touch_armor_class = array['touch_armor_class']
       self.flat_footed_armor_class = array['flat_footed_armor_class']
       self.fortitude = array['fortitude']
       self.reflex = array['reflex']
       self.willpower = array['willpower']
       self.cmd = array['cmd']
       self.hit_points = array['hit_points']
       self.ability_dc = array['ability_dc']
       self.spell_dc = array['spell_dc']
       self.master_ability_mod = array['master_ability_mod']
       self.great_ability_mod = array['great_ability_mod']
       self.good_ability_mod = array['good ability_mod']
       self.master_skill = array['master_skill']
       self.master_skill_count = array['master_skill_count']
       self.good_skill = array['good_skill']
       self.good_skill_count = array['good_skill_count']
       self.options = array['options']

