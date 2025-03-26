import tkinter as tk

class BetterScratchCommentDisplay(tk.Frame):
    def __init__(self,master,commentobj):
        self.master=master
        super().__init__(master)
        i=0
        self.lbl=tk.Label(self,text=commentobj.author().username+" says: "+commentobj.content,wraplength=200, justify="left")
        self.lbl.pack(fill="both",expand=True)
        self.lbl.bind('<Configure>', lambda _: self.lbl.config(wraplength=self.winfo_width()))