import pygame
import sys
import tool
import wall
import myTank
import enemyTank
import food
import level 
import home

class Level():
    def __init__(self,levels,players,screen):
        self.levels=levels
        self.players=players
        self.screen=screen
        self.mytool=tool.Tool()
        # 定义精灵组:坦克，我方坦克，敌方坦克，敌方子弹
        self.allTankGroup     = pygame.sprite.Group()
        self.mytankGroup      = pygame.sprite.Group()
        self.allEnemyGroup    = pygame.sprite.Group()
        self.redEnemyGroup    = pygame.sprite.Group()
        self.greenEnemyGroup  = pygame.sprite.Group()
        self.otherEnemyGroup  = pygame.sprite.Group()  
        self.enemyBulletGroup = pygame.sprite.Group()
        # 创建地图 
        self.bgMap = wall.Map()
        # 创建食物/道具 但不显示
        self.prop = food.Food()
        #創建家
        self.myhome=home.Home()
        # 创建我方坦克
        self.myTank_T1 = myTank.MyTank(1)
        self.allTankGroup.add(self.myTank_T1)
        self.mytankGroup.add(self.myTank_T1)
        self.myTank_T2 = myTank.MyTank(2)
        self.allTankGroup.add(self.myTank_T2)
        self.mytankGroup.add(self.myTank_T2)
        # 创建敌方 坦克
        for i in range(1, 4):
            enemy = enemyTank.EnemyTank(i)
            self.allTankGroup.add(enemy)
            self.allEnemyGroup.add(enemy)
            if enemy.isred == True:
                self.redEnemyGroup.add(enemy)
                continue
            if enemy.kind == 3:
                self.greenEnemyGroup.add(enemy)
                continue
            self.otherEnemyGroup.add(enemy)
        # 敌军坦克出现动画
        appearance_image = pygame.image.load(r"image\appear.png").convert_alpha()
        self.appearance = []
        self.appearance.append(appearance_image.subsurface(( 0, 0), (48, 48)))
        self.appearance.append(appearance_image.subsurface((48, 0), (48, 48)))
        self.appearance.append(appearance_image.subsurface((96, 0), (48, 48)))

        self.delay = 100
        self.moving = 0
        self.movdir = 0
        self.moving2 = 0
        self.movdir2 = 0
        self.enemyNumber = 3
        self.enemyCouldMove      = True
        self.switch_R1_R2_image  = True
        self.running_T1          = True
        self.running_T2          = True
        self.clock = pygame.time.Clock()
        self.end=False
        # 自定义事件
        # 创建敌方坦克延迟200
        self.DELAYEVENT = pygame.constants.USEREVENT
        pygame.time.set_timer(self.DELAYEVENT, 200)
        # 创建 敌方 子弹延迟1000
        self.ENEMYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 1
        pygame.time.set_timer(self.ENEMYBULLETNOTCOOLINGEVENT, 1000)
        # 创建 我方 子弹延迟200
        self.MYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 2
        pygame.time.set_timer(self.MYBULLETNOTCOOLINGEVENT, 200)
        # 敌方坦克 静止8000
        self.NOTMOVEEVENT = pygame.constants.USEREVENT + 3
        pygame.time.set_timer(self.NOTMOVEEVENT, 8000)
    
    def reset(self):
        # 定义精灵组:坦克，我方坦克，敌方坦克，敌方子弹
        self.allTankGroup     = pygame.sprite.Group()
        self.mytankGroup      = pygame.sprite.Group()
        self.allEnemyGroup    = pygame.sprite.Group()
        self.redEnemyGroup    = pygame.sprite.Group()
        self.greenEnemyGroup  = pygame.sprite.Group()
        self.otherEnemyGroup  = pygame.sprite.Group()  
        self.enemyBulletGroup = pygame.sprite.Group()
        # 创建地图 
        self.bgMap = wall.Map()
        # 创建食物/道具 但不显示
        self.prop = food.Food()
        #創建家
        self.myhome=home.Home()
        # 创建我方坦克
        self.myTank_T1 = myTank.MyTank(1)
        self.allTankGroup.add(self.myTank_T1)
        self.mytankGroup.add(self.myTank_T1)
        self.myTank_T2 = myTank.MyTank(2)
        self.allTankGroup.add(self.myTank_T2)
        self.mytankGroup.add(self.myTank_T2)
        # 创建敌方 坦克
        for i in range(1, 4):
            enemy = enemyTank.EnemyTank(i)
            self.allTankGroup.add(enemy)
            self.allEnemyGroup.add(enemy)
            if enemy.isred == True:
                self.redEnemyGroup.add(enemy)
                continue
            if enemy.kind == 3:
                self.greenEnemyGroup.add(enemy)
                continue
            self.otherEnemyGroup.add(enemy)
        self.delay = 100
        self.moving = 0
        self.movdir = 0
        self.moving2 = 0
        self.movdir2 = 0
        self.enemyNumber = 3
        self.enemyCouldMove      = True
        self.switch_R1_R2_image  = True
        self.running_T1          = True
        self.running_T2          = True
        self.clock = pygame.time.Clock()
        self.end=False

    def play(self):
        while self.end!=True:
            self.myEvent()
            self.running_T1,self.moving,self.movdir=self.keyAction(self.moving,self.myTank_T1,self.running_T1,self.movdir)
            #self.moving2,self.running_T2,self.movdir2=self.keyAction(self.moving2,self.myTank_T2,self.running_T2,self.movdir2)
            self.draw()
            self.delay -= 1
            if not self.delay:
                self.delay = 100    
            
            pygame.display.flip()
            self.clock.tick(60)

    def myEvent(self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # 我方子弹冷却事件
            if event.type == self.MYBULLETNOTCOOLINGEVENT:
                self.myTank_T1.bulletNotCooling = True
                print("我方子彈冷卻")
            # 敌方子弹冷却事件
            if event.type == self.ENEMYBULLETNOTCOOLINGEVENT:
                for each in self.allEnemyGroup:
                    each.bulletNotCooling = True
            
            # 敌方坦克静止事件
            if event.type == self.NOTMOVEEVENT:
                self.enemyCouldMove = True
                print("敵人可以移動")
            # 创建敌方坦克延迟
            if event.type == self.DELAYEVENT:
                if self.enemyNumber < 4:
                    enemy = enemyTank.EnemyTank()
                    if pygame.sprite.spritecollide(enemy, self.allTankGroup, False, None):
                        break
                    self.allEnemyGroup.add(enemy)
                    self.allTankGroup.add(enemy)
                    self.enemyNumber += 1
                    if enemy.isred == True:
                        self.redEnemyGroup.add(enemy)
                    elif enemy.kind == 3:
                        self.greenEnemyGroup.add(enemy)
                    else:
                        self.otherEnemyGroup.add(enemy)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()
            
                if event.key == pygame.K_e:
                    self.myTank_T1.levelUp()
                if event.key == pygame.K_q:
                    self.myTank_T1.levelDown()
                if event.key == pygame.K_3:
                    self.myTank_T1.levelUp()
                    self.myTank_T1.levelUp()
                    self.myTank_T1.level = 3
                if event.key == pygame.K_1:
                    for x, y in [(11,23),(12,23),(13,23),(14,23),(11,24),(14,24),(11,25),(14,25)]:
                        self.bgMap.brick = wall.Brick()
                        self.bgMap.brick.rect.left, self.bgMap.brick.rect.top = 3 + x * 24, 3 + y * 24
                        self.bgMap.brickGroup.add(self.bgMap.brick)                
                if event.key == pygame.K_4:
                    for x, y in [(11,23),(12,23),(13,23),(14,23),(11,24),(14,24),(11,25),(14,25)]:
                        self.bgMap.iron = wall.Iron()
                        self.bgMap.iron.rect.left, self.bgMap.iron.rect.top = 3 + x * 24, 3 + y * 24
                        self.bgMap.ironGroup.add(self.bgMap.iron)

    def  keyAction(self,moving,myTank,running,movdir):
        # 检查用户的键盘操作
        key_pressed = pygame.key.get_pressed()
        # 玩家一的移动操作
        if moving:
            moving -= 1
            if movdir == 0:
                self.allTankGroup.remove(myTank)
                if myTank.moveUp(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup):
                    moving += 1
                self.allTankGroup.add(myTank)
                running = True
            if movdir == 1:
                self.allTankGroup.remove(myTank)
                if myTank.moveDown(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup):
                    moving += 1
                self.allTankGroup.add(myTank)
                running = True
            if movdir == 2:
                self.allTankGroup.remove(myTank)
                if myTank.moveLeft(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup):
                    moving += 1
                self.allTankGroup.add(myTank)
                running = True
            if movdir == 3:
                self.allTankGroup.remove(myTank)
                if myTank.moveRight(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup):
                    moving += 1
                self.allTankGroup.add(myTank)
                running = True
                
        if not moving:
            if key_pressed[pygame.K_w]:
                moving = 7
                movdir = 0
                running = True
                self.allTankGroup.remove(myTank)
                if myTank.moveUp(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup):
                    moving = 0
                self.allTankGroup.add(myTank)
            elif key_pressed[pygame.K_s]:
                moving = 7
                movdir = 1
                running = True
                self.allTankGroup.remove(myTank)
                if myTank.moveDown(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup):
                    moving = 0
                self.allTankGroup.add(myTank)
            elif key_pressed[pygame.K_a]:
                moving = 7
                movdir = 2
                running = True
                self.allTankGroup.remove(myTank)
                if myTank.moveLeft(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup):
                    moving = 0
                self.allTankGroup.add(myTank)
            elif key_pressed[pygame.K_d]:
                moving = 7
                movdir = 3
                running = True
                self.allTankGroup.remove(myTank)
                if myTank.moveRight(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup):
                    moving = 0
                self.allTankGroup.add(myTank)
        if key_pressed[pygame.K_SPACE]:
            if not myTank.bullet.life and myTank.bulletNotCooling:
                self.mytool.fire_sound.play()
                myTank.shoot()
                myTank.bulletNotCooling = False
        return running , moving , movdir
    
    def draw(self):
        # 画背景
        self.screen.blit(self.mytool.background_image, (0, 0))
        # 画砖块
        for each in self.bgMap.brickGroup:
            self.screen.blit(each.image, each.rect)        
        # 花石头
        for each in self.bgMap.ironGroup:
            self.screen.blit(each.image, each.rect)        
        # 画home
        if self.myhome.life:
            self.screen.blit(self.myhome.image, self.myhome.rect)
            for each in self.allTankGroup:
                if pygame.sprite.collide_rect(each.bullet, self.myhome):
                    self.mytool.bang_sound.play()
                    self.end=True
        # 画我方坦克1
        if not (self.delay % 5):
            self.switch_R1_R2_image = not self.switch_R1_R2_image
        if self.switch_R1_R2_image and self.running_T1:
            self.screen.blit(self.myTank_T1.tank_R0, (self.myTank_T1.rect.left, self.myTank_T1.rect.top))
            self.running_T1 = False
        else:
            self.screen.blit(self.myTank_T1.tank_R1, (self.myTank_T1.rect.left, self.myTank_T1.rect.top))
        # 画我方坦克2
        if self.switch_R1_R2_image and self.running_T2:
            self.screen.blit(self.myTank_T2.tank_R0, (self.myTank_T2.rect.left, self.myTank_T2.rect.top))
            self.running_T2 = False
        else:
            self.screen.blit(self.myTank_T2.tank_R1, (self.myTank_T2.rect.left, self.myTank_T2.rect.top))    
        # 画敌方坦克
        for each in self.allEnemyGroup:
            # 判断5毛钱特效是否播放            
            if each.flash:
                #　判断画左动作还是右动作
                if self.switch_R1_R2_image:
                    self.screen.blit(each.tank_R0, (each.rect.left, each.rect.top))
                    if self.enemyCouldMove:
                        self.allTankGroup.remove(each)
                        each.move(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup)
                        self.allTankGroup.add(each)
                else:
                    self.screen.blit(each.tank_R1, (each.rect.left, each.rect.top))
                    if self.enemyCouldMove:
                        self.allTankGroup.remove(each)
                        each.move(self.allTankGroup, self.bgMap.brickGroup, self.bgMap.ironGroup)
                        self.allTankGroup.add(each)                    
            else:
                # 播放5毛钱特效
                if each.times > 0:
                    each.times -= 1
                    if each.times <= 10:
                        self.screen.blit(self.appearance[2], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 20:
                        self.screen.blit(self.appearance[1], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 30:
                        self.screen.blit(self.appearance[0], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 40:
                        self.screen.blit(self.appearance[2], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 50:
                        self.screen.blit(self.appearance[1], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 60:
                        self.screen.blit(self.appearance[0], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 70:
                        self.screen.blit(self.appearance[2], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 80:
                        self.screen.blit(self.appearance[1], (3 + each.x * 12 * 24, 3))
                    elif each.times <= 90:
                        self.screen.blit(self.appearance[0], (3 + each.x * 12 * 24, 3))
                if each.times == 0:
                    each.flash = True
    
                
        # 绘制我方子弹1
        if self.myTank_T1.bullet.life:
            self.myTank_T1.bullet.move()    
            self.screen.blit(self.myTank_T1.bullet.bullet, self.myTank_T1.bullet.rect)
            # 子弹 碰撞 子弹
            for each in self.enemyBulletGroup:
                if each.life:
                    if pygame.sprite.collide_rect(self.myTank_T1.bullet, each):
                        self.myTank_T1.bullet.life = False
                        each.life = False
                        pygame.sprite.spritecollide(self.myTank_T1.bullet, self.enemyBulletGroup, True, None)
            # 子弹 碰撞 敌方坦克
            if pygame.sprite.spritecollide(self.myTank_T1.bullet, self.redEnemyGroup, True, None):
                self.prop.change()
                self.mytool.bang_sound.play()
                self.enemyNumber -= 1
                self.myTank_T1.bullet.life = False
            elif pygame.sprite.spritecollide(self.myTank_T1.bullet,self.greenEnemyGroup, False, None):
                for each in self.greenEnemyGroup:
                    if pygame.sprite.collide_rect(self.myTank_T1.bullet, each):
                        if each.life == 1:
                            pygame.sprite.spritecollide(self.myTank_T1.bullet,self.greenEnemyGroup, True, None)
                            self.mytool.bang_sound.play()
                            self.enemyNumber -= 1
                        elif each.life == 2:
                            each.life -= 1
                            each.tank = each.enemy_3_0
                        elif each.life == 3:
                            each.life -= 1
                            each.tank = each.enemy_3_2
                self.myTank_T1.bullet.life = False
            elif pygame.sprite.spritecollide(self.myTank_T1.bullet, self.otherEnemyGroup, True, None):
                self.mytool.bang_sound.play()
                self.enemyNumber -= 1
                self.myTank_T1.bullet.life = False    
            #if pygame.sprite.spritecollide(myTank_T1.bullet, allEnemyGroup, True, None):
            #    bang_sound.play()
            #    enemyNumber -= 1
            #    myTank_T1.bullet.life = False
            # 子弹 碰撞 brickGroup
            if pygame.sprite.spritecollide(self.myTank_T1.bullet, self.bgMap.brickGroup, True, None):
                self.myTank_T1.bullet.life = False
                self.myTank_T1.bullet.rect.left, self.myTank_T1.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
            # 子弹 碰撞 ironGroup
            if self.myTank_T1.bullet.strong:
                if pygame.sprite.spritecollide(self.myTank_T1.bullet, self.bgMap.ironGroup, True, None):
                    self.myTank_T1.bullet.life = False
                    self.myTank_T1.bullet.rect.left, self.myTank_T1.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
            else:    
                if pygame.sprite.spritecollide(self.myTank_T1.bullet, self.bgMap.ironGroup, False, None):
                    self.myTank_T1.bullet.life = False
                    self.myTank_T1.bullet.rect.left, self.myTank_T1.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
        
        # 绘制我方子弹2
        if self.myTank_T2.bullet.life:
            self.myTank_T2.bullet.move()    
            self.screen.blit(self.myTank_T2.bullet.bullet, self.myTank_T2.bullet.rect)
            # 子弹 碰撞 敌方坦克
            if pygame.sprite.spritecollide(self.myTank_T2.bullet, self.allEnemyGroup, True, None):
                self.mytool.bang_sound.play()
                self.enemyNumber -= 1
                self.myTank_T2.bullet.life = False
            # 子弹 碰撞 brickGroup
            if pygame.sprite.spritecollide(self.myTank_T2.bullet, self.bgMap.brickGroup, True, None):
                self.myTank_T2.bullet.life = False
                self.myTank_T2.bullet.rect.left, self.myTank_T2.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
            # 子弹 碰撞 brickGroup
            if self.myTank_T2.bullet.strong:
                if pygame.sprite.spritecollide(self.myTank_T2.bullet, self.bgMap.ironGroup, True, None):
                    self.myTank_T2.bullet.life = False
                    self.myTank_T2.bullet.rect.left, self.myTank_T2.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
            else:    
                if pygame.sprite.spritecollide(self.myTank_T2.bullet, self.bgMap.ironGroup, False, None):
                    self.myTank_T2.bullet.life = False
                    self.myTank_T2.bullet.rect.left, self.myTank_T2.bullet.rect.right = 3 + 12 * 24, 3 + 24 * 24
        

        # 绘制敌人子弹
        for each in self.allEnemyGroup:
            # 如果子弹没有生命，则赋予子弹生命
            if not each.bullet.life and each.bulletNotCooling and self.enemyCouldMove:
                self.enemyBulletGroup.remove(each.bullet)
                each.shoot()
                self.enemyBulletGroup.add(each.bullet)
                each.bulletNotCooling = False
            # 如果5毛钱特效播放完毕 并且 子弹存活 则绘制敌方子弹
            if each.flash:
                if each.bullet.life:
                    # 如果敌人可以移动
                    if self.enemyCouldMove:
                        each.bullet.move()
                    self.screen.blit(each.bullet.bullet, each.bullet.rect)
                    # 子弹 碰撞 我方坦克
                    if pygame.sprite.collide_rect(each.bullet, self.myTank_T1):
                        self.mytool.bang_sound.play()
                        self.myTank_T1.rect.left, self.myTank_T1.rect.top = 3 + 8 * 24, 3 + 24 * 24 
                        each.bullet.life = False
                        self.moving = 0  # 重置移动控制参数
                        for i in range(self.myTank_T1.level+1):
                            self.myTank_T1.levelDown()
                    if pygame.sprite.collide_rect(each.bullet, self.myTank_T2):
                        self.mytool.bang_sound.play()
                        self.myTank_T2.rect.left, self.myTank_T2.rect.top = 3 + 16 * 24, 3 + 24 * 24 
                        each.bullet.life = False
                    # 子弹 碰撞 brickGroup
                    if pygame.sprite.spritecollide(each.bullet, self.bgMap.brickGroup, True, None):
                        each.bullet.life = False
                    # 子弹 碰撞 ironGroup
                    if each.bullet.strong:
                        if pygame.sprite.spritecollide(each.bullet, self.bgMap.ironGroup, True, None):
                            each.bullet.life = False
                    else:    
                        if pygame.sprite.spritecollide(each.bullet, self.bgMap.ironGroup, False, None):
                            each.bullet.life = False
            
        # 最后画食物/道具
        if self.prop.life:
            self.screen.blit(self.prop.image, self.prop.rect)
            # 我方坦克碰撞 食物/道具
            if pygame.sprite.collide_rect(self.myTank_T1, self.prop):
                if self.prop.kind == 1:  # 敌人全毁
                    for each in self.allEnemyGroup:
                        if pygame.sprite.spritecollide(each, self.allEnemyGroup, True, None):
                            self.mytool.bang_sound.play()
                            self.enemyNumber -= 1
                    self.prop.life = False
                if self.prop.kind == 2:  # 敌人静止
                    self.enemyCouldMove = False
                    self.prop.life = False
                if self.prop.kind == 3:  # 子弹增强
                    self.myTank_T1.bullet.strong = True
                    self.prop.life = False
                if self.prop.kind == 4:  # 家得到保护
                    for x, y in [(11,23),(12,23),(13,23),(14,23),(11,24),(14,24),(11,25),(14,25)]:
                        self.bgMap.iron = wall.Iron()
                        self.bgMap.iron.rect.left, self.bgMap.iron.rect.top = 3 + x * 24, 3 + y * 24
                        self.bgMap.ironGroup.add(bgMap.iron)                
                    self.prop.life = False
                if self.prop.kind == 5:  # 坦克无敌
                    self.prop.life = False
                    pass
                if self.prop.kind == 6:  # 坦克升级
                    self.myTank_T1.levelUp()
                    self.prop.life = False
                if self.prop.kind == 7:  # 坦克生命+1
                    self.myTank_T1.life += 1
                    self.prop.life = False

            