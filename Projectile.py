import pygame
from os import path
import math
vec = pygame.math.Vector2

img = path.join(path.dirname("__file__"),'ImageList')
imgdirectory = path.join(path.dirname("__file__"),'img')
bulletimg = pygame.image.load(path.join(imgdirectory,"laserBlue04.png")).convert()

pygame.init()
sHeight = 800
sWidth = 1000
screen = pygame.display.set_mode((sWidth,sHeight))

red = (255,0,0)
torqouise = (89,147,222)
green = (181,213,205)
black = (0,0,0)
grey = (0,0,100)
blue = (0,255,0)
white = (255,255,255)

class projectile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bulletimg,(13,37))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -25

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()