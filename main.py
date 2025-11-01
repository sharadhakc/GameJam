import pygame
import sys

from enemy import Enemy
from make import make_enemy, make_bullets
from player import Player

pygame.init() #start up pygame

screenWidth=1200
screenHeight=800

screen= pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("SHOOTER")

running=True

# Enemy Section ------------------------------------------------------------------------------
e1_sprite = pygame.image.load("Assets/alien2.png")
enemy_size=[100,100]
enemy_pos= [100,100]
speed=0.2
enemy1_array = make_enemy(start=enemy_pos, num_enemy=19, level=1, sprite=e1_sprite, size=enemy_size)
# Enemy Section ------------------------------------------------------------------------------

#player section------------------------------------------------------------------------------
player_sprite= pygame.image.load("Assets/player.png")
player_size= [100,100]
player_pos = [550, 600]
speed= 0.5
player= Player(health=5, bul_sp= speed, bul_count=50, defence= 3, position= player_pos, size= player_size, sprite= player_sprite )
dx = 0
#player section------------------------------------------------------------------------------


# blast section------------------------------------------------------------------------------

blast_sprite = pygame.image.load("Assets/blast.png")
blast_array = make_bullets(player.bul_count, sprite=blast_sprite, player_pos=player.position, speed=player.bul_sp, player_size=player_size, bullet_size=[15,15])
# blast section------------------------------------------------------------------------------



while running:


    player.move_position(dx)
    for event in pygame.event.get():
        if event.type== pygame.QUIT: # if they click on X it exits the screen
            running=False


        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT :
                dx = -1
            if event.key== pygame.K_d or event.key == pygame.K_RIGHT :
                dx = 1
        if event.type== pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                dx = 0
            if event.key== pygame.K_d or event.key == pygame.K_RIGHT :
                dx = 0

            


    screen.fill((0,0,0))

    for e in enemy1_array:
        screen.blit(e.sprite,(e.position[0],e.position[1]))
        e.change_position()
    
    for b in blast_array:

        screen.blit(b.sprite,(b.position[0],b.position[1]))
        b.move()
    
    screen.blit(player.sprite,(player.position[0],player.position[1]))



    pygame.display.flip()
