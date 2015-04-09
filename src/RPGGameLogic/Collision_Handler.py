from shapely.geometry import Polygon

from RPGElements.RPGObjects.RPG_Character import RPGCharacter


# Define coordinate indices to avoid magic numbers
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1


class CollisionHandler(object):

    def __init__(self, game_objects, game_map):
        self.game_objects = game_objects
        self.game_map = game_map
        
    def no_collisions_with_character(self, character):
        if self.at_edge_of_map(character):
            return False
        for game_object in self.game_objects:
            if not isinstance(game_object, RPGCharacter) and self.rectangle_collision(character, game_object):
                return False
        return True
        
    
    #check if character is at edge of map
    def at_edge_of_map(self, character):
        return (character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX] not in range(0,700) or
                character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX] not in range(0,500))
    
    
    # if the map is bigger than what's shown on screen
    # we re-render the new section of the map that the player has entered
    # TODO: needs implementing!!
    def handle_edge_of_map_(self):
        print("TO BE IMPLEMENTED")
        
    
    # utilize shapely API to perform collision detection
    def rectangle_collision(self, character, game_object):
        p1 = self.generate_rectangle(game_object)
        p2 = self.generate_rectangle(character)
        return p1.intersects(p2)
    
    def generate_rectangle(self, game_object):
        x = game_object.coordinates[X_COOR_INDEX]
        y = game_object.coordinates[Y_COOR_INDEX]
        if isinstance(game_object, RPGCharacter):
            x += game_object.speed_vector[X_COOR_INDEX]
            y += game_object.speed_vector[Y_COOR_INDEX]

        x_length = game_object.hitbox[0]
        y_length = game_object.hitbox[1]
        p1 = Polygon([(x,y),(x + x_length, y),(x , y + y_length), (x + x_length, y + y_length)])
        return p1
    
    
    
