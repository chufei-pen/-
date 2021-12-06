import pygame

class Tool():
    def __init__(self):
        # 加载音乐,音效.
        pygame.mixer.init()
        self.start_sound         = pygame.mixer.Sound(r"music\start.wav")
        self.add_sound           = pygame.mixer.Sound(r"music\add.wav")
        self.blast_sound         = pygame.mixer.Sound(r"music\blast.wav")
        self.fire_sound          = pygame.mixer.Sound(r"music\fire.wav")
        self.gunFire_sound       = pygame.mixer.Sound(r"music\Gunfire.wav")
        self.hit_sound           = pygame.mixer.Sound(r"music\hit.wav")
        self.bang_sound          = pygame.mixer.Sound(r"music\bang.wav")
        self.bang_sound.set_volume(1)
        self.background_image     = pygame.image.load(r"image\background.png")