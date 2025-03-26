import tkinter as tk
from .BetterScratchMenuBar import BetterScratchMenuBar
from .BetterScratchProfilePage import BetterScratchProfilePage
from .BetterScratchUserProfileEntry import BetterScratchUserProfileEntry
from .BetterScratchLoginDialog import BetterScratchLoginDialog

class BetterScratch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.windowmenuitems=[self]
        self.window_menu=tk.Menu(self,tearoff=False)
        self.sessions=[]
        self.add_buttons()
        self.menu=BetterScratchMenuBar(self,"master")
        self.config(menu=self.menu)
        self.window_menu.add_radiobutton(label=self.title(),command=self.focus)
        self.title("BetterScratch")
        self.minsize(180,100)
        self.geometry("180x100")
    def create_user_profile_dialog(self,username):
        page=BetterScratchProfilePage(self,username)
    def add_buttons(self):
        addacctbutton=tk.Button(self,text="Add account",command=self.add_acct_handler)
        addacctbutton.pack()
        showuserbutton=tk.Button(self,text="Lookup user",command=self.lookup_user)
        showuserbutton.pack()
    def lookup_user(self):
        user_dialog=BetterScratchUserProfileEntry(self)
    def add_acct_handler(self):
        acct_dialog=BetterScratchLoginDialog(self)
    def title(self,title=None):
        if title is not None:
            self.window_menu.entryconfigure(self.windowmenuitems.index(self)+1,label=title)
        return super().title(title)
