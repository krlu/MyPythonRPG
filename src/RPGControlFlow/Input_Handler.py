import pygame

# Define coordinate indices to avoid magic numbers
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

class UserInputHandler(object):

    # TODO: handle other key pressed and mouse clicks
    def __init__(self):
        self.last_key_pressed = None
        
    # All event processing done in this method
    # includes key pressed for up down left right
    # NOTE: this only updates the character vector!!!
    # event handler moves the character separately!!!
    # other methods in here may call event handler
    def handle_movement_key_input(self,character,done):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                # User pressed down on a key
             
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                self.last_key_pressed = event.key
                
                if event.key == pygame.K_LEFT:
                    character.speed_vector[X_COOR_INDEX] =- character.move_speed
                elif event.key == pygame.K_RIGHT:
                    character.speed_vector[X_COOR_INDEX] =  character.move_speed
                elif event.key == pygame.K_UP:
                    character.speed_vector[Y_COOR_INDEX] =- character.move_speed
                elif event.key == pygame.K_DOWN:
                    character.speed_vector[Y_COOR_INDEX] =  character.move_speed
                      
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT and self.last_key_pressed != pygame.K_RIGHT:
                    character.speed_vector[X_COOR_INDEX] = 0
                elif event.key == pygame.K_RIGHT and self.last_key_pressed != pygame.K_LEFT:
                    character.speed_vector[X_COOR_INDEX] = 0
                elif event.key == pygame.K_UP and self.last_key_pressed != pygame.K_DOWN:
                    character.speed_vector[Y_COOR_INDEX] = 0
                elif event.key == pygame.K_DOWN and self.last_key_pressed != pygame.K_UP:
                    character.speed_vector[Y_COOR_INDEX] = 0
        return done
    
    
    def handle_ability_key_input(self, character, done):
        print("TO BE IMPLEMENTED!!!")
        
    
    
    
    