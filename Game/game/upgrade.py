import pygame

class Upgrade:
    def __init__(self, amount, position, size, sprite):

        self.amount = amount
        self.position = position
        self.size = size
        
        self.sprite = pygame.transform.scale(sprite,(self.size[0],self.size[1]))


    