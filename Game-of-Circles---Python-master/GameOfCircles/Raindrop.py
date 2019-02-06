class Raindrop:
    
    speed = 2
    diameter = 10
    c = color(255,0,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        #self.x += self.speed
        #if self.x < 0 or self.x > width:
            #self.speed *= -1
        self.y += self.speed
        if self.y > height:
            self.y = 0
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
