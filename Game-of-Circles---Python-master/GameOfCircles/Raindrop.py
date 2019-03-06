from Sprite import Sprite

class Raindrop(Sprite):
    
    team = 2
    speed = 20
    diameter = 10
    c = color(255,0,255)
    
    def move(self):
        self.y += self.speed
        if self.y > height:
            self.y = 0
