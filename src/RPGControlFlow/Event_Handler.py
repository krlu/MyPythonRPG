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

    def __init__(self, game_objects):
        self.game_objects = game_objects
        
    
    # Handles movement of main character after 
    def handle_game_events(self):
        for game_object in self.game_objects:
            if isinstance(game_object, RPGCharacter):
                self.handle_character_movement(game_object)
    
    def handle_character_movement(self,character):
        
        if character.current_hp == 0:
            mig = MessagesInGame()
            mig.death_msg("You just lost the game, play again?")
        # Move the object according to the speed vector.
        collisionHandler = CollisionHandler()
        if collisionHandler.no_collisions(character): 
            character.move_x()
            character.move_y()
        else:
            character.current_hp -= 1
            print("collision!!")
    
    
            
                
