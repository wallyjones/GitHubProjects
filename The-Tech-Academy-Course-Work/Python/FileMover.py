import shutil
import os

src = r"C:\Users\jacob_000\Desktop\FolderA"
dest = r"C:\Users\jacob_000\Desktop\FolderB"

files = os.listdir(src)


print("These files have been moved to the following location.")
print (dest)
files = os.listdir(src)
now = time.time()
for f in files:
    if os.stat(os.path.join(src,f)).st_mtime > now - (1*86400):
        shutil.move(os.path.join(src,f), os.path.join(dest, f))
