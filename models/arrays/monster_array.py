class MonsterArray(Object):
    def __init__(self, cr, monster_array):
        self.cr = cr
        self.armor_class = monster_array['armor_class']
        self.touch_armor_class = monster_array['touch_armor_class']
        self.flat_footed_armor_class = monster_array['flat_footed_armor_class']
        self.fortitude = monster_array['fortitude']
        self.reflex = monster_array['reflex']
        self.willpower = monster_array['willpower']
        self.cmd = monster_array['cmd']
        self.hit_points = monster_array['hit_points']
        self.ability_dc = monster_array['ability_dc']
        self.spell_dc = monster_array['spell_dc']
        self.master_ability_mod = monster_array['master_ability_mod']
        self.great_ability_mod = monster_array['great_ability_mod']
        self.good_ability_mod = monster_array['good ability_mod']
        self.master_skill = monster_array['master_skill']
        self.master_skill_count = monster_array['master_skill_count']
        self.good_skill = monster_array['good_skill']
        self.good_skill_count = monster_array['good_skill_count']
        self.options = monster_array['options']

    def getChallengeRating(self):
        return self.cr

    def getArmorClass(self):
        return self.armor_class

    def getTouchArmorClass(self):
        return self.touch_armor_class


