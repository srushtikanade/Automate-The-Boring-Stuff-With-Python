import PyPDF2,os,sys


if len(sys.argv)>1:
    mypassword=sys.argv[1]

failed=[]

for folder,subfolder,files in os.walk('.'):
    for file in files:
        if file.endswith('.pdf'):
            path=os.path.join(folder,file)
            pdfReader=PyPDF2.PdfFileReader(open(path,'rb'))
            if pdfReader.isEncrypted:
                print(file+' is encypted.')
                if pdfReader.decrypt(mypassword) is True:
                    pdfWriter=PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    newpath=path[:-14]+'-Decrypted.pdf' # 14 because encryped has 9 letters, .pdf has 4 and 1 hypen, so we get the filename 
                    resultPdf=open(newpath,'wb')
                    pdfWriter.write(resultPdf)
                    resultPdf.close()
                    print('The password is correct, file has been decrypted!')
                else:
                    print('The password is incorrect.')
                    failed.append(file)
                    
                  
if failed!=0:
    print('Some PDFs could not be decrypted! Those filenames are :')
    for filename in failed:
        print(filename)
else:
    print('All PDFs have been succesfully decrypted. Your files are easy to access now.')

