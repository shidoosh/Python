import os

#finding the total size of all the files in a folder 
totalSize = 0
for filename in os.listdir('C:\\Users\\Stefanie\\Desktop\\Code\\Python'):
    #don't count non-folders
    if not os.path.isfile(os.path.join('C:\\Users\\Stefanie\\Desktop\\Code\\Python', filename)):
        continue
    totalSize += os.path.getsize(os.path.join('C:\\Users\\Stefanie\\Desktop\\Code\\Python', filename))
