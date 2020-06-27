import os,re

#put the location of your og madlibs file
os.chdir(r'C:\Users\yourName\OneDrive\Documents')
madlibsRegex=re.compile(r'ADJECTIVE|NOUN|VERB|NOUN') #this searches for those words 
with open('madlibsOld.txt','r') as myFile,open('madlibsNew1.txt','w') as myFileNew:
    myLines=myFile.read()
    words=madlibsRegex.findall(myLines)
    for word in words:
        newWord=input('Enter a '+word+':')
        myLines=myLines.replace(word,newWord,1)
    myFileNew.write(myLines)
    print('Saved this round of madlibs game in file name : madlibsNew1.txt')
    print(myLines)

    
        
    # this is alternate way to solve it by taking those files individually
#myFile=open('madlibsOld.txt','r')
#myLines=myFile.read()
#myFileNew=open('madlibsNew.txt','w')
#madlibsRegex=re.compile(r'ADJECTIVE|NOUN|VERB|NOUN')
#words=madlibsRegex.findall(myLines)
#for word in words:
    #newWord=input('Enter a '+word+':')
    #myLines=myLines.replace(word,newWord,1)
#myFileNew.write(myLines)
#print('Saved this round of madlibs game in file name : madlibsNew.txt')
#print(myLines)
    
    #myFileNew.write(re.sub(word,newWord,myLines))
    #myFile.close()
    #myFileNew.close()
    
    
    
