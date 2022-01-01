import tool
import pygame
import state
import sys

class Store(state.State):
    def __init__(self,screen):
        self.mytool=tool.Tool()
        self.screen=screen
        self.next='level'
        self.end=False
        


    def play(self):
        while self.end!=True:
            self.myEvent()
            self.draw()
            pygame.display.flip()

    def startup(self,player1,player2):
        self.end=False
        self.player1=player1
        self.player2=player2
        self.player1.fire+=1
        self.player2.fire+=1
        return self.player1,self.player2

    def myEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.mytool.bang_sound.play()
                    self.end=True
                

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.blit(self.mytool.background_image, (0, 0))
        head_font = pygame.font.SysFont(None, 60)
        text_surface = head_font.render('Press s to Buy!', True, (255, 255, 255))
        self.screen.blit(text_surface, (150, 280))