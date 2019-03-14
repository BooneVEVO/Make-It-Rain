from Sprite import Sprite

from ArmoredEnemy import ArmoredEnemy
class JiggleBot(ArmoredEnemy, Sprite):
    
    hp = 4
    speed = 4
    diameter = 50
    c = color(255,100,255)
    weight = 1
    
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0 , width)
        self.y = constrain(self.y, 0, height)
        
