class Sprite(object):
    def __init__(self, x, y, imgFile, speed, lifeCounter):
        self.x = x
        self.y = y
        self.imgFile = imgFile
        self.speed = speed
        self.lifeCounter = lifeCounter

class Enemy(Sprite):
    def __init__(self, x, y, imgFile, speed):
        __init__(self, x, y, imgFile, speed, 5)
        self.message = "I'm here to protect my master"

class Player(Enemy):
    def __init__(self, x, y, imgFile, speed):
        Sprite.(self, y, imgFile, speed, 6)
        self.speed = 56

class DifficultEnemy(Enemy):
    def __init__(self, x, y, imgFile):
        Enemy.__init__(self, imgFile, 80)

class EasyEnemy(Player):
    Enemy.__init__(self, x, y, imgFile, 40)
    def __init__(self, x, y, imgFile):
        self.lifeCounter = 1
