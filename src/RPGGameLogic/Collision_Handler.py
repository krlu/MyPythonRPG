# Define coordinate indices to avoid magic numbers
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

class CollisionHandler(object):

    def __init__(self):
        pass         
        # checks for any collisions with edge of map as well as objects
        def no_collisionss():
            pass
        
        def no_collisions(self, character):
            if not self.at_edge_of_map(character):
                return True
            else:
                return False
        
        def at_edge_of_map(self, character):
            return (character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX] in range(0,700) and 
                    character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX]  in range(0,500))
        