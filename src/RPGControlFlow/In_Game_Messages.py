from test.test_idle import tk
from tkinter import ttk
from RPGUtils import Utility


NORM_FONT = ("Helvetica", 10)

class MessagesInGame(object):   
    
    def __init__(self):
        pass
    
    def death_msg(self, msg):
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