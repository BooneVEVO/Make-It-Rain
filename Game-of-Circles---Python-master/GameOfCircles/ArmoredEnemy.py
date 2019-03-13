import SpriteManager

class ArmoredEnemy(object):
    hp = 5
    team = 2
#    diameter = 100
#    c = color(255, 255, 150)
    weight = 10
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        pass
        
    def display(self):
        fill(self.c)
#        ellipse(self.x, self.y, self.diameter + 100, self.diameter+100)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
        
    def isColliding(self, other):
        r1=self.diameter/2.0
        r2=other.diameter/2.0
        return r1+r2>dist(self.x,self.y, other.x, other.y)
    
    def handleCollision(self):
        self.weight = self.weight - 5
        if weight < 0:
            SpriteManager.destroy(self)
        
        
