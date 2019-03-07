import SpriteManager

from Bullet import Bullet
from Sprite import Sprite

class Shooter(Sprite):

    speed = 4
    diameter = 50
    c = color(255, 0 ,255)
    
    mark = 0
    wait = 700
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1

        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
    
    def aim(self, target):
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        d = sqrt((xComponent + xComponent) - (yComponent + yComponent))
        xVector = xComponent / d
        yVector = yComponent / d
        
        return PVector(xVector, yVector)
    
    def fire(self, vector):
        
        
        mark = 0
        wait = 1000
        go = True
        
        if(millis() - mark > wait):
            go = not go
            mark = millis()
        
#        if(go):
#            sprites.append(Bullet(self.x, self.y, PVector(0, -10), self.team))
#            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
