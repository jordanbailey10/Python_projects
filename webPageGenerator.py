
from tkinter import *
import tkinter as tk
from tkinter import messagebox


# importing modules 
import webPageGenerator_gui
import webPageGenerator_func




# tkinter frame class that class will inherit from

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("Customize Webpage")

        self.labelTxt = Label(text = "Customize your webpage by entering text, then click to view!", font=("Arial", 12))   ##both of these are required for any widget that is created, one to define it,
        self.labelTxt.grid(row=0,column=0, padx=20, pady=(20,0))  ## and one to tell Tkinter where it should be placed.  

        self.txtEntry = Entry(self.master, font=("Helvetica", 12))
        self.txtEntry.grid(row=1, column=0, padx=(30,15), pady=(10,10), columnspan=2, sticky=W+E)

        self.btnSubmit = Button(self.master, text="Submit", width=12, height=1, command=self.customEntry)   ##this way or using the lambdas are how to call a function with a Tkinter button. Which one you use mostly depends on how the object is being used.  Since this is all on one page you don't need to rely on the lambda method.
        self.btnSubmit.grid(row=2, column=1, padx=(0,10) , pady=(0,10))

        self.master.columnconfigure(1,weight=1)

    def customEntry(self):
        customText = self.txtEntry.get()      ##   .get() targets the txtEntry in your frame and gets whatever has been put into it. There is also a .set() that is related.  The self is it acting as the current 'object' that all of these widgets are connected to. Effectively the gui itself.  That is then saved to your variable.
        htmlFile = open("user_customized.html", "w")
        htmlFormat = "<html>\n<body>\n<p>" + customText + "</p>\n</body>\n</html>"
        htmlFile.write(htmlFormat)
        htmlFile.close()
        webbrowser.open_new_tab("user_customized.html")





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    
