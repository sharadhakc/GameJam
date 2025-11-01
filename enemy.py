import pygame
class Enemy:
    def __init__(self, health, damage, position, speed,sprite, level,size):
       
        self.health= health
        self.damage= damage
        self.position= position

        self.speed= speed
        self.level = level

        self.size=size
        self.sprite= pygame.transform.scale(sprite,(self.size[0],self.size[1]))

    def decrease_health(self,incoming_damage):
        self.health-= incoming_damage 

    def change_position(self):
        self.position[1]+= (self.speed * self.level)

    

    

    