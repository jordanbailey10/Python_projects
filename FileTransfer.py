import shutil
import os

#set where the source of the files are
source = 'C:\\Users\\jorda\\OneDrive\\Desktop\\folderA\\'

#set destination path to folderB
destination ='C:\\Users\\jorda\\OneDrive\\Desktop\\folderB\\'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i'
    shutil.move(source+i, destination)
