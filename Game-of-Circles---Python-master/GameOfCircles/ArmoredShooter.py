import SpriteManager
from Bullet import Bullet
from Sprite import Sprite
from ArmoredEnemy import ArmoredEnemy

class ArmoredShooter(ArmoredEnemy, Sprite):
    
    speed = 4
    diameter = 50

    c = color(255, 255 ,255)
    
    mark = 0
    wait = 700

    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1

        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
    
    def aim(self, target):
        
        distance = dist(target.x, target.y, self.x, self.y)
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        
        if distance == 0:
            distance = 0.01
            
        magnitude = 7
        return PVector(xComponent/distance * magnitude, yComponent / distance * magnitude)
    
    def fire(self, vector):
        
        if millis() - self.mark > self.wait:
             SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))

             self.mark = millis()
