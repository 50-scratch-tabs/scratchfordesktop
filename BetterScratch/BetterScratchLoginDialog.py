import scratchattach
from .BetterScratchToplevel import BetterScratchToplevel
from tkinter import messagebox
import tkinter as tk

class BetterScratchLoginDialog(BetterScratchToplevel):
    def __init__(self,master):
        self.master=master
        super().__init__(master,"loginbox")
        self.create_form()
    def loginhandler(self):
        try:
            session=scratchattach.login(self.username_entry.get(),self.password_entry.get())
        except:
            self.incorrect_label.grid(row=2,column=0,columnspan=2)
        else:
            self.master.sessions.append(session)
            messagebox.showinfo("Login successful")
            self.destroy()
    def create_form(self):
        self.username_label=tk.Label(self,text="Username:")
        self.username_label.grid(row=0,column=0)
        self.username_entry=tk.Entry(self)
        self.username_entry.grid(row=0,column=1)
        self.password_label=tk.Label(self,text="Password:")
        self.password_label.grid(row=1,column=0)
        self.password_entry=tk.Entry(self,show="\u25cf")
        self.password_entry.grid(row=1,column=1)
        self.incorrect_label=tk.Label(self,text="Your username or password is incorrect")
        self.submit_button=tk.Button(self,text="Log in",command=self.loginhandler)
        self.submit_button.grid(row=3,column=0,columnspan=2)
