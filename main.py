from os import path
import pygame
from pygame import MOUSEBUTTONDOWN

img = path.join(path.dirname("__file__"),'ImageList')

#initialise window
pygame.init()
sHeight = 800
sWidth = 1000
screen = pygame.display.set_mode((sWidth,sHeight))

#defining colours used in the game
red = (255,0,0)
torqouise = (89,147,222)
green = (181,213,205)
black = (0,0,0)
white = (255,255,255)

pygame.display.set_caption("Tank Trouble")
font = pygame.font.match_font('arial')

def gametext (surf, text, size, x, y, font=None):
    font = pygame.font.Font(font,size)
    textsurface = font.render(text,True,black)
    text_rect = textsurface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(textsurface,text_rect)

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(tankSprite,(64,64))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.radius = 19
        self.rect.centerx = (sWidth/2)
        self.rect.bottom = (sHeight/2)
        self.vel = 0
        self.speedy = 0

    def update(self):
        self.vel = 0
        self.speedy = 0
        ctrlpress = pygame.key.get_pressed()
        if ctrlpress[pygame.K_UP] and self.rect.top > 10:
            self.speedy = -10
        if ctrlpress[pygame.K_DOWN] and self.rect.bottom < sHeight:
            self.speedy = 10
        if ctrlpress[pygame.K_LEFT]:
            self.vel = -10
        if ctrlpress[pygame.K_RIGHT]:
            self.vel = 10
        self.rect.y += self.speedy
        self.rect.x += self.vel
        if self.rect.right > sWidth:
            self.rect.right = sWidth
        if self.rect.left < 0:
            self.rect.left = 0

tankSprite = pygame.image.load(path.join(img,"TankSprite.png")).convert()

all_sprites = pygame.sprite.Group()
player = player()

all_sprites.add(player)

clock = pygame.time.Clock()

click = False

def game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def menu():
    run = True
    while run:

        screen.fill((255,255,255))
        gametext(screen,str('Main Menu'),80,sWidth/2,250)

        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(50,100,200,50)
        button2 = pygame.Rect(50,200,200,50)
        if button1.collidepoint((mx,my)):
            if click:
                pass
        if button2.collidepoint((mx,my)):
            if click:
                pass
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        all_sprites.update()
        clock.tick(25)
        all_sprites.draw(screen)
        pygame.display.flip()

menu()

pygame.quit()
