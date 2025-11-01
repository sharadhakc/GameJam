import pygame

pygame.init() #start up pygame

screenWidth=1200
screenHeight=800

screen= pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("SHOOTER")

running=True

while running:

    for event in pygame.event.get():
        if event.type== pygame.QUIT: # if they click on X it exits the screen
            running=False

    screen.fill((2,3,5))

    pygame.display.flip()





