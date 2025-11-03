import pygame
import asyncio
import random
import sys
import time
from game.screen import screenHeight, screenWidth, background, title_screen, text_color, font 
from game.enemy import Enemy 
from game.make import make_enemy, make_bullets 
from game.player import Player

pygame.init() #start up pygame


screen = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("SHOOTER")

clock = pygame.time.Clock()
FPS = 480

running=True

current_score = 0
highest_score = 0
score_text = font.render(f"Score: {current_score}", True, text_color)

state = {
    "title": True,
    "game": False,
}


sprite = {
    1: pygame.image.load("Assets/alien1.png"),
    2: pygame.image.load("Assets/alien2.png"),
    3: pygame.image.load("Assets/alien3.png"),
    "upgrade": pygame.image.load("Assets/upgrade.png")
}

blast_sprite = pygame.image.load("Assets/blast.png")

# Enemy Section ------------------------------------------------------------------------------

enemy_size=[75,75]
enemy_pos= [100,100]
speed=0.2
enemy_array = []
enemy_cooldown = 150
enemy_counter = 0
# Enemy Section ------------------------------------------------------------------------------

#player section------------------------------------------------------------------------------
player_sprite= pygame.image.load("Assets/player.png")
player_size= [100,100]
player_pos = [550, 680]
speed= 0.5 * 4
player= Player(health=15, bul_sp=speed, bul_count=1, defence= 0.5, position= player_pos, size= player_size, sprite= player_sprite)
dx = 0
#player section------------------------------------------------------------------------------


# blast section------------------------------------------------------------------------------
blast_array = []
cooldown = 50
counter = 0
# blast section------------------------------------------------------------------------------




def enemy_passed(enemy_array, player):

    enemy_to_remove = []
    for e in enemy_array:

        if (e.position[1] + e.size[1]) >= screenHeight:

            if e not in enemy_to_remove:
                enemy_to_remove.append(e)
    
                player.take_dmg(e.damage)

    
    for e in enemy_to_remove:
        enemy_array.remove(e)



def check_blast_enemy_collision(blast_array, enemy_array):
    """Check if any blast hits any enemy and handle damage"""
    blasts_to_remove = []
    enemies_to_remove = []
    score = 0
    
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
                        score += 10
    
    # Remove dead entities
    for blast in blasts_to_remove:
        blast_array.remove(blast)
    for enemy in enemies_to_remove:
        enemy_array.remove(enemy)
    
    return score



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

    start = random.randint(200, 1000) # x - position
    level = random.randint(1,3)
    num_enemy = 0

    if level > 2:
        num_enemy = random.randint(1, 2)
    else:
        num_enemy = random.randint(1, 3)


    make_enemy(enemy_array=enemy_array, start=[start,pos[1]], num_enemy=num_enemy, level=level, sprite=sprite[level], size=size)


def render_screen(screen, screen_elements):
    for key, value in screen_elements.items():

        if key == "background":
            screen.blit(value, (0, 0))

        elif key == "text":
            screen.blit(value, (screenWidth//2 - 100, 100))

        elif key == "score":            
            screen.blit(value, (screenWidth - 400, 10))  # Top right

        elif key == "start":
            screen.blit(value, (screenWidth//2 - 100, screenHeight//2))

def render_health(player, screen):
    bar_width = 300

    red_bar = pygame.Rect(0, 10, bar_width, 50)
    green_bar = pygame.Rect(0, 10, (player.health/player.max_health) * bar_width, 50)

    pygame.draw.rect(screen, (255, 0, 0), red_bar)
    pygame.draw.rect(screen, (0, 255, 0), green_bar)




async def main(running,
    state,
    player,
    enemy_array,
    blast_array,
    title_screen,
    clock,
    FPS,
    screen,
    background,
    font,
    text_color,
    screenWidth,
    screenHeight,
    blast_sprite,
    enemy_size,
    enemy_pos,
    enemy_cooldown,
    enemy_counter,
    counter,
    cooldown,
    current_score,
    highest_score, dx, sprite):
    while running:

        print(state)

        # Makes speed of the game consistent 
        clock.tick(FPS)


        if state["title"]:
            render_screen(screen=screen, screen_elements=title_screen)

    


        player.move_position(dx)


        for event in pygame.event.get():
            if event.type== pygame.QUIT: # if they click on X it exits the screen
                running=False


            if event.type == pygame.MOUSEBUTTONDOWN:
                if title_screen["button_rect"].collidepoint(event.pos):
                    state["title"] = False
                    state["game"] = True



            keys = pygame.key.get_pressed()
            dx = 0  # Reset movement each frame
            
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                dx = -1.5 * 3
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                dx = 1.5 * 3
        
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



            score = check_blast_enemy_collision(blast_array, enemy_array)
            current_score += score
            score_text = font.render(f"Score: {current_score}", True, text_color)

            screen.blit(score_text, (screenWidth - 250, 10))  # Top right
            is_alive = check_enemy_player_collision(enemy_array, player)

            enemy_passed(enemy_array=enemy_array, player=player)


            if enemy_counter == 0:
                enemy_counter = enemy_cooldown
                enemy_cooldown = random.randint(200, 300)
                spawn_random_enemy(size=enemy_size, pos=enemy_pos)
            
            else:
                enemy_counter -= 1

            if not is_alive:
                print("Game Over")
                state["game"] = False
                state["title"] = True

                highest_score = max(highest_score, current_score)
                current_score = 0
                title_screen["score"] = font.render(f"Highest score: {highest_score}", True, text_color)

                player.health = player.max_health
                enemy_array.clear()
                blast_array.clear()


            if counter == 0:
                counter = cooldown
                blast_array = make_bullets(blast_array= blast_array,num_blast=player.bul_count, sprite=blast_sprite, player_pos=player.position, speed=player.bul_sp, player_size=player_size, bullet_size=[30,40])
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
        await asyncio.sleep(0)


asyncio.run(main(running,
    state,
    player,
    enemy_array,
    blast_array,
    title_screen,
    clock,
    FPS,
    screen,
    background,
    font,
    text_color,
    screenWidth,
    screenHeight,
    blast_sprite,
    enemy_size,
    enemy_pos,
    enemy_cooldown,
    enemy_counter,
    counter,
    cooldown,
    current_score,
    highest_score, dx, sprite))
