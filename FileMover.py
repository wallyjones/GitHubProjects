import shutil
import os

src = "C:\Users\jacob_000\Desktop\FolderA"
dest = "C:\Users\jacob_000\Desktop\FolderB"

files = os.listdir(src)

print files
print("These files have been moved to the following location.")
print dest
for f in files:
    if f.endswith('.txt'):
        shutil.move(os.path.join(src,f), os.path.join(dest,f))


