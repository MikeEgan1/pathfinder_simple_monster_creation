class MonsterArray:
    def __init__(self, cr, moster_array):
        self.cr = cr
        self.armor_class = moster_array['armor_class']
        self.touch_armor_class = moster_array['touch_armor_class']
        self.flat_footed_armor_class = moster_array['flat_footed_armor_class']
        self.fortitude = moster_array['fortitude']
        self.reflex = moster_array['reflex']
        self.willpower = moster_array['willpower']
        self.cmd = moster_array['cmd']
        self.hit_points = moster_array['hit_points']
        self.ability_dc = moster_array['ability_dc']
        self.spell_dc = moster_array['spell_dc']
        self.master_ability_mod = moster_array['master_ability_mod']
        self.great_ability_mod = moster_array['great_ability_mod']
        self.good_ability_mod = moster_array['good ability_mod']
        self.master_skill = moster_array['master_skill']
        self.master_skill_count = moster_array['master_skill_count']
        self.good_skill = moster_array['good_skill']
        self.good_skill_count = moster_array['good_skill_count']
        self.options = moster_array['options']

    def getChallengeRating(self):
        return self.cr

    def getArmorClass(self):
        return self.armor_class

    def getTouchArmorClass(self):
        return self.touch_armor_class


