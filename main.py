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

class peluru(object):
    def _init_(self):
        self.point = player.head
        self.x, self.y = self.point
        self.width = 4
        self.height = 4
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
        
class musuh(object):
    def _init_(self, jenis):
        self.jenis = jenis
        if self.jenis == 1 :
            self.img = alien_img
        elif self.jenis == 2 :
            self.img = ufo_img
        
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
