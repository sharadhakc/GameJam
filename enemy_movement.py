import pygame
import sys

from enemy import Enemy
from make_enemy import enemy_enemy

pygame.init() #start up pygame

screenWidth=1200
screenHeight=800

screen= pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("SHOOTER")

running=True


enemy1 = pygame.image.load("Assets/alien1.png")

enemy_size=[100,100]

enemy1 = pygame.transform.scale(enemy1,(enemy_size[0],enemy_size[1]))

enemyPos= [100,100]

movement=[False, False]
speed=0.2

e1= Enemy(health=2, damage=2, position= enemyPos, speed=speed, sprite=enemy1, level=1)


while running:

    enemyPos[1]= enemyPos[1]+ speed

    for event in pygame.event.get():
        if event.type== pygame.QUIT: # if they click on X it exits the screen
            running=False

    screen.fill((0,0,0))


    screen.blit(enemy1,(enemyPos[0],enemyPos[1]))

    pygame.display.flip()
