import pygame
from RPGElements.RPGObjects.RPGCharacter import RPGCharacter

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
        for gameObject in gameObjects:
            self.render_gameObject(screen, gameObject)        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        
    # takes in a screen, gameObject, and utilizes gameObject's position to draw on screen
    def render_gameObject(self, screen, gameObject):
        if isinstance(gameObject, RPGCharacter):
            x = gameObject.coordinates[X_COOR_INDEX]
            y = gameObject.coordinates[Y_COOR_INDEX]
            # Head
            pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
          
            # Legs
            pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
            pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
          
            # Body
            pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
          
            # Arms
            pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
            pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
            pygame.draw.rect(screen, GREEN, [0,0,gameObject.current_hp,10], 0)
            pygame.draw.rect(screen, RED, [gameObject.current_hp,0,gameObject.max_hp - gameObject.current_hp,10], 0)
            
        else:
            x = gameObject.coordinates[X_COOR_INDEX]
            y = gameObject.coordinates[Y_COOR_INDEX]
            # building
            pygame.draw.rect(screen, BLUE, [1 + x, y, 60, 60], 0)

        
        
        
        