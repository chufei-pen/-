import pygame
import green
import red
import yellow
import white
import fire
import armor
import track
import treasure


class TankFactory():
                
    def createTank(self,kind=None,x=None):
        self.kind=kind

        self.x = x
        if not self.x:
            self.x = random.choice([1, 2, 3])
        self.x -= 1

        if kind==1:
            self.tank=green.GreenTank(self.x)
            self.tank=armor.Armor(self.tank)
            return self.tank
        elif kind==2:
            self.tank=white.WhiteTank(self.x)
            self.tank=track.Track(self.tank)
            return self.tank 
        elif kind==3:
            self.tank=yellow.YellowTank(self.x)
            self.tank=fire.Fire(self.tank)
            return self.tank   
        elif kind==4:
            self.tank=red.RedTank(self.x)
            self.tank=treasure.Treasure(self.tank)
            return self.tank              
