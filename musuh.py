import pygame
import random

screen_width = 1200
screen_height = 800

class Musuh:
    def __init__(self, jenis, img_path, size_multiplier):
        self.jenis = jenis
        self.img = pygame.image.load(img_path)
        self.width = 50 * size_multiplier
        self.height = 50 * size_multiplier
        self.spawnPoint = random.choice([(random.randrange(0, screen_width - self.width), random.choice([-1 * self.height - 5, screen_height + 5])),
                                         (random.choice([-1 * self.width - 5, screen_width + 5]), random.randrange(0, screen_height - self.height))])
        self.x, self.y = self.spawnPoint

        if self.x < screen_width // 2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < screen_height // 2:
            self.ydir = 1
        else:
            self.ydir = -1

        self.xv = self.xdir * random.randrange(1, 2)
        self.yv = self.ydir * random.randrange(1, 2)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


class Ufo(Musuh):
    def __init__(self):
        super().__init__(jenis=1, img_path='Assets/Enemy/ufo.png', size_multiplier=1)


class MegaUfo(Musuh):
    def __init__(self):
        super().__init__(jenis=2, img_path='Assets/Enemy/megaUfo.png', size_multiplier=2)
