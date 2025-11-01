class Enemy:
    def __init__(self, health, damage, position, speed,sprite, level):
        self.health= health
        self.damage= damage
        self.position= position
        self.speed= speed
        self.sprite= sprite
        self.level = level

    def decrease_health(self,incoming_damage):
        self.health-= incoming_damage 

    def change_position(self):
        self.position[1]-= (self.speed * self.level)

    

    

    