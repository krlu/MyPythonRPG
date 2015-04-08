from test.test_idle import tk
from tkinter import ttk
import pygame
from RPGElements.RPGObjects.Building import RPGBuilding
from RPGElements.RPGObjects.RPGCharacter import RPGCharacter
from RPGRenderer.RenderGameObjects import GameObjectRenderer
from RPGUtils import Utility


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
     
    # Hide the mouse cursor
    pygame.mouse.set_visible(1)
     
    # Speed in pixels per frame
    # Represents character's initial vector
    x_speed = 0
    y_speed = 0
    #TODO: very hacky stuff in memory, needs to persist in database! 
    # Current position 
    x_coord = 10
    y_coord = 10 
    gameObjects = []
    character = RPGCharacter([x_coord, y_coord],[x_speed, y_speed])
    building = RPGBuilding([x_coord + 100, y_coord + 100])
    gameObjects.append(character)
    gameObjects.append(building)
    #uses game renderer to create objects on screen
    renderer = GameObjectRenderer()
    # -------- Main Program Loop -----------
    while not done:
        done = handle_user_input(character, done)
        
        handle_game_events(character)
     
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT :   
        renderer.render_map(screen, gameObjects)      
        # Limit to 20 frames per second
        clock.tick(60)
          
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
     
# Handles all interactions between game objects
def handle_game_events(character):
    
    if character.current_hp == 0:
        deathmsg("You just lost the game, play again?")
    # Move the object according to the speed vector.
    if character.coordinates[X_COOR_INDEX] + character.speed_vector[X_COOR_INDEX] in range(0,700): 
        character.move_x()
    else:
        character.current_hp -= 1
        print("out of bounds x-coordinates!!")
                    
    if character.coordinates[Y_COOR_INDEX] + character.speed_vector[Y_COOR_INDEX]  in range(0,500):   
        character.move_y()
    else:
        character.current_hp -= 1
        print("out of bounds y-coordinates!!")


def deathmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Yes", command = Utility.combine_funcs(popup.destroy, yes))
    B1.pack()
    B2 = ttk.Button(popup, text="No", command = no)
    B2.pack()
    popup.mainloop() 

def yes():
    run_game() 
def no():
    exit(0)
    
# All event processing done in this method
# includes key pressed for up down left right
# TODO: handle other key pressed and mouse clicks
def handle_user_input(character,done):

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            # User pressed down on a key
         
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                character.speed_vector[X_COOR_INDEX] =- 3
            elif event.key == pygame.K_RIGHT:
                character.speed_vector[X_COOR_INDEX] = 3
            elif event.key == pygame.K_UP:
                character.speed_vector[Y_COOR_INDEX] =- 3
            elif event.key == pygame.K_DOWN:
                character.speed_vector[Y_COOR_INDEX] = 3
                  
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                character.speed_vector[X_COOR_INDEX] = 0
            elif event.key == pygame.K_RIGHT:
                character.speed_vector[X_COOR_INDEX] = 0
            elif event.key == pygame.K_UP:
                character.speed_vector[Y_COOR_INDEX] = 0
            elif event.key == pygame.K_DOWN:
                character.speed_vector[Y_COOR_INDEX] = 0
    return done

 
run_game()