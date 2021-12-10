import pygame
import weapon

class Treasure(weapon.Weapon):
    def __init__(self,colorTank):
        weapon.Weapon.__init__(self,colorTank)
        self.isred=True