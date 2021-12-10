import pygame
import sys
import tankfactory

pygame.init() 
resolution = 630, 630
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Tank War ")
background_image     = pygame.image.load(r"image\background.png")
screen.blit(background_image, (0, 0))
clock = pygame.time.Clock()

factory=tankfactory.TankFactory()
test=factory.createTank(1)

screen.blit(test.tank_R0, (test.rect.left, test.rect.top))

pygame.display.flip()
clock.tick(60)
print(test.life)
