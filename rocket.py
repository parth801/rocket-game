import pygame
from pygame.locals import *
from time import *
pygame.init()
screen = pygame.display.set_mode((600, 600))
object_x = 200
object_y = 200
keys = [False, False, False, False]
object = pygame.image.load("Rocket in space L5\rocket.png")
background = pygame.image.load("Rocket in space L5\background.png")
#pygame.display.update()

while object_y < 600:
    screen.blit(background, (0,0))
    screen.blit(object, (object_x, object_y))
    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_RIGHT:
                keys[3] = False
    
    if keys[0]:
        if object_y>0:
            object_y -= 7
    elif keys[2]:
        if object_y<540:
            object_y += 7
    if keys[1]:
        if object_x>0:
            object_x -= 3
    elif keys[3]:
        if object_x<540:
            object_x += 3
    
    object_y += 3
    sleep(0.05)

print("GAME OVER")
    #pygame.display.update()
