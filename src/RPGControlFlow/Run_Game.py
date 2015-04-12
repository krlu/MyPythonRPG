import pygame

from RPGControlFlow.Event_Handler import EventHandler
from RPGControlFlow.Input_Handler import UserInputHandler
from RPGElements.RPGObjects.Building import RPGBuilding
from RPGElements.RPGObjects.RPG_Character import RPGCharacter
from RPGElements.RPGUniverse.Map import GameMap
from RPGRenderer.Render_Game_Objects import GameObjectRenderer


def run_game():    
    # Setup
    pygame.init()
    
    # Load Map object, currently loads in memory
    # TODO: should load from database!!
    # Set the width and height of the screen [width,height]
    
    game_map = GameMap([1400,1000])
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
    
    # Current position of building
    building_x = x_coord + 100
    building_y = y_coord + 100
    
    #Create game objects (buildings, terrain, main characters, NPCS) 
    #TODO: very hacky stuff in memory, needs to persist in database! 
    gameObjects = []
    character = RPGCharacter([x_coord, y_coord],[25,25], move_speed)
    building = RPGBuilding([building_x, building_y], [60,60])
    gameObjects.append(character)
    gameObjects.append(building)
    
    #create handler objects to manage different portions of the game
    userInputHandler = UserInputHandler()
    eventHandler = EventHandler(gameObjects, game_map)
    renderer = GameObjectRenderer()
    
    # -------- Main Program Loop -----------
    while not done:
        done = userInputHandler.handle_movement_key_input(character, done)
        
        eventHandler.handle_game_events()

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT :   
        renderer.render_map(screen, gameObjects)      
        # Limit to 20 frames per second
        clock.tick(60)
          
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
     
run_game()



