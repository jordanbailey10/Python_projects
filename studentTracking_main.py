from tkinter import *
import tkinter as tk
from tkinter import messagebox


# importing modules 
import studentTracking_func
import studentTracking_gui

# tkinter frame class that class will inherit from
class ParentWindow(Frame):
    def __init(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame config
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        studentTracking_func.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill50_phonebook_func.ask_quit(self))
        arg = self.master


        drill50_phonebook_gui.load_gui(self)

        #dropdown menue
        menubar = Menu(self.master)
        filemenu.add_separator()
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: drill50_phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) 
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Student Tracker") 
        menubar.add_cascade(label="Help", menu=helpmenu)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    

