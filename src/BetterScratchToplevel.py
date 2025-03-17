import tkinter as tk
from .BetterScratchMenuBar import BetterScratchMenuBar

class BetterScratchToplevel(tk.Toplevel):
    def __init__(self,master,kind):
        self.master.windowmenuitems.append(self)
        super().__init__(master)
        self.master=master
        self.menu=BetterScratchMenuBar(self.master,kind)
        self.config(menu=self.menu)
        self.master.window_menu.add_radiobutton(label=self.title(),command=self.focus)
        self.protocol("WM_DELETE_WINDOW",self.close)
    def close(self):
        self.master.window_menu.delete(self.master.windowmenuitems.index(self)+1)
        del self.master.windowmenuitems[self.master.windowmenuitems.index(self)]
        self.destroy()
    def title(self,title=None):
        if title is not None:
            self.master.window_menu.entryconfigure(self.master.windowmenuitems.index(self)+1,label=title)
        return super().title(title)