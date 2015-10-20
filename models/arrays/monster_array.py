class MonsterArray(object):
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
        self.skills = monster_array['skills']
        self.options = monster_array['options']

    def getChallengeRating(self):
        return self.cr

    def getMasterAbilityMod(self):
        return self.master_ability_mod

    def getGreatAbilityMod(self):
        return self.good_ability_mod

    def getGoodAbilityMod(self):
        return self.good_ability_mod

    def getArmorClass(self):
        return self.armor_class

    def getTouchArmorClass(self):
        return self.touch_armor_class
    
    def getName(self):
        return self.name 
    
    def getXP(self):
        return self.xp 
    
    def getMonsterType(self):
        return self.monster_type 
    
    def getInit(self):
        return self.init 
    
    def getSenses(self):
        return self.senses 
    
    def getPerception(self):
        return self.perception 
    
    def getSize(self):
        return self.size 
    
    def getSpeed(self):
        return self.speed 
    
    def getFlatFootedArmorClass(self):
        return self.flat_footed_armor_class 
    
    def getFortitude(self):
        return self.fortitude 
    
    def getReflex(self):
        return self.reflex 
    
    def getWillpower(self):
        return self.willpower 
    
    def getCMD(self):
        return self.cmd 
    
    def getHitPoints(self):
        return self.hit_points 
    
    def getMelee(self):
        return self.melee 
    
    def getRanged(self):
        return self.ranged 
    
    def getAttackOptions(self):
        return self.attack_options 
    
    def getCMB(self):
        return self.cmb 
    
    def getStrngth(self):
        return self.strength 
    
    def getDexterity(self):
        return self.dexterity 
    
    def getConstitution(self):
        return self.constitution 
    
    def getIntelligence(self):
        return self.intelligence 
    
    def getWidsome(self):
        return self.wisdom 
    
    def getCharisma(self):
        return self.charisma 

