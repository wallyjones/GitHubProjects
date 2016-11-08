import shutil
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import time
import FilesFunc
import FilesGUI

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)

        FilesFunc.center_window(self,500,300)
        self.master.title("File Transfer")
        self.master.configure(bg="#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: FilesFunc.ask_quit(self))
        arg = self.master

        FilesGUI.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
