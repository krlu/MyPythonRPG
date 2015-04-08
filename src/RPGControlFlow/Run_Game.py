import pygame
from RPGElements.RPGObjects.Building import RPGBuilding
from RPGElements.RPGObjects.RPG_Character import RPGCharacter
from RPGRenderer.Render_Game_Objects import GameObjectRenderer
from RPGControlFlow.Input_Handler import UserInputHandler
from RPGControlFlow.Event_Handler import EventHandler

NORM_FONT = ("Helvetica", 10)
# Define coordinate indices to avoid magic numbers
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

def run_game():    
    # Setup
    pygame.init()
    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)
      
    pygame.display.set_caption("My Game")
      
    #Loop until the user clicks the close button.
    done = False
      
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    # Don't hide the mouse cursor
    pygame.mouse.set_visible(1)
     
    # Speed in pixels per frame
    # Represents character's initial vector
    move_speed = 3
    
    # Current position of main character
    x_coord = 10
    y_coord = 10 
    
    #Create game objects (buildings, terrain, main charcters, NPCS) 
    #TODO: very hacky stuff in memory, needs to persist in database! 

    gameObjects = []
    character = RPGCharacter([x_coord, y_coord],move_speed)
    building = RPGBuilding([x_coord + 100, y_coord + 100])
    gameObjects.append(character)
    gameObjects.append(building)
    
    #create handler objects to manage different portions of the game
    userInputHandler = UserInputHandler()
    eventHandler = EventHandler()
    renderer = GameObjectRenderer()
    
    # -------- Main Program Loop -----------
    while not done:
        
        done = userInputHandler.handle_movement_key_input(character, done)
        
        eventHandler.handle_game_events(character)
     
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT :   
        renderer.render_map(screen, gameObjects)      
        # Limit to 20 frames per second
        clock.tick(60)
          
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
     
 
run_game()