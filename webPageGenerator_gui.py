

from tkinter import *
import tkinter as tk


import webPageGenerator

def load_gui(self):
    self.lbl_text = tk.Label(self.master,text='Enter text:')
    self.lbl_text.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.txt_text = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)


if __name__ == "__main__":
    pass
