import os
from tkinter import *
import tkinter as tk
import shutil
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askdirectory

# tkinter frame class that class will inherit from

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("File Transfers")
        self.sourceEntrytext = StringVar()
        self.destinationEntrytext = StringVar()
        
        self.sourceLabel = Label(text = "Source Folders", font=("Arial", 12))   ##both of these are required for any widget that is created, one to define it,
        self.sourceLabel.grid(row=0,column=0, padx=20, pady=(20,0))  ## and one to tell Tkinter where it should be placed.
        
        self.sourceEntry = Entry(self.master, textvariable = self.sourceEntrytext, font=("Helvetica", 12),width=12)
        self.sourceEntry.grid(row=1, column=0, padx=(30,15), pady=(10,10), columnspan=2, sticky=W+E)

        self.sourceButton = Button(self.master, text="Source", width=12, height=1, command=self.get_source)   ##this way or using the lambdas are how to call a function with a Tkinter button. Which one you use mostly depends on how the object is being used.  Since this is all on one page you don't need to rely on the lambda method.
        self.sourceButton.grid(row=2, column=1, padx=(0,10) , pady=(0,10))

        self.destinationLabel = Label(text = "Retrieve Folders", font=("Arial", 12))
        self.destinationLabel.grid(row=2,column=0,padx=20, pady=(20,0))

        self.destinationEntry = Entry(self.master, textvariable = self.destinationEntrytext, font=("Helvetica", 12),width=12)
        self.destinationEntry.grid(row=3, column=0, padx=(30,15), pady=(10,10), columnspan=2, sticky=W+E)
        
        self.destinationButton = Button(self.master, text="Destination", width=12, height=1, command=self.get_destination)   ##this way or using the lambdas are how to call a function with a Tkinter button. Which one you use mostly depends on how the object is being used.  Since this is all on one page you don't need to rely on the lambda method.
        self.destinationButton.grid(row=4, column=1, padx=(0,10) , pady=(0,10))

        self.submitButton = Button(self.master, text="Submit", width=12, height=1, command=self.file_transfer) ##command uses function name ex def get_spource  ##this way or using the lambdas are how to call a function with a Tkinter button. Which one you use mostly depends on how the object is being used.  Since this is all on one page you don't need to rely on the lambda method.
        self.submitButton.grid(row=6, column=1, padx=(0,10) , pady=(0,10))

        self.master.columnconfigure(1,weight=1)

    def get_source(self):
        source = askdirectory()
        self.sourceEntrytext.set(source)

    def get_destination(self):
        destination = askdirectory()
        self.destinationEntrytext.set(destination)

    def file_transfer(self):
        source = self.sourceEntrytext.get()
        destination = self.destinationEntrytext.get()

        
        files = os.listdir(source)

        for i in files:
            #we are saying move the files represented by 'i'
            shutil.move(source+"/"+i, destination)

        





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
