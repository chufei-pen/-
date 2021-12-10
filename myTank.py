import pygame
import bulletClass


tank_T1_0 = r"image\tank_T1_0.png"
tank_T1_1 = r"image\tank_T1_1.png"
tank_T1_2 = r"image\tank_T1_2.png"
tank_T2_0 = r"image\tank_T2_0.png"
tank_T2_1 = r"image\tank_T2_1.png"
tank_T2_2 = r"image\tank_T2_2.png"

       

class MyTank(pygame.sprite.Sprite):
    def __init__(self, playerNumber):
        pygame.sprite.Sprite.__init__(self)
        

        if playerNumber == 1:
            self.tank_L0_image = pygame.image.load(tank_T1_2).convert_alpha()
        if playerNumber == 2:
            self.tank_L0_image = pygame.image.load(tank_T2_2).convert_alpha()
        

        self.tank = self.tank_L0_image

        self.tank_R0 = self.tank.subsurface((0, 0),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0),(48, 48))
        self.rect = self.tank_R0.get_rect()
        if playerNumber == 1:
            self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24 
        if playerNumber == 2:
            self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24 


        self.fire = 1
        self.speed = 3
        self.life=3
        self.dir_x, self.dir_y = 0, -1
        self.coin=0
        self.bulletNotCooling = True
        self.bullet = bulletClass.Bullet()
        #self.bullet.rect.left, self.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
    
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
        
        self.bullet.speed  = 12

        
    

        

    def moveUp(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        self.tank_R0 = self.tank.subsurface((0, 0),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0),(48, 48))
        self.dir_x, self.dir_y = 0, -1
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        return False
    def moveDown(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        self.tank_R0 = self.tank.subsurface((0, 48),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48),(48, 48))
        self.dir_x, self.dir_y = 0, 1
        if self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        return False
    def moveLeft(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 96),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 96),(48, 48))
        self.dir_x, self.dir_y = -1, 0
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        return False
    def moveRight(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 144),(48, 48))
        self.tank_R1 = self.tank.subsurface((48, 144),(48, 48))
        self.dir_x, self.dir_y = 1, 0
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        return False