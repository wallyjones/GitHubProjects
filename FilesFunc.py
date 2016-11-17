import shutil
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import time
import datetime
import FilesGUI
import FilesMain

def askdirectory(self):
    src = filedialog.askdirectory()
    self.var_src.set(src)

def askdirectory2(self):
    dest = filedialog.askdirectory()
    self.var_dst.set(dest)

def filetransfer(self):
    srcPath=self.var_src.get()
    dstPath=self.var_dst.get()
    now = time.time()
    lst = Listbox(Tk(), width=50)
    lst.pack()
    for f in os.listdir(srcPath):
        src = os.path.join(srcPath,f)
        dst = os.path.join(dstPath,f)
        mtime = (os.path.getmtime(src)) # file creation/modification date
        timeDiff = time.time() - mtime #Difference from time of file creation or modification until current time
        _24hrsAgo = time.time() - (24 *60 *60) #Epoc time for a 24hr period is 86400 seconds
        last24hrs = time.time() - _24hrsAgo #Seconds that have occured within the last 24 hr period
        if timeDiff < last24hrs: #Seconds that have passed since file creation or modification from last 24 hrs
            shutil.move(src,dst) # move files to destination folder
            Path = os.listdir(dstPath)
            lst.insert(END,dst)
    dateCheck(self,now)
    funkyfunc()
    
def dateCheck(self,now):
    conn = sqlite3.connect('dateCheck.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""UPDATE tbl_datecheck SET col_date = (?)""",(now,)) # just overwrite previous date so it is always most current
        conn.commit()
    conn.close()
    lastDate = float(now)
    legibleDate = datetime.datetime.fromtimestamp(lastDate).strftime('%m/%d/%Y %H:%M')
    self.var_date.set("Last Checked: {}".format(legibleDate))

def funkyfunc():
    messagebox.showinfo("Check Complete.","There are no more eligable files to move at this time.")

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_datecheck""")
    count = cur.fetchone()[0]
    return cur,count
    
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

def show_date(self):
    conn = sqlite3.connect('dateCheck.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_date FROM tbl_datecheck""")
        data = cur.fetchone()[0]
        lastDate = float(data)
        legibleDate = datetime.datetime.fromtimestamp(lastDate).strftime('%m/%d/%Y  %H:%M')
        self.var_date.set("Last Check Date: "+legibleDate)
        conn.commit()
    conn.close()
