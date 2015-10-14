class Monster():
    def __init__(self):
        self.cr = 0

    def applyArray(self, array):
        self.setChallengeRating(array.getChallengeRating)

    def setChallengeRating(self, cr):
        self.cr = cr

    def getChallengeRating(self):
        return self.cr