import scratchattach
import tkinter as tk
from tkinter import messagebox

class BetterScratchMenuBar(tk.Menu):
    def __init__(self,master,kind):
        super().__init__(master)
        self.master=master
        self.kind=kind
        self.create_items()
    def create_items(self):
        if self.kind=="master":
            self.master.window_menu=tk.Menu(self.master)
            self.master.window_menu.add_radiobutton(label="Main",command=self.master.focus)
        self.add_command(label="Thing",command=lambda:print("Thing!!!!"))
        self.add_cascade(label="Window",menu=self.master.window_menu)
class BetterScratchToplevel(tk.Toplevel):
    def __init__(self,master,kind):
        super().__init__(master)
        self.master=master
        self.menu=BetterScratchMenuBar(self.master,kind)
        self.config(menu=self.menu)
    def close(self):
        self.destroy()

class BetterScratchUserProfileEntry(BetterScratchToplevel):
    def __init__(self,master):
        super().__init__(master,"profilelookup")
        self.master=master
        self.create_form()
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

class BetterScratchAccountDialog(BetterScratchToplevel):
    def __init__(self,master):
        super().__init__(master,"loginbox")
        self.master=master
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

class BetterScratchProfilePage(BetterScratchToplevel):
    def __init__(self,master,sauser):
        super().__init__(master,"profile")
        self.master=master
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

class BetterScratch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.sessions=[]
        self.add_buttons()
        self.menu=BetterScratchMenuBar(self,"master")
        self.config(menu=self.menu)
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
        acct_dialog=BetterScratchAccountDialog(self)

def main():
    app=BetterScratch()
    app.mainloop()

if __name__=="__main__":
    main()