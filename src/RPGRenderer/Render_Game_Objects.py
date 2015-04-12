import pygame
from RPGElements.RPGObjects.RPG_Character import RPGCharacter

# Define coordinate indices to avoid magic numbers
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = ( 0  ,   0, 255)
class GameObjectRenderer(object):


    def __init__(self):
        pass
    
    # renders the entire map view and all objects on the map
    def render_map(self,screen, gameObjects):          
        # First, clear the screen to WHITE. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        for game_object in gameObjects:
            self.render_game_object(screen, game_object)        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        
    # takes in a screen, game_object, and utilizes game_object's position to draw on screen
    def render_game_object(self, screen, game_object):
        if isinstance(game_object, RPGCharacter):
            x = game_object.coordinates[X_COOR_INDEX]
            y = game_object.coordinates[Y_COOR_INDEX]
            # Head
            pygame.draw.rect(screen, BLACK, [x, y, game_object.hitbox[0], game_object.hitbox[1]], 0)
            """pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
          
            # Legs
            pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
            pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
          
            # Body
            pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
          
            # Arms
            pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
            pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)"""
            pygame.draw.rect(screen, GREEN, [0,0,game_object.current_hp,10], 0)
            pygame.draw.rect(screen, RED, [game_object.current_hp,0,game_object.max_hp - game_object.current_hp,10], 0)
            
        else:
            x = game_object.coordinates[X_COOR_INDEX]
            y = game_object.coordinates[Y_COOR_INDEX]
            # building
            pygame.draw.rect(screen, BLUE, [x, y, game_object.hitbox[0], game_object.hitbox[1]], 0)

        
        
        
        