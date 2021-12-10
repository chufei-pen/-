import pygame
import weapon

class Fire(weapon.Weapon):
    def __init__(self,colorTank):
        weapon.Weapon.__init__(self,colorTank)
        self.fire=self.colorTank.fire+1
