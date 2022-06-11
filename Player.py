import pygame
from os import path
import math
from Utils import blit_rotate_center

img = path.join(path.dirname("__file__"),'ImageList')
imgdirectory = path.join(path.dirname("__file__"),'img')


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

tankSprite = pygame.image.load(path.join(img,"TankSprite.png")).convert()

class AbstractPlayer:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.img.set_colorkey((255, 255, 255))
        self.img_copy = self.IMG.copy()
        self.rect = self.img_copy.get_rect()
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
        self.last_update = pygame.time.get_ticks()

    def rotate(self, left=False, right=False):
        currtime = pygame.time.get_ticks()
        if currtime - self.last_update > 50:
            self.last_update = currtime
            if left:
                self.angle = (self.angle + self.rotation_vel)
                new_image = pygame.transform.rotate(self.IMG, self.angle)
                self.img_copy = new_image
            elif right:
                self.angle = (self.angle - self.rotation_vel)
                new_image = pygame.transform.rotate(self.IMG, self.angle)
                self.img_copy = new_image

    def draw(self, screen):
        blit_rotate_center(screen, self.img,(self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

class Player(AbstractPlayer):
    IMG = tankSprite
    START_POS = (sWidth/2,sHeight/2)
    # def update(self):
    #     self.vel = 0
    #     self.speedy = 0
    #     prev_center = self.rect.center
    #     ctrlpress = pygame.key.get_pressed()
    #     if ctrlpress[pygame.K_UP] and self.rect.top > 10:
    #          self.speed = vec(self.vel, 0).rotate(-self.rot)
    #     if ctrlpress[pygame.K_DOWN] and self.rect.bottom < sHeight:
    #         if self.rot > 0:
    #             self.rect.x += self.rot
    #             self.rect.y += self.rot
    #         else:
    #             self.rect.x -= self.rot
    #             self.rect.y -= self.rot
    #     if ctrlpress[pygame.K_LEFT]:
    #         self.rot = (self.rot + self.rotspeed) % 360
    #         new_image = pygame.transform.rotate(self.image_qua, self.rot)
    #         ocenter = self.rect.center
    #         self.image = new_image
    #         self.rect = self.image.get_rect()
    #         self.rect.center = ocenter
    #     if ctrlpress[pygame.K_RIGHT]:
    #         self.rot = (self.rot - self.rotspeed) % 360
    #         new_image = pygame.transform.rotate(self.image_qua, self.rot)
    #         ocenter = self.rect.center
    #         self.image = new_image
    #         self.rect = self.image.get_rect()
    #         self.rect.center = ocenter
    #     self.rect.y += self.speedy
    #     self.rect.x += self.vel
    #     if self.rect.right > sWidth:
    #         self.rect.right = sWidth
    #     if self.rect.left < 0:
    #         self.rect.left = 0

    def shoot(self):
        bullet = Projectile.projectile(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

