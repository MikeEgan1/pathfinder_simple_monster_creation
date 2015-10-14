class Monster():
    def __init__(self):
        self.cr = 0
        self.name = ''
        self.xp = 0
        self.monster_type = ''
        self.init = 0
        self.senses = ''
        self.perception = 0
        self.size = ''
        self.speed = 0
        self.armor_class = 0
        self.touch_armor_class = 0
        self.flat_footed_armor_class = 0
        self.fortitude = 0
        self.reflex = 0
        self.willpower = 0
        self.cmd = 0
        self.hit_points = 0
        self.melee = ''
        self.ranged = ''
        self.attack_options = ''
        self.cmb = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

    def applyArray(self, monster_array):
        self.setChallengeRating(monster_array.getChallengeRating())
        self.setArmorClass(monster_array.getArmorClass())
        self.setTouchArmorClass(monster_array.getTouchArmorClass())


    def setArmorClass(self, armor_class):
        self.armor_class = armor_class

    def setTouchArmorClass(self, touch_armor_class):
        self.touch_armor_class = touch_armor_class

    def setChallengeRating(self, cr):
        self.cr = cr

    def getChallengeRating(self):
        return self.cr