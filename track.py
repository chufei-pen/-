import pygame
import weapon

class Track(weapon.Weapon):
    def __init__(self,colorTank):
        weapon.Weapon.__init__(self,colorTank)
        self.speed=self.colorTank.speed+2