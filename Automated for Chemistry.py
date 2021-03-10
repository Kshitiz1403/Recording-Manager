import os
import shutil

source = "E:\\OneDrive - vitbhopal.ac.in\\OBS Classes"
destination = "E:\\OneDrive - vitbhopal.ac.in\\Classes\\Chemistry\\March"

for i in reversed(os.listdir(source)):
    print("File being moved is: "+i)
    sourcefile = source+'\\'+i
    #source to destination
    dest = shutil.move(sourcefile,destination)
    print("Successful, file",i,"is moved to",destination, "from", source)

    print("File renaming in process")
    destinationfile = destination + '\\' + i
    date = i[8:10]
    file_name = date + " Mar Chemistry.mp4"
    newfile = destination + '\\' + file_name
    os.rename(destinationfile,newfile)
    print("File",i,"renamed to",file_name)
    break
