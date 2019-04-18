import SpriteManager
from Sprite import Sprite
from Bullet import Bullet

class FlickerBot(Sprite):
    
    speed = 8
    diameter = 80

    c = color(0, 0 ,255)
    
    mark = 0
    wait = 50
    
    mark2 = 0
    wait2 = 2000

    mark3 = 0
    wait3 = 3000
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1

        vector = self.aim(SpriteManager.getPlayer())
        
        self.fire(vector)
        self.teleport()
       # self.shotgun(0, vector)
        
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
             SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector, self.team))

             self.mark = millis()
             
    def teleport(self):
        
        if millis() - self.mark2 > self.wait2:
             self.x = random(width)
             self.y = random(height)

             self.mark2 = millis()
             

    def shotgun(self, expCount, vector):
        
        if millis() - self.mark3 > self.wait3:
            
'            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector-75, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector-60, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector-45, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector-30, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector-15, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector+75, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector+60, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector+45, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector+30, self.team))
            SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector+15, self.team)) 
'           SpriteManager.spawn(Bullet(self.x + random(-100, 100), self.y + random(-100, 100), vector, self.team))
        
            self.mark3 = millis()
