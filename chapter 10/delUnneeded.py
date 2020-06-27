import os

for folder,subfolder,files in os.walk(r'.'):
    for file in files:
        size=os.path.getsize(os.path.join(r'.',file))
        if size>100:
            print('Name of file larger than 100Mb is :'+ file)

# this is a function to do the same, here you can decide the size of files to delete and the folders to search/del into
def delLargeFiles(folderName,mysize):
    for folder,subfolder,files in os.walk(folderName):
        for file in files:
            size=os.path.getsize(os.path.join(folderName,file))
            if size>mysize:
                print('Name of file larger than '+ mysize +'is :'+ file)
                #os.remove(file) # this is the code for deleting those files, please use another module to save these temporarily deleted files like SEND2TRASh before completely deleting
                #print("File Removed!")

myfolderName=input('Enter the absolute path of folder you want to search into :')
mysize=input('What size do you want to find files above:')
delLargeFiles(myfolderName,mysize)
