
import SpriteManager

class ArmoredEnemy:
    armor = 10

    def display(self):
        stroke(100)
        strokeWeight(self.armor)
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
        constrain(x, 0, 500)
        constrain(y, 0, 500)
    def handleCollision(self):
        self.weight -= 1
        if weight < 1:
            SpriteManager.destroy(self)
        
        
