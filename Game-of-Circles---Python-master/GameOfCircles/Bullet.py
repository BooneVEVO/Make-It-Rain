from Sprite import Sprite
import SpriteManager

class Bullet(Sprite):
    

    diameter = 10
    c = color(0)
    weight = 1
    mark = 0
    wait = 10
    
    def __init__(self, x, y, vector, team):
        Sprite.__init__(self, x, y, team)
        self.vector = vector   
       
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        
        if millis() - self.mark > self.wait:
             self.destroy()
             self.mark = millis()
