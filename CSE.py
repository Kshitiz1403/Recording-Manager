import os
import shutil
from datetime import date
today = str(date.today())[-2:]

source = "E:\\vitbhopal.ac.in\\587-BL2020-Object Oriented Programming With C++ - Recordings"
destination = "E:\\OneDrive - vitbhopal.ac.in\\Classes\\C++\\March"

for i in reversed(os.listdir(source)):
    dateoffile = i[25:27]
    if dateoffile!=today:
        continue

    print("File being copied is: "+i)
    sourcefile = source+'\\'+i
    # #source to destination
    dest = shutil.copy(sourcefile,destination)
    print("Successful, file",i,"is copied to",destination)

    print("File renaming in process")
    destinationfile = destination + '\\' + i
    file_name = dateoffile + " Mar C++.mp4"
    newfile = destination + '\\' + file_name
    os.rename(destinationfile,newfile)
    print("File",i,"renamed to",file_name)
    break