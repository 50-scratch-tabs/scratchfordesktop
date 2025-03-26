import tkinter as tk
from tkinter import messagebox
from .BetterScratchToplevel import BetterScratchToplevel
import scratchattach

class BetterScratchUserProfileEntry(BetterScratchToplevel):
    def __init__(self,master):
        self.master=master
        super().__init__(master,"profilelookup")
        self.create_form()
        self.resizable(False)
        self.minsize(180,50)
        self.geometry("180x50")
    def create_form(self):
        self.nouserlabel=tk.Label(text="That user does not exist.")
        self.usernameentry=tk.Entry(self)
        self.usernameentry.grid(row=1,column=0)
        self.lookupbutton=tk.Button(self,text="Lookup",command=self.lookup)
        self.lookupbutton.grid(row=2,column=0)
    def lookup(self):
        user=self.usernameentry.get()
        try:
            sauserobject=scratchattach.get_user(user)
        except scratchattach.utils.exceptions.UserNotFound:
            self.nouserlabel.grid(row=0,column=0)
        else:
            if not sauserobject.does_exist():
                messagebox.showwarning("Deleted account","This user account has been deleted, but you can still view the profile.")
            self.master.create_user_profile_dialog(sauserobject)