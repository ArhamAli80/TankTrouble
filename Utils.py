import pygame

def gametext (surf, text, size, x, y, font=None):
    font = pygame.font.Font(font,size)
    textsurface = font.render(text,True,(0,0,0))
    text_rect = textsurface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(textsurface,text_rect)

def blit_rotate_center(screen,image,top_left,angle):
   rotated_image = pygame.transform.rotate(image,angle)
   new_rect=rotated_image.get_rect(center = image.get_rect(topleft=top_left).center)
   screen.blit(rotated_image,new_rect.topleft)