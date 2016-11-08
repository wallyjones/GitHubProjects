import shutil
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import time

import FilesGUI
import FilesMain

def askdirectory(self):
    src = filedialog.askdirectory()
    self.var_src.set(src)
    return src

def askdirectory2(self):
    dest = filedialog.askdirectory()
    self.var_dst.set(dest)
    return dest

def filetransfer(self):
    srcPath=self.var_src.get()
    dstPath=self.var_dst.get()
    now = time.time()
    for f in os.listdir(srcPath):
        if os.stat(os.path.join(srcPath,f)).st_mtime > now - (1*86400):
            shutil.move(os.path.join(srcPath,f), os.path.join(dstPath, f))
    return ask_quit2(self)
    
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def ask_quit2(self):
    if messagebox.askokcancel("Files Moved", "The process is complete"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def center_window(self, w, h): 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
