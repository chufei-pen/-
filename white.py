import pygame
import enemyTank2

class WhiteTank(enemyTank2.EnemyTank):
    def __init__(self,x):       
        enemyTank2.EnemyTank.__init__(self)
        self.x=x
        self.tank = pygame.image.load(r"image\enemy_1_0.png").convert_alpha()
        self.tank_R0 = self.tank.subsurface(( 0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.rect = self.tank_R0.get_rect()
        self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 3 + 0 * 24