import tkinter as tk

class BetterScratchMenuBar(tk.Menu):
    def __init__(self,master,kind):
        super().__init__(master)
        self.master=master
        self.kind=kind
        self.create_items()
    def create_items(self):
        self.add_command(label="Thing",command=lambda:print("Thing!!!!"))
        self.open_menu=tk.Menu(self.master)
        self.open_menu.add_command(label="Lookup profile...",command=self.master.lookup_user)
        self.add_cascade(label="Open",menu=self.open_menu)
        self.add_cascade(label="Window",menu=self.master.window_menu)