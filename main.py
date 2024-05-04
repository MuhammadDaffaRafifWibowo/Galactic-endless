import pygame
import os
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Turtle Graphics Game")

# Load images
background = pygame.image.load("starfield.gif")
player_img = pygame.image.load("triangle.png")
enemy_img = pygame.image.load("circle.png")
bullet_img = pygame.image.load("triangle.png")
ally_img = pygame.image.load("square.png")

# Load sounds
laser_sound = pygame.mixer.Sound("laser.mp3")
explosion_sound = pygame.mixer.Sound("explosion.mp3")
