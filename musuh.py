import pygame
import random

screen_width = 1200
screen_height = 800

class musuh(object):
    def __init__(self, jenis):
        self.jenis = jenis
        if self.jenis == 1 :
            self.img = pygame.image.load('Assets/Enemy/ufo.png')
        elif self.jenis == 2 :
            self.img = pygame.image.load('Assets/Enemy/megaUfo.png')
        
        self.width = 50 * jenis
        self.height = 50 * jenis
        self.spawnPoint = random.choice([(random.randrange(0, screen_width-self.width), random.choice([-1*self.height - 5, screen_height + 5])), (random.choice([-1 * self.width - 5, screen_width + 5]), random.randrange(0, screen_height-self.height))])
        self.x, self.y = self.spawnPoint

        if self.x < screen_width//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < screen_height//2:
            self.ydir = 1
        else:
            self.ydir = -1

        self.xv = self.xdir * random.randrange(1,2)    
        self.yv = self.ydir * random.randrange(1,2)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))