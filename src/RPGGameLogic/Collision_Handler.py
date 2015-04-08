# Define coordinate indices to avoid magic numbers
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

class CollisionHandler(object):

    def __init__(self, game_objects, game_map):
        self.game_objects = game_objects
        self.game_map = game_map
        
    def no_collisions_with_character(self, character):
        if not self.at_edge_of_map(character):
            return False
        else:
            return True
    
    #check if character is at edge of map
    def at_edge_of_map(self, character):
        return (character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX] in range(0,700) and 
                character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX]  in range(0,500))
    
    
    # if the map is bigger than what's shown on screen
    # we re-render the new section of the map that the player has entered
    # TODO: needs implementing!!
    def handle_edge_of_map_(self):
        print("TO BE IMPLEMENTED")
        