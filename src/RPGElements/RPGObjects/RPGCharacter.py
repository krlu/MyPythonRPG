from RPGElements.RPGObjects.GameObject import GameObject
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

class RPGCharacter(GameObject):
    
    def __init__(self, coordinates, speed_vector):
        self.coordinates = coordinates
        self.speed_vector = speed_vector
        self.max_hp = 100
        self.current_hp = 100
    
    def move_x(self):
        self.coordinates[X_COOR_INDEX] = self.coordinates[X_COOR_INDEX] + self.speed_vector[X_COOR_INDEX]
    
    def move_y(self):
        self.coordinates[Y_COOR_INDEX] = self.coordinates[Y_COOR_INDEX] + self.speed_vector[Y_COOR_INDEX]

        