import pygame
import sys
import traceback
import tool
import level
import endScreen
import menu
import myTank
import store


def main():
    pygame.init()   
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    mytool=tool.Tool()
    mytool.start_sound.play()
    done=False
    player1 = myTank.MyTank(1)
    player2 = myTank.MyTank(2)

    stateDic={
        'menu':menu.Menu(screen),
        'level':level.Level(screen),
        'win':endScreen.WinScreen(screen),
        'loose':endScreen.LooseScreen(screen),
        'store':store.Store(screen)
    }
    stateName='menu'

    while not done:
        nowState=stateDic[stateName]
        if stateName=="level":
            nowState.startup(player1,player2)
        elif stateName=="store":
            player1,player2=nowState.startup(player1,player2)
        else:
            nowState.startup()
        nowState.play()
        stateName=nowState.next
        if stateName=="menu":
            player1 = myTank.MyTank(1)
            player2 = myTank.MyTank(2)


        
    
    
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
