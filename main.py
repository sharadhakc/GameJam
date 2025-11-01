import pygame
import sys

from enemy import Enemy
from make_enemy import make_enemy

pygame.init() #start up pygame

screenWidth=1200
screenHeight=800

screen= pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("SHOOTER")

running=True







enemy1 = pygame.image.load("Assets/alien1.png")

enemy_size=[100,100]

e1_sprite = pygame.transform.scale(enemy1,(enemy_size[0],enemy_size[1]))

enemyPos= [100,100]

movement=[False, False]
speed=0.2


enemy1_array = make_enemy(start=enemyPos, num_enemy=19, level=1, sprite=e1_sprite, size=enemy_size)
print(len(enemy1_array))


while running:


    for event in pygame.event.get():
        if event.type== pygame.QUIT: # if they click on X it exits the screen
            running=False

    screen.fill((0,0,0))



    
    for e in enemy1_array:
        screen.blit(e.sprite,(e.position[0],e.position[1]))
        e.change_position()


    pygame.display.flip()
