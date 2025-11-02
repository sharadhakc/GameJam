import pygame
import random
import sys
import time
from screen import screenHeight, screenWidth, background, title_screen, end_screen

from enemy import Enemy
from make import make_enemy, make_bullets
from player import Player

pygame.init() #start up pygame





screen = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("SHOOTER")

clock = pygame.time.Clock()
FPS = 480

running=True



state = {
    "title": True,
    "game": False,
    "end": False
}


# Enemy Section ------------------------------------------------------------------------------
sprite = {
    1: pygame.image.load("Assets/alien1.png"),
    2: pygame.image.load("Assets/alien2.png"),
    3: pygame.image.load("Assets/alien3.png")
}
enemy_size=[50,50]
enemy_pos= [100,100]
speed=0.2
enemy_array = []
enemy_cooldown = 1500
enemy_counter = 0
# Enemy Section ------------------------------------------------------------------------------

#player section------------------------------------------------------------------------------
player_sprite= pygame.image.load("Assets/player.png")
player_size= [100,100]
player_pos = [550, 600]
speed= 0.5
player= Player(health=5, bul_sp= speed, bul_count=1, defence= 3, position= player_pos, size= player_size, sprite= player_sprite)
dx = 0
#player section------------------------------------------------------------------------------


# blast section------------------------------------------------------------------------------
blast_array = []
blast_sprite = pygame.image.load("Assets/blast.png")
print(len(blast_array))
cooldown = 200
counter = 0
# blast section------------------------------------------------------------------------------







def check_blast_enemy_collision(blast_array, enemy_array):
    """Check if any blast hits any enemy and handle damage"""
    blasts_to_remove = []
    enemies_to_remove = []
    
    for blast in blast_array:
        blast_rect = pygame.Rect(blast.position[0], blast.position[1], 
                                  blast.size[0], blast.size[1])
        
        for enemy in enemy_array:
            enemy_rect = pygame.Rect(enemy.position[0], enemy.position[1],
                                     enemy.size[0], enemy.size[1])
            
            if blast_rect.colliderect(enemy_rect):
                # Handle collision
                enemy.decrease_health(blast.damage)
                if blast not in blasts_to_remove:
                    blasts_to_remove.append(blast)
                
                # Remove enemy if dead
                if enemy.health <= 0:
                    if enemy not in enemies_to_remove:
                        enemies_to_remove.append(enemy)
    
    # Remove dead entities
    for blast in blasts_to_remove:
        blast_array.remove(blast)
    for enemy in enemies_to_remove:
        enemy_array.remove(enemy)



def check_enemy_player_collision(enemy_array, player):
    """Check if any enemy collides with player"""
    player_rect = pygame.Rect(player.position[0], player.position[1],
                              player.size[0], player.size[1])
    
    enemies_to_remove = []
    
    for enemy in enemy_array:
        enemy_rect = pygame.Rect(enemy.position[0], enemy.position[1],
                                 enemy.size[0], enemy.size[1])
        
        if player_rect.colliderect(enemy_rect):
            # Player takes damage
            player.take_dmg(enemy.damage)
            enemies_to_remove.append(enemy)
    
    # Remove enemies that hit player
    for enemy in enemies_to_remove:
        enemy_array.remove(enemy)
    
    return player.health > 0  # Return False if player is dead

def spawn_random_enemy(size, pos):

    start = random.randint(0, 1200)
    num_enemy = random.randint(1, 4)
    level = random.randint(1,3)

    make_enemy(enemy_array=enemy_array, start=[start,pos[1]], num_enemy=num_enemy, level=level, sprite=sprite[level], size=size)


def render_screen(screen, screen_elements):
    for key, value in screen_elements.items():

        if key == "background":
            screen.blit(value, (0, 0))

        elif key == "text":
            screen.blit(value, (screenWidth//2, 100))

        else:
            screen.blit(value, (screenWidth//2, screenHeight//2))

def render_health(player, screen):
    bar_width = 300

    red_bar = pygame.Rect(0, 10, bar_width, 50)
    green_bar = pygame.Rect(0, 10, (player.health/player.max_health) * bar_width, 50)

    pygame.draw.rect(screen, (255, 0, 0), red_bar)
    pygame.draw.rect(screen, (0, 255, 0), green_bar)




while running:

    # Makes speed of the game consistent 
    clock.tick(FPS)


    if state["title"]:
        render_screen(screen=screen, screen_elements=title_screen)

    elif state["end"]:
        render_screen(screen=screen, screen_elements=end_screen)


    


    player.move_position(dx)


    for event in pygame.event.get():
        if event.type== pygame.QUIT: # if they click on X it exits the screen
            running=False


        keys = pygame.key.get_pressed()
        dx = 0  # Reset movement each frame
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1.5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1.5
    
        # if event.type== pygame.KEYDOWN:
        #     if event.key == pygame.K_a or event.key == pygame.K_LEFT :
        #         dx = -1.5
        #     if event.key== pygame.K_d or event.key == pygame.K_RIGHT :
        #         dx = 1.5

        # if event.type== pygame.KEYUP:
        #     if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        #         dx = 0
        #     if event.key== pygame.K_d or event.key == pygame.K_RIGHT :
        #         dx = 0

    
    if state["game"]:

        screen.blit(background, (0,0))
        render_health(player, screen)



        check_blast_enemy_collision(blast_array, enemy_array)
        is_alive = check_enemy_player_collision(enemy_array, player)


        if enemy_counter == 0:
            enemy_counter = enemy_cooldown
            enemy_cooldown = random.randint(1000, 1500)
            spawn_random_enemy(size=enemy_size, pos=enemy_pos)
        
        else:
            enemy_counter -= 1

        if not is_alive:
            print("Game Over")
            running = False


        if counter == 0:
            counter = cooldown
            blast_array = make_bullets(blast_array= blast_array,num_blast=player.bul_count, sprite=blast_sprite, player_pos=player.position, speed=player.bul_sp, player_size=player_size, bullet_size=[15,15])
        else:
            counter -= 1


        for e in enemy_array:
            screen.blit(e.sprite,(e.position[0],e.position[1]))
            e.change_position()
        
        for b in blast_array:

            screen.blit(b.sprite,(b.position[0],b.position[1]))
            b.move()
    
        screen.blit(player.sprite,(player.position[0],player.position[1]))



    pygame.display.flip()
