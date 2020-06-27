import os
import shutil

def selectiveCopy(folderTree,ext,destination):
    for folder,subfolder,files in os.walk(folderTree):
        for file in files:
            if file.endswith(ext):
                shutil.copy(os.path.join(folderTree,file),destination)
                print('Copying ' +file +' into '+ destination)
                file.close()

myfolderTree=input('Enter the absolute path of folder/ directory you want to search in :')
myext=input('Enter the extension you want to search and copy :')
mydestination=input('Enter the destination you want to save these selective copies into :')
selectiveCopy(myfolderTree,myext,mydestination)

# this was an example
selectiveCopy(r'C:\Users\yourName\OneDrive\Documents\diet_data','.csv',r'C:\Users\yourName\OneDrive\Documents\diet_data\copies')
                
