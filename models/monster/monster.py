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
        self.setFortitude(monster_array.getFortitude())


    def setArmorClass(self, armor_class):
        self.armor_class = armor_class

    def setTouchArmorClass(self, touch_armor_class):
        self.touch_armor_class = touch_armor_class

    def setChallengeRating(self, cr):
        self.cr = cr

    def getChallengeRating(self):
        return self.cr

    def setName(self, name):
        self.name = name

    def setXP(self, xp):
        self.xp = xp

    def setMonsterType(self, monster_type):
        self.monster_type = monster_type

    def setInit(self, init):
        self.init = init

    def setSenses(self, senses):
        self.senses = senses

    def setPerception(self, perception):
        self.perception = perception

    def setSize(self, size):
        self.size = size

    def setSpeed(self, speed):
        self.speed = speed

    def setFlatFootedArmorClass(self, ffac):
        self.flat_footed_armor_class = ffac

    def setFortitude(self, fortitude):
        self.fortitude = fortitude

    def setReflex(self, reflex):
        self.reflex = reflex

    def setWillpower(self, willpower):
        self.willpower = willpower

    def setCMD(self, cmd):
        self.cmd = cmd

    def setHitPoints(self, hit_points):
        self.hit_points = hit_points

    def setMelee(self, melee):
        self.melee = melee

    def setRanged(self, ranged):
        self.ranged = ranged

    def setAttackOptions(self, attack_options):
        self.attack_options = attack_options

    def setCMB(self, cmb):
        self.cmb = cmb

    def setStrngth(self, strength):
        self.strength = strength

    def setDexterity(self, dexterity):
        self.dexterity = dexterity

    def setConstitution(self, constitution):
        self.constitution = constitution

    def setIntelligence(self, intelligence):
        self.intelligence = intelligence

    def setWidsome(self, widsom):
        self.wisdom = widsom

    def setCharisma(self, charisma):
        self.charisma = charisma