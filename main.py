import pygame

pygame.init() #start up pygame

screenWidth=800
screenHeight=500

screen= pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("SHOOTER")

running=True

while running:

    for event in pygame.event.get():
        pass

    screen.fill((2,3,5))

    pygame.display.flip()





