import shutil
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox


# importing modules 
import FileTransfer_main
import FileTransfer_gui

# tkinter frame class that class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

#set where the source of the files are
source = 'C:\\Users\\jorda\\OneDrive\\Desktop\\folderA\\'

#set destination path to folderB
destination ='C:\\Users\\jorda\\OneDrive\\Desktop\\folderB\\'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i'
    shutil.move(source+i, destination)
