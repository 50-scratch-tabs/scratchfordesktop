import scratchattach
import tkinter as tk

class BetterScratch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.sessions=[]