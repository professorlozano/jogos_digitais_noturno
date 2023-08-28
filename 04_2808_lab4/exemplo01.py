import pygame
from pygame.locals import * 
from sys import exit

background_image_filename = 'mar.jpeg'
sprite_image_filename = 'peixe.png'

pygame.init ()
screen = pygame.display. set_mode ((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame. image.load(sprite_image_filename)

x = 0
while True:
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit()
            exit ()

    screen.blit(background,(0,0)) 
    screen.blit(sprite,(x,100))
    x += 1
   
    if x > 640:
        x -= 640
    pygame.display.update ()


    