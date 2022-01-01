# -*- coding: utf-8 -*-
import pygame
import sys
import traceback
import tool
import level

def main():
    pygame.init()   
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    mytool=tool.Tool()
    mytool.start_sound.play()
    
    mylevel=level.Level(1,2,screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    mytool.bang_sound.play()
                    mylevel.play()
                    mylevel.reset()

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(mytool.background_image, (0, 0))
        head_font = pygame.font.SysFont(None, 60)
        text_surface = head_font.render('Press s to start!', True, (255, 255, 255))
        screen.blit(text_surface, (150, 280))
        pygame.display.flip()

        
    
    
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()