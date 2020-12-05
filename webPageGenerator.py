
from tkinter import *
import tkinter as tk
from tkinter import messagebox


# importing modules 
import webPageGenerator_gui
import webPageGenerator_func




# tkinter frame class that class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame config
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        webPageGenerator_func.center_window(self,500,300)
        self.master.title("Web Page Generator")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: webPageGenerator_func.ask_quit(self))
        arg = self.master


        webPageGenerator_gui.load_gui(self)

        #dropdown menue
        menubar = Menu(self.master) 
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: studentTracking_func.ask_quit(self))

def generator_func(self):
    userInput = self.txt_entry.get();
    #Opening summer_sale,html, append content
    f = open("summer_sale.html", "a")
    f.write("Here is the html code ad user input"+userInput)
    f.close()
    webbrowser.open('summer_sale.html', new=2)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    
