from In_Game_Messages import MessagesInGame
from RPGElements.RPGObjects.RPG_Character import RPGCharacter
from RPGGameLogic.Collision_Handler import CollisionHandler

# Define coordinate indices to avoid magic numbers
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

# ALL GAME LOGIC GOES IN THIS CLASS (and potential sub-classes)
# Handles all interactions between game objects
# Interactions include character movement, object collisions
# Ability interactions, player to NPC interaction, etc
class EventHandler(object):

    def __init__(self, game_objects,game_map):
        self.game_objects = game_objects
        self.collision_handler = CollisionHandler(game_objects,game_map)
    
    # Handles movement of main character after 
    def handle_game_events(self):
        for game_object in self.game_objects:
            if isinstance(game_object, RPGCharacter):
                self.handle_character_movement(game_object)
    
    def handle_character_movement(self,character):        
        if character.current_hp == 0:
            mig = MessagesInGame()
            mig.death_msg("You just lost the game, play again?")
            
        # Check for collisions (this is a separate class)
        # Move the object according to the speed vector.
        if self.collision_handler.no_collisions_with_character(character): 
            character.move_x()
            character.move_y()
        else:
            character.current_hp -= 1
            print("collision!!")
            
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
