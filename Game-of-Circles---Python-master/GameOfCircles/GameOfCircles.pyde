import platform
from Bullet import Bullet
from Enemy import Enemy
from Raindrop import Raindrop
from Player import Player
from SpriteManager import sprites
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Shooter import Shooter
from ArmoredShooter import ArmoredShooter
from ArmoredEnemy import ArmoredEnemy
from PeaShooter import PeaShooter
from FlickerBot import FlickerBot

import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    SpriteManager.setPlayer(player)
#    SpriteManager.spawn(JiggleBot(200, 50, 2))
    SpriteManager.spawn(Enemy(100, 100, 2))
    SpriteManager.spawn(Enemy(150, 50, 2))
    SpriteManager.spawn(Shooter(150, 50, 2))
    SpriteManager.spawn(FlickerBot(random(1, 500), random(1, 500), 2))
    SpriteManager.spawn(FlickerBot(random(1, 500), random(1, 500), 2))
#    SpriteManager.spawn(PeaShooter(2))

def draw():
    background(random(0, 255), random(0, 255), random(0, 255))    
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
