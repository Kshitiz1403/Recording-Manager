# Recording-Manager
A Python Script to automatically download Teams Recordings to local system and then upload it to onedrive after renaming it.

After every online class, I had to manually download, rename and then upload the recording from MS Teams to my OneDrive folder. I found this really tedious and to do it for 3 classes daily was such a headache. 
So randomly sitting on the couch I thought of an idea to automate this process and here it is!
A Python Script to automate the process.

The program copies the file from Sharepoint's synced folder to a Onedrive Folder using os and shutil module.
Once the file is copied, the program then renames the copied file to a fixed format like [09 Mar Maths.mp4] and then the file is uploaded to OneDrive.
