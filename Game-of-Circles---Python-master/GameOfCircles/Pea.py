from Bullet import Bullet

class Pea(Bullet):
    
    diameter = 20
    c = color(0, 255, 0)
    weight = 1
    def __init__(self, x, y, vector, team):
        Sprite.__init__(self, x, y, team)
        self.vector = vector   
       
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
