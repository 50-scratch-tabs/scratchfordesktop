import scratchattach
import tkinter as tk

class BetterScratch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.sessions=[]

def main():
    app=BetterScratch()
    app.mainloop()

if __name__=="__main__":
    main()