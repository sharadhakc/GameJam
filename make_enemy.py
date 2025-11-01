from enemy import Enemy

def make_enemy(start, num_enemy, level, sprite,size):

    enemy = []
    for e in range(num_enemy):

        x_position = start[0] + (e*150)
        if x_position > 0 and x_position+ size[0] < 1200:
            enemy.append(Enemy(health=2, damage=2, position=[x_position, start[1]], speed=(0.2 * level), level=level, sprite=sprite, size=size))

    return enemy
        