import pygame
class Player:

    def __init__(self, health, bul_sp, bul_count, defence, position,size, sprite):
        self.max_health = health
        self.health=health
        self.bul_sp= bul_sp
        self.bul_count=bul_count
        
        self.defence= defence
        self.position= position # this is an array with index 0 as x and index 1 as y

        self.size= size

        self.sprite=pygame.transform.scale(sprite,(self.size[0],self.size[1]))


    
    def take_dmg (self, income_dmg): # function to see how much our health decreases
        damage= income_dmg - self.defence
        if damage<= 0: # checking if the damage is -ve 
            damage=0
        # print("Health=", self.health)
        self.health-= damage
        # print("New health=", self.health)
        # print("Damage taken=", damage)

    def heal(self, heal_amount ):
        self.health+= heal_amount

    def increase_speed( self, speed_up):
        self.bul_sp+= speed_up
    
    def increase_bul(self, bull_up):
        self.bul_count= (self.bul_count* bull_up)+ self.bul_count

    def decrease_bul (self):
        self.bul_count= self.bul_count- 2

    def move_position(self,x):
        self.position[0]+=x

    

    


     
    
            
    

    
