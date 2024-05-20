import pygame
import random
import math

screen_width = 1200
screen_height = 800

class ally(object):
    def __init__(self):
        self.img = pygame.image.load('Assets/Player/ally.png')
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.spawnPoint = random.choice([
            (random.randrange(0, screen_width-self.width), random.choice([-1*self.height - 5, screen_height + 5])),
            (random.choice([-1 * self.width - 5, screen_width + 5]), random.randrange(0, screen_height-self.height))
        ])
        self.x, self.y = self.spawnPoint

        if self.x < screen_width // 2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < screen_height // 2:
            self.ydir = 1
        else:
            self.ydir = -1
        
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)

        # Hitung sudut rotasi
        self.angle = math.degrees(math.atan2(self.xv, -self.yv))

    def draw(self, window):
        # Rotasi gambar sesuai dengan sudut yang dihitung
        rotated_img = pygame.transform.rotate(self.img, -self.angle)
        new_rect = rotated_img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        window.blit(rotated_img, new_rect.topleft)
