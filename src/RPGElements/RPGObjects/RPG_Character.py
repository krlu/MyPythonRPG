from RPGElements.RPGObjects.Game_Object import GameObject
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

class RPGCharacter(GameObject):
    
    def __init__(self, coordinates, move_speed):
        super().__init__(coordinates)
        self.move_speed = move_speed
        self.speed_vector = [0, 0]
        self.max_hp = 100
        self.current_hp = 100
    
    # move in the X-direction given speed vector 
    def move_x(self):
        self.coordinates[X_COOR_INDEX] = self.coordinates[X_COOR_INDEX] + self.speed_vector[X_COOR_INDEX]
        
    # move in the Y-direction given speed vector
    def move_y(self):
        self.coordinates[Y_COOR_INDEX] = self.coordinates[Y_COOR_INDEX] + self.speed_vector[Y_COOR_INDEX]

        