import pygame
import random

screen_width = 1200
screen_height = 800

class bintang(object):
    def __init__(self):
        self.img = pygame.image.load('Assets/Object/star.png')
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.spawnPoint = random.choice([(random.randrange(0, screen_width - self.width), random.choice([-1*self.height - 5, screen_height + 5])), (random.choice([-1 * self.width - 5, screen_width + 5]), random.randrange(0, screen_height-self.height))])
        self.x, self.y = self.spawnPoint

        if self.x < screen_width//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < screen_height//2:
            self.ydir = 1
        else:
            self.ydir = -1

        self.xv = self.xdir * 2
        self.yv = self.ydir * 2
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

        
