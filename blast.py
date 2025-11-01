import pygame

class Blast:
    
    def __init__(self, damage, position, speed,sprite,size=[15,15]):

        self.damage = damage
        self.position = position
        self.speed = speed 

        self.size = size
        self.sprite = pygame.transform.scale(sprite,(self.size[0],self.size[1]))
    

    def move(self):
        self.position[1]-= self.speed


