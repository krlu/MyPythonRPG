from test.test_idle import tk
from tkinter import ttk
from RPGUtils import Utility


NORM_FONT = ("Helvetica", 10)
# Define coordinate indices to avoid magic numbers
X_COOR_INDEX = 0 
Y_COOR_INDEX = 1

class EventHandler(object):

    def __init__(self):
        pass
    # Handles all interactions between game objects
    def handle_game_events(self,character):
        
        if character.current_hp == 0:
            self.deathmsg("You just lost the game, play again?")
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
                
    def deathmsg(self, msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Yes", command = Utility.combine_funcs(popup.destroy, self.yes))
        B1.pack()
        B2 = ttk.Button(popup, text="No", command = self.no)
        B2.pack()
        popup.mainloop() 
    
    def yes(self):
        import Run_Game
        Run_Game.run_game() 
    def no(self):
        exit(0)