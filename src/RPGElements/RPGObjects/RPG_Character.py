from RPGElements.RPGObjects.Game_Object import GameObject
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

class RPGCharacter(GameObject):
    
    def __init__(self, coordinates, hitbox, move_speed):
        super().__init__(coordinates, hitbox)
        self.move_speed = move_speed
        self.speed_vector = [0, 0]
        self.max_hp = 100
        self.current_hp = 100
    
    # move in the X-direction given speed vector 
    def move(self):
        self.coordinates[X_COOR_INDEX] += self.speed_vector[X_COOR_INDEX]
        self.coordinates[Y_COOR_INDEX] += self.speed_vector[Y_COOR_INDEX]


    def update_coordinates(self):
        self.coordinates[X_COOR_INDEX] = 200
        self.coordinates[Y_COOR_INDEX] = 200