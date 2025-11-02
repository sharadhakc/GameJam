from .enemy import Enemy
from .blast import Blast

def make_enemy(enemy_array, start, num_enemy, level, sprite,size):

    
    for e in range(num_enemy):

        x_position = start[0] + (e*150)
        if x_position > 0 and x_position+ size[0] < 1200:
            enemy_array.append(Enemy(health=2*level*0.5, damage=level, position=[x_position, start[1]], speed=(0.2 * level), level=level, sprite=sprite, size=size))

    return enemy_array



def make_bullets(blast_array, num_blast, sprite, player_size, player_pos,bullet_size, speed ):
    

    for b in range(num_blast):

        x_position = player_pos[0] + player_size[0]/2


        blast_array.append(Blast(damage=2, position=[x_position, player_pos[1] + 10], speed=speed, sprite=sprite, size=bullet_size))

    return blast_array







        