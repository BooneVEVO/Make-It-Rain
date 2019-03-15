import SpriteManager
from Pea import Pea 
class PeaShooter:
    wait = 1000
    mark = 0
    cooldown = True
    
    def __init__(self, handler):
        self.handler = handler
        
    def shoot(self, vector):
        if self.cooldown:
            pea = Pea(self.handler.x, self.handler.y, vector, self.handler.team)
            SpriteManager.spawn(pea)
            self.cooldown = False
        if(millis() - self.mark > self.wait):
            self.mark = millis()
            self.cooldown = True
            
'    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1

        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
    
