import tkinter as tk

class BetterScratchCommentDisplay(tk.Frame):
    def __init__(self,master,commentobj):
        self.master=master
        super().__init__(master)
        self.lbl=tk.Label(self,text=commentobj.author().username+" says: "+commentobj.content)
        self.lbl.pack()