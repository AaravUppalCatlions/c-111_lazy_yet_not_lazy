import os
import shutil

source = "D:/Downloads"
to_dir = "D:/Desktop/downloaded photos"

list1 = os.listdir(source)
#print(list1)

for file in list1:
    name,ext = os.path.splitext(file)
    print(name,ext)
