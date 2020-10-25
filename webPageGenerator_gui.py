from tkinter import *
import tkinter as tk



#importing modules
import webPageGenerator



def load_gui(self):

    self.lbl_entry = tk.Label(self.master,text='Enter text:')
    self.lbl_entry.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)


    self.txt_entry = tk.Entry(self.master,text='')
    self.txt_entry.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: studentTracking_func.addToList(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: studentTracking_func.onUpdate(self))
    self.btn_update.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: studentTracking_func.onDelete(self))
    self.btn_delete.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: studentTracking_func.ask_quit(self))
    self.btn_close.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)





if __name__ == "__main__":
    pass

