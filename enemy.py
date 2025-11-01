class Enemy:
    def __init__(self, health, damage, position, speed):
        self.health= health
        self.damage= damage
        self.position= position
        self.speed= speed

    def decrease_health(self,incoming_damage):
        self.health-= incoming_damage 

    def change_position(self,level):
        self.position[1]-= (self.speed * level)

    

    