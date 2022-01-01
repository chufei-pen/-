import pygame
import sys
import traceback
import tool
import level
import endScreen
import menu

def main():
    pygame.init()   
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    mytool=tool.Tool()
    mytool.start_sound.play()
    done=False
    stateDic={
        'menu':menu.Menu(screen),
        'level':level.Level(screen),
        'win':endScreen.WinScreen(screen),
        'loose':endScreen.LooseScreen(screen)
    }
    stateName='menu'

    while not done:
        nowState=stateDic[stateName]
        nowState.startup()
        nowState.play()
        stateName=nowState.next


        
    
    
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
