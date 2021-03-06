from SpriteManager import sprites
from Bullet import Bullet
from PeaShooter import PeaShooter

class Player:
    
    # instance variables
    left = False
    right = False
    up = False
    down = False
    speed = 10
    diameter = 35
    c = color(255,0,0)
#    primaryWeapon = peaShooter
    
    # constructor
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    # instance methods
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def move(self):
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        self.x = constrain(self.x, self.diameter / 2, width - self.diameter / 2)
        self.y = constrain(self.y, self.diameter / 2, height - self.diameter / 2)
    
    def animate(self):
        self.display()
        self.move()
        
    def fire(self, vector = None):
        if vector is None:
            primaryWeapon = fire
        else:
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
        
        
    def handleCollision(self):
        pass
        
    def keyDown(self):
        
        charge = 0
        
        if key == 'f' or key == 'F':
            sprites.append(Bullet(self.x, self.y, PVector(0, -10), self.team))
            sprites.append(Bullet(self.x + 15, self.y + 5, PVector(0, -10), self.team))
            sprites.append(Bullet(self.x - 15, self.y + 5, PVector(0, -10), self.team))
            
            charge = charge + 1
        
        if charge > 10:
            SpriteManager.spawn(bigBullet(self.x, self.y, vector, self.team))
            charge = 0
    
        if keyCode == LEFT:
            self.left = True
        if keyCode == RIGHT:
            self.right = True
        if keyCode == UP:
            self.up = True
        if keyCode == DOWN:
            self.down = True
            
    def keyUp(self):
        if keyCode == LEFT:
            self.left = False
        if keyCode == RIGHT:
            self.right = False
        if keyCode == UP:
            self.up = False
        if keyCode == DOWN:
            self.down = False
