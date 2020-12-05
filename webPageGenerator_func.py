import os
from tkinter import *
from tkinter import messagebox
import sqlite3

import webPageGenerator
import webPageGenerator_gui
import webbrowser


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def AddText(self):
    #grabs the text from the Entry widget and sabes it to a variable named "AddText"
    textToAdd = self.text_entry.get()
    #Opening summer_sale,html, append content
    f = open("summer_sale.html","a")
    f.write(textToAdd)
    f.close()
    #opens the "summer sale.html" file in browser
    webbrowser.open('summer_sale.html')

    
# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


