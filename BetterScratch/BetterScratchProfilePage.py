import tkinter as tk

from .BetterScratchCommentDisplay import BetterScratchCommentDisplay
from .BetterScratchToplevel import BetterScratchToplevel

class BetterScratchProfilePage(BetterScratchToplevel):
    def __init__(self,master,sauser):
        self.master=master
        super().__init__(master,"profile")
        self.sauser=sauser
        self.create_form()
    def create_form(self):
        self.abtmelabel=tk.Label(self,text="About me")
        self.abtmelabel.grid(row=0,column=0)
        self.aboutme=tk.Text(self,width=30,height=10)
        self.aboutme.grid(row=1,column=0)
        self.aboutme.insert("0.0",self.sauser.about_me)
        self.aboutme.config(state="disabled")
        self.wiwolabel=tk.Label(self,text="What I'm working on")
        self.wiwolabel.grid(row=2,column=0)
        self.wiwo=tk.Text(self,width=30,height=10)
        self.wiwo.grid(row=3,column=0)
        self.wiwo.insert("0.0",self.sauser.wiwo)
        self.wiwo.config(state="disabled")
        self.commentsframe=tk.Frame(self)
        for i in self.sauser.comments():
            BetterScratchCommentDisplay(self.commentsframe,i).pack()
        self.commentsframe.grid(row=1,column=0)
