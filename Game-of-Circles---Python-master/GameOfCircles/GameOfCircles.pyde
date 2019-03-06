import platform
from Bullet import Bullet
from Enemy import Enemy
from Raindrop import Raindrop
from Player import Player
from SpriteManager import sprites
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot

import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(200, 50, 2))
    SpriteManager.spawn(Enemy(100, 100, 2))
    SpriteManager.spawn(Enemy(150, 50, 2))
    #SpriteManager.spawn(Raindrop(100,10, 20))
   # SpriteManager.spawn(Raindrop(200,10, 20))
  #  SpriteManager.spawn(Raindrop(300,10, 20))
 #   SpriteManager.spawn(Raindrop(400,10, 20))
#    SpriteManager.spawn(Raindrop(150,20, 20))
   # SpriteManager.spawn(Raindrop(250,20, 20))
  #  SpriteManager.spawn(Raindrop(350,20, 20))
 #   SpriteManager.spawn(Raindrop(50,10, 20))
#    SpriteManager.spawn(Raindrop(450,10, 20))
def draw():
    background(255)    
    SpriteManager.animate()
 
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
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
