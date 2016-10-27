import shutil
import os
import time
from datetime import datetime


src = "C:\Users\jacob_000\Desktop\Customertxt"
dest = "C:\Users\jacob_000\Desktop\HomeOffice"

files = os.listdir(src)
now = time.time()
for f in files:
    if os.stat(os.path.join(src,f)).st_mtime > now - (1*86400):
        shutil.move(os.path.join(src,f), os.path.join(dest, f))


