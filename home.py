import pygame

class Home(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(r"image\home.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 3 + 12 * 24, 3 + 24 * 24
        self.life=True

