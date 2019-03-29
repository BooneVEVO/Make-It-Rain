import SpriteManager
from Sprite import Sprite
from Bullet import Bullet

class FlickerBot(Sprite):
    
    speed = 2
    diameter = 100

    c = color(0, 0 ,255)
    
    mark = 0
    wait = 10
    
    mark2 = 0
    wait2 = 3000

    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1

        vector = self.aim(SpriteManager.getPlayer())
        
        self.fire(vector)
        self.teleport()
        
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
             SpriteManager.spawn(Bullet(self.x + random(-200, 200), self.y + random(-200, 200), vector, self.team))

             self.mark = millis()
             
    def teleport(self):
        
        if millis() - self.mark2 > self.wait2:
             self.x = random(width)
             self.y = random(height)

             self.mark2 = millis()
