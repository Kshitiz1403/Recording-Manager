import os
import shutil
from datetime import date
today = str(date.today())[-2:]

source = "E:\\OneDrive - vitbhopal.ac.in\\OBS Classes"
destination = "E:\\OneDrive - vitbhopal.ac.in\\Classes\\Chemistry\\March"

for i in reversed(os.listdir(source)):
    dateoffile = i[8:10]
    if today!=dateoffile:
        continue

    print("File being moved is: "+i)
    sourcefile = source+'\\'+i
    #source to destination
    dest = shutil.move(sourcefile,destination)
    print("Successful, file",i,"is moved to",destination, "from", source)

    print("File renaming in process")
    destinationfile = destination + '\\' + i
    file_name = dateoffile + " Mar Chemistry.mp4"
    newfile = destination + '\\' + file_name
    os.rename(destinationfile,newfile)
    print("File",i,"renamed to",file_name)
    break