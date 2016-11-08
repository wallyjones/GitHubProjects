import shutil
import os
from tkinter import *
import tkinter as tk
import sqlite3

import FilesMain
import FilesFunc

def load_gui(self):
    self.var_src = StringVar()
    self.var_dst = StringVar()
    
    self.btn_src = tk.Button(self.master,width=12,height=2,text='Main Folder:',command=lambda: FilesFunc.askdirectory(self))
    self.btn_src.grid(row=1,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.txt_src = tk.Entry(self.master,width=50,textvariable=self.var_src)
    self.txt_src.grid(row=1,column=1,padx=(26,0),pady=(45,10),sticky=W)
    self.btn_dst = tk.Button(self.master,width=12,height=2,text='Copied Folder:',command=lambda: FilesFunc.askdirectory2(self))
    self.btn_dst.grid(row=3,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.txt_dst = tk.Entry(self.master,width=50,textvariable=self.var_dst)
    self.txt_dst.grid(row=3,column=1,padx=(26,0),pady=(45,10),sticky=W)
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Send Files',command=lambda: FilesFunc.filetransfer(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    
if __name__ == "__main__":
    pass
