import pygame
import state
import tool
import sys

class WinScreen(state.State):
    def __init__(self,screen):
        self.mytool=tool.Tool()
        self.screen=screen
        self.next='store'
        self.end=False

    def play(self):
        while self.end!=True:
            self.myEvent()
            self.draw()
            pygame.display.flip()

    def startup(self):
        self.end=False

    def myEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.end=True

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw(self):
        self.screen.blit(self.mytool.background_image, (0, 0))
        win_font = pygame.font.SysFont(None, 60)
        win_surface = win_font.render('You Win!', True, (255, 255, 255))
        head_font = pygame.font.SysFont(None, 60)
        text_surface = head_font.render('Press s to continue', True, (255, 255, 255))
        self.screen.blit(win_surface, (150, 180))
        self.screen.blit(text_surface, (150, 280))


class LooseScreen(state.State):
    def __init__(self,screen):
        self.mytool=tool.Tool()
        self.screen=screen
        self.next='menu'
        self.end=False

    def play(self):
        while self.end!=True:
            self.myEvent()
            self.draw()
            pygame.display.flip()

    def startup(self):
        self.end=False

    def myEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.end=True

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw(self):
        self.screen.blit(self.mytool.background_image, (0, 0))
        win_font = pygame.font.SysFont(None, 60)
        win_surface = win_font.render('You Lose!', True, (255, 255, 255))
        head_font = pygame.font.SysFont(None, 60)
        text_surface = head_font.render('Press s to continue', True, (255, 255, 255))
        self.screen.blit(win_surface, (150, 180))
        self.screen.blit(text_surface, (150, 280))
        
