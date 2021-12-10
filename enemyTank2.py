import pygame
import bulletClass
import random



class EnemyTank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.flash = False
        self.times = 90
        self.dir_x, self.dir_y = 0, 1
        self.life = 1
        self.fire = 1        
        self.speed = 1
        self.bulletNotCooling = True
        self.bullet = bulletClass.Bullet()
        self.isred=False
        

        

        
    def shoot(self):

        self.bullet.life = True
        self.bullet.changeImage(self.dir_x, self.dir_y)
        
        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top + 1
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom - 1
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet.rect.left = self.rect.right + 1
            self.bullet.rect.top = self.rect.top + 20
    
    def move(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * self.dir_x, self.speed * self.dir_y)
        
        if self.dir_x == 0 and self.dir_y == -1:
            self.tank_R0 = self.tank.subsurface(( 0, 0),(48, 48))
            self.tank_R1 = self.tank.subsurface((48, 0),(48, 48))
        elif self.dir_x == 0 and self.dir_y == 1:
            self.tank_R0 = self.tank.subsurface(( 0, 48),(48, 48))
            self.tank_R1 = self.tank.subsurface((48, 48),(48, 48))
        elif self.dir_x == -1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface(( 0, 96),(48, 48))
            self.tank_R1 = self.tank.subsurface((48, 96),(48, 48))
        elif self.dir_x == 1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface(( 0, 144),(48, 48))
            self.tank_R1 = self.tank.subsurface((48, 144),(48, 48))
        
        

        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            self.dir_x, self.dir_y = random.choice(([0,1],[0,-1],[1,0],[-1,0]))
        elif self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            self.dir_x, self.dir_y = random.choice(([0,1],[0,-1],[1,0],[-1,0]))
        elif self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0,1],[0,-1],[1,0],[-1,0]))
        elif self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0,1],[0,-1],[1,0],[-1,0]))

        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None) \
            or pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.dir_x, self.speed * -self.dir_y)
            self.dir_x, self.dir_y = random.choice(([0,1],[0,-1],[1,0],[-1,0]))
