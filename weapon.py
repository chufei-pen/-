import pygame
import enemyTank2

class Weapon(enemyTank2.EnemyTank):
    def __init__(self,colorTank):
        enemyTank2.EnemyTank.__init__(self)
        self.colorTank=colorTank
        self.tank = colorTank.tank
        self.x=colorTank.x
        self.tank_R0 = colorTank.tank_R0
        self.tank_R1 = colorTank.tank_R1
        self.rect = colorTank.rect
        self.rect.left, self.rect.top = colorTank.rect.left ,colorTank.rect.top
