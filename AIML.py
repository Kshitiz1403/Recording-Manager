import os
import shutil

source = "E:\\vitbhopal.ac.in\\AI &ML(F11+F12+F13) - Recordings"
destination = "E:\\OneDrive - vitbhopal.ac.in\\Classes\\AIML\\March"

for i in reversed(os.listdir(source)):

    if i=="AI&ML(F11+F12+F13)_20210210_091028.mp4":
        continue

    print("File being copied is: "+i)
    sourcefile = source+'\\'+i
    
    #source to destination
    
    dest = shutil.copy(sourcefile,destination)
    print("Successful, file",i,"is copied to",destination)

    destinationfile = destination + '\\' + i
    date = i[25:27]
    file_name = date + " Mar AIML.mp4"
    newfile = destination + '\\' + file_name
    
    os.rename(destinationfile,newfile)
    print("File",i,"renamed to",file_name)
    break