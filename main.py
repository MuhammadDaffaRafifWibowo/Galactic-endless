import pygame
import math
import random

pygame.init()
 
screen_width = 1200
screen_height = 800

background = pygame.image.load('mappp/7.png')
alien_img = pygame.image.load('ufo (1)/6.png')
ufo_img = pygame.image.load('ufo (1)/8.png')
player_img = pygame.image.load('DurrrSpaceShip.png')
bintang_img = pygame.image.load('star.png')
ally_img = pygame.image.load('fighter.png')

pygame.display.set_caption('Galactic Endless')
window = pygame.display.set_mode((screen_width, screen_height ))

clock = pygame.time.Clock()

Gameover = False
nyawa = 3
score = 0
machineGun = False


class player(object):
    def __init__(self):
        self.img = player_img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = screen_width//2
        self.y = screen_height//2
        #sudut dimana pemain sedang menghadap
        self.sudut = 0 
        #untuk merotasi pesawat player dan memberikan nilai baru dari gambar ketika sedang berotasi
        self.rotasiSurf = pygame.transform.rotate(self.img, self.sudut)
        self.rotasiRect = self.rotasiSurf.get_rect()
        #Membenarkan posisi pesawat agar berada di tengah window
        self.rotasiRect.center = (self.x, self.y)
        self.cosin = math.cos(math.radians(self.sudut + 90))
        self.sin = math.sin(math.radians(self.sudut + 90))
        #Memberi tahu dimana posisi depan kita
        self.head = (self.x + self.cosin * self.width//2, self.y - self.sin * self.height//2)


    def draw(self, window):
        #window.blit(self.img,[self.x, self.y, self.width, self.height])
        window.blit(self.rotasiSurf, self.rotasiRect)

    def putarKiri(self):
        self.sudut += 5 
        self.rotasiSurf = pygame.transform.rotate(self.img, self.sudut)
        self.rotasiRect = self.rotasiSurf.get_rect()
        self.rotasiRect.center = (self.x, self.y)
        self.cosin = math.cos(math.radians(self.sudut + 90))
        self.sin = math.sin(math.radians(self.sudut + 90))
        self.head = (self.x + self.cosin * self.width//2,  self.y - self.sin * self.height//2)

    def putarKanan(self):
        self.sudut -= 5 
        self.rotasiSurf = pygame.transform.rotate(self.img, self.sudut)
        self.rotasiRect = self.rotasiSurf.get_rect()
        self.rotasiRect.center = (self.x, self.y)
        self.cosin = math.cos(math.radians(self.sudut + 90))
        self.sin = math.sin(math.radians(self.sudut + 90))
        self.head = (self.x + self.cosin * self.width//2,  self.y - self.sin * self.height//2)

    def maju(self):
        self.x += self.cosin * 6
        self.y -= self.sin * 6
        self.rotasiSurf = pygame.transform.rotate(self.img, self.sudut)
        self.rotasiRect = self.rotasiSurf.get_rect()
        self.rotasiRect.center = (self.x, self.y)
        self.cosin = math.cos(math.radians(self.sudut + 90))
        self.sin = math.sin(math.radians(self.sudut + 90))
        self.head = (self.x + self.cosin * self.width//2,  self.y - self.sin * self.height//2)

    def batasRenderPlayer(self):
        if self.x > screen_width + 50 :
            self.x = 0
        elif self.x < 0 - self.width :
            self.x = screen_width
        elif self.y < -50 :
            self.y = screen_height
        elif self.y > screen_height + 50:
            self.y = 0
