import pygame
from os import path
import math
import time
import Player
from Utils import gametext
from pygame import MOUSEBUTTONDOWN, K_ESCAPE, KEYDOWN

img = path.join(path.dirname("__file__"),'ImageList')
imgdirectory = path.join(path.dirname("__file__"),'img')

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
grey = (0,0,100)
blue = (0,255,0)
white = (255,255,255)

pygame.display.set_caption("Tank Trouble")
font = pygame.font.match_font('arial')

WALLS = pygame.image.load(path.join(img,"LevelOne.png")).convert()

def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()

images = [(WALLS, (0, 0))]
player = Player.Player(10,10)


clock = pygame.time.Clock()

click = False

def game():
    run = True
    while run:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                if event.key == K_ESCAPE:
                    run = False

        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_a]:
            player.rotate(left=True)
        if keys[pygame.K_d]:
            player.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            player.move_forward()

        if not moved:
            player.reduce_speed()

        draw(screen,images,player)
        clock.tick(25)
        pygame.display.flip()

click = False
def menu():
    clock.tick(60)
    run = True
    while run:

        screen.fill((255,255,255))

        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(sWidth/2,330,200,50)
        button2 = pygame.Rect(sWidth/2,380,200,50)

        if button1.collidepoint((mx,my)):
            screen.fill((255, 255, 255))
            gametext(screen, str('Play'), 85, sWidth / 2, 330)
            gametext(screen, str('Exit'), 65, sWidth / 2, 400)
            if click:
                game()

        elif button2.collidepoint((mx,my)):
            screen.fill((255, 255, 255))
            gametext(screen, str('Exit'), 85, sWidth / 2, 400)
            gametext(screen, str('Play'), 65, sWidth / 2, 330)
            if click:
                pygame.quit()
        else:
            gametext(screen, str('Exit'), 65, sWidth / 2, 400)
            gametext(screen, str('Play'), 65, sWidth / 2, 330)

        gametext(screen, str('Main Menu'), 80, sWidth / 2, 250)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()



menu()

pygame.quit()
