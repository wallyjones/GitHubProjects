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

        conn = sqlite3.connect('dateCheck.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_datecheck( \
            col_date TEXT \
            );")
            conn.commit()
            cur,count=FilesFunc.count_records(cur)
            if count < 1:
                cur.execute("""INSERT INTO tbl_datecheck(col_date) VALUES (?)""",('Empty',))
                conn.commit()

        FilesGUI.load_gui(self)
        
        conn.close()
            
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
