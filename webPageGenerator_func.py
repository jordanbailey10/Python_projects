import os
from tkinter import *
import sqlite3

import webPageGenerator
import webPageGenerator_gui

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


#=========================================================
def create_db(self):
    conn = sqlite3.connect('db_webPageGenerator.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_webPageGenerator( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_text TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)
