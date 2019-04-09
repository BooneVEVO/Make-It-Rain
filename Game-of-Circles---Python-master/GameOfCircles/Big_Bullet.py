from Sprite import Sprite
import SpriteManager

class bigBullet(Sprite):
    

    diameter = 50
    c = color(255, 0, 0)
    weight = 1
    mark = 0
    wait = 10
    
    def __init__(self, x, y, vector, team):
        Sprite.__init__(self, x, y, team)
        self.vector = vector   
       
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        
