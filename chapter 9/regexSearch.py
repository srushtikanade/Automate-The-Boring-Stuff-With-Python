import os,re

myRegex=re.compile(r'srush|srushti') #here I've created a regex to find my name(s) in text files in document folder

for folder,subfolder,files in os.walk(r'C:\Users\yourName\OneDrive\Documents'):
    for file in files:
        if file.endswith('.txt'):
            thisFile=open(os.path.join(r'C:\Users\yourName\OneDrive\Documents',file),'r')
            content=thisFile.read()
            matches=myRegex.search(content)
            if matches!=None:
                print('Files that have these word(s) are in lines:' + str(content) +' in file :' + str(thisFile))
                thisFile.close()
            
# This is the same program but as a whole function that you can call for multiple regex,files.
def regexSearch(yourregex,yourFile):
    for folder,subfolder,files in os.walk(yourFile):
    for file in files:
        if file.endswith('.txt'):
            thisFile=open(os.path.join(yourFile,file),'r')
            content=thisFile.read()
            matches=yourRegex.search(content)
            if matches!=None:
                print('Files that have these word(s) are in lines:' + str(content) +' in file :' + str(thisFile))
                thisFile.close()
            
    


myregex=input('Enter your regex:')
myFile=input('Enter the abs location you want to search in :')
regexSearch(myregex,myFile)

