import os
import shutil

source = "E:\\vitbhopal.ac.in\\Discrete Mathematics And Graph Theory (B slot) - Recordings"
destination = "E:\\OneDrive - vitbhopal.ac.in\\Classes\\Maths\\March"

for i in reversed(os.listdir(source)):

    print("File being copied is: "+i)
    sourcefile = source+'\\'+i
    #source to destination
    dest = shutil.copy(sourcefile,destination)
    print("Successful, file",i,"is copied to",destination)

    print("File renaming in process")
    destinationfile = destination + '\\' + i
    date = i[27:29]
    file_name = date + " Mar Maths.mp4"
    newfile = destination + '\\' + file_name
    os.rename(destinationfile,newfile)
    print("File",i,"renamed to",file_name)
    break