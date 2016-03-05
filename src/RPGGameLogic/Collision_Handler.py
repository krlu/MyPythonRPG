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
        if self.side1_intersection(p1, character):
            print("side1")
            return True
        elif self.side2_intersection(p1, character):
            print("side2")
            return True
        elif self.side3_intersection(p1, character):
            print("side3")
            return True
        elif self.side4_intersection(p1, character):
            print("side4")
            return True
        return False
    
    def generate_rectangle(self, game_object):
        x = game_object.coordinates[X_COOR_INDEX]
        y = game_object.coordinates[Y_COOR_INDEX]
        x_length = game_object.hitbox[0]
        y_length = game_object.hitbox[1]
        p1 = [x, y, x+x_length, y+y_length]
        return p1
    
    def side1_intersection(self,poly, character): 
        x_left = character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX]
        x_right = x_left + character.hitbox[X_COOR_INDEX]
        y_top = character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX]
        y_bot = y_top + character.hitbox[Y_COOR_INDEX] 
        if self.point_inside_polygon(poly, x_right, y_top):
            if(abs(x_right - poly[0]) < abs(y_top - poly[1]) and x_right - poly[0] > 0 and y_top - poly[1] > 0):                
                return True
        elif self.point_inside_polygon(poly, x_right, y_bot):
            if(abs(x_right - poly[0]) < abs(y_bot - poly[3]) and x_right - poly[0] > 0 and y_bot - poly[3] < 0):
                return True                                                 
        return False
    
    def side2_intersection(self,poly, character): 
        x_left = character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX]
        x_right = x_left + character.hitbox[X_COOR_INDEX]
        y_top = character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX]
        y_bot = y_top + character.hitbox[Y_COOR_INDEX] 
        if self.point_inside_polygon(poly, x_left, y_bot):
            if(x_left - poly[0] > y_bot - poly[1]):
                return True
        elif self.point_inside_polygon(poly, x_right, y_bot):
            if(x_right - poly[2] > y_bot - poly[1]):
                return True                                                 
        return False
    def side3_intersection(self,poly, character): 
        x_left = character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX]
        x_right = x_left + character.hitbox[X_COOR_INDEX]
        y_top = character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX]
        y_bot = y_top + character.hitbox[Y_COOR_INDEX] 
        if self.point_inside_polygon(poly, x_left, y_top):
            if(x_left - poly[2] < y_top - poly[1]):
                return True
        elif self.point_inside_polygon(poly, x_left, y_bot):
            if(x_left - poly[2] < y_bot - poly[3]):                
                return True                                                 
        return False
    def side4_intersection(self,poly, character): 
        x_left = character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX]
        x_right = x_left + character.hitbox[X_COOR_INDEX]
        y_top = character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX]
        y_bot = y_top + character.hitbox[Y_COOR_INDEX] 
        if self.point_inside_polygon(poly, x_left, y_top):
            if(x_left - poly[0] > y_top - poly[1]):               
                return True
        elif self.point_inside_polygon(poly, x_right, y_top):
            if(x_right - poly[2] > y_top - poly[1]):               
                return True                                                 
        return False
    
    def inbetween(self, x, a, b):
        return a < x and x < b   
    
    def point_inside_polygon(self,poly, x,y): 
        return self.inbetween(x, poly[0], poly[2]) and self.inbetween(y, poly[1], poly[3])









