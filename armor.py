import pygame
import weapon

class Armor(weapon.Weapon):
    def __init__(self,colorTank):
        weapon.Weapon.__init__(self,colorTank)
        self.life=self.colorTank.life+2