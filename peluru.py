import pygame

from player import player

screen_width = 1200
screen_height = 800

class peluru(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.width = 5
        self.height = 5
        self.cosin = player.cosin
        self.sin = player.sin
        #velocity peluru
        self.xv = self.cosin * 10
        self.yv = self.sin * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), [self.x, self.y, self.width, self.height])

    def batasRenderPeluru(self):
        if self.x < -50 or self.x > screen_width or self.y > screen_height or self.y < -50:
            return True
        
