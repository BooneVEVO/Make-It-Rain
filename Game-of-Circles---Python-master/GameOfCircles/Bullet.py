from Sprite import Sprite
import SpriteManager

class Bullet(Sprite):
    

    diameter = 10
    c = color(0)
       
    def __init__(self, x, y, vector, team):
        Sprite.__init__(self, x, y, team)
        self.vector = vector   
       
    #NEEDS FIXING   
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
