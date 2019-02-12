import platform
from Bullet import Bullet
from Enemy import Enemy
from Raindrop import Raindrop
from Player import Player
from SpriteManager import sprites
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    sprites.append(player)
    sprites.append(Enemy(50, 50, enemyTeam))
    sprites.append(Enemy(150, 150, enemyTeam))
    sprites.append(Raindrop(50, 50, enemyTeam))
    sprites.append(Raindrop(150, 150, enemyTeam))
    sprites.append(Raindrop(50, 250, enemyTeam))
    sprites.append(Raindrop(350, 350, enemyTeam))
    sprites.append(Raindrop(150, 250, enemyTeam))
    sprites.append(Raindrop(250, 350, enemyTeam))
    sprites.append(Raindrop(250, 150, enemyTeam))
    sprites.append(Raindrop(350, 150, enemyTeam))
    sprites.append(Raindrop(350, 50, enemyTeam))
    sprites.append(Raindrop(250, 50, enemyTeam))
    sprites.append(ScreenSaverBot(0,0, enemyTeam))
    sprites.append(JiggleBot(40, 40, enemyTeam))
                           
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
