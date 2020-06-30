import PyPDF2,os,sys


if len(sys.argv)>1:
    mypassword=sys.argv[1]

failed=[]

for folder,subfolder,files in os.walk('.'):
    for file in files:
        if file.endswith('.pdf'):
            path=os.path.join(folder,file)
            pdfReader=PyPDF2.PdfFileReader(open(path,'rb'))
            if not pdfReader.isEncrypted:
                pdfWriter=PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(mypassword)
                newpath=path[:-4]+'-Encrypted.pdf'
                resultPdf=open(newpath,'wb')
                pdfWriter.write(resultPdf)
                resultPdf.close()

                newpdfReader=PyPDF2.PdfFileReader(open(newpath,'rb'))
                if newpdfReader.isEncrypted and newpdfReader.decrypt(mypassword) is True:
                    print('This PDF has been encrypted and will be deleted.')
                    os.remove(path) # it would be better to use sen2trash or other soft delete in case of errors
                else:
                    failed.append(file)

                    
if failed!=0:
    print('Some PDFs could not be encrypted! Those filenames are :')
    for filename in failed:
        print(filename)
else:
    print('All PDFs have been succesfully encrypted. Your files are safer now.')

