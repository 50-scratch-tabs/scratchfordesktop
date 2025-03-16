import scratchattach
import tkinter as tk

class BetterScratchAccountDialog(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.create_form()
    def create_form(self):
        self.username_label=tk.Label(self,text="Username:")
        self.username_label.grid(row=0,column=0)
        self.username_entry=tk.Entry(self)
        self.username_entry.grid(row=0,column=1)
        self.password_label=tk.Label(self,text="Password:")
        self.password_label.grid(row=1,column=0)
        self.password_entry=tk.Entry(self)
        self.password_entry.grid(row=1,column=1)
        self.submit_button=tk.Button(self,text="Log in",command=self.loginhandler)
        self.submit_button.grid(row=2,column=0,columnspan=2)

class BetterScratch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.sessions=[]
        self.add_buttons()
    def add_buttons(self):
        addacctbutton=tk.Button(self,text="Add account",command=self.add_acct_handler)
        addacctbutton.pack()
    def add_acct_handler(self):
        acct_dialog=BetterScratchAccountDialog(self)
        acct_dialog

def main():
    app=BetterScratch()
    app.mainloop()

if __name__=="__main__":
    main()