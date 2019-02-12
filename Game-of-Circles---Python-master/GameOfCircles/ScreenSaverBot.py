class ScreenSaverBot:
    yspeed = 4
    xspeed = 8
    diameter = 50
    c = color(0, 255 ,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.y > height or self.y < 0:
            self.y *= -1
        if self.x < 0 or self.x > width:
            self.x *= -1
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
