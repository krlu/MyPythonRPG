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
        x_left = character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX]
        x_right = x_left + character.hitbox[X_COOR_INDEX]
        y_top = character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX]
        y_bot = y_top + character.hitbox[Y_COOR_INDEX]
        if x_left < 0:
            character.coordinates[X_COOR_INDEX] = 0
            return True
        elif x_right > 700:
            character.coordinates[X_COOR_INDEX] = 700 - character.hitbox[0]
        elif y_top < 0:
            character.coordinates[Y_COOR_INDEX] = 0
            return True
        elif y_bot > 500:
            character.coordinates[Y_COOR_INDEX] = 500 - character.hitbox[1]
            return True
        return False
    # if the map is bigger than what's shown on screen
    # we re-render the new section of the map that the player has entered
    # TODO: needs implementing!!
    def handle_edge_of_map_(self):
        print("TO BE IMPLEMENTED")
        
    
    # utilize shapely API to perform collision detection
    def rectangle_collision(self, character, game_object):
        p1 = self.generate_rectangle(game_object)
        p2 = self.generate_rectangle(character)
        vertices = [(p2[0],p2[1]),(p2[2],p2[1]),(p2[0],p2[3]),(p2[2],p2[3])]
        #for vertex in p1:
        #   if self.point_inside_polygon(vertex[X_COOR_INDEX], vertex[Y_COOR_INDEX], p2):
        #        return True
        for vertex in vertices:
            print(character.coordinates)
            if self.point_inside_polygon(vertex[X_COOR_INDEX], vertex[Y_COOR_INDEX], p1, character):          
                return True
        return False
    
    def generate_rectangle(self, game_object):
        x = game_object.coordinates[X_COOR_INDEX]
        y = game_object.coordinates[Y_COOR_INDEX]
        x_length = game_object.hitbox[0]
        y_length = game_object.hitbox[1]
        p1 = [x, y, x+x_length, y+y_length]
        return p1
    # determine if a point is inside a given polygon or not
    # Polygon is a list of (x,y) pairs.
    
    def point_inside_polygon(self, x, y, poly, character):  
        if x + character.hitbox[0]> poly[0] and y > poly[1] and y< poly[3] and poly[2] - x > x - poly[0]:
            print("Collision1!!")
            character.coordinates[0] = poly[0]
            return True
        elif x == poly[2] and y > poly[1] and y< poly[3] and poly[2] - x < x - poly[0]:
            print("Collision3!!")
            character.coordinates[0] = x 
            return True
        elif y == poly[1] and x > poly[0] and x < poly[2]:
            print("Collision2!!")
            character.coordinates[1] = y - character.hitbox[1] - 0.1
            return True
        elif y == poly[3] and x > poly[0] and x < poly[2]:
            print("Collision4!!")
            character.coordinates[1] = y + 0.1
            return True
        return False
    
    
    
    
