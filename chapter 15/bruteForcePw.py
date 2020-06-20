import PyPDF2,os


with open('dictionary.txt','r') as file:
    words=file.readlines()
    
        
for folder,subfolder,files in os.walk(r'C:\Users\YourName\OneDrive\Documents'): # or  could just search in root os.walk('.')
    for file in files:
        if file.endswith('.pdf'):
            mypdf=open(os.path.join(r'C:\Users\YourName\OneDrive\Documents',file),'rb')
            pdfReader=PyPDF2.PdfFileReader(mypdf)
            if pdfReader.isEncrypted:
                for word in words:
                    word=word.strip()
                    lower=word.lower()
                    upper=word.upper()
                    
                    
                    if pdfReader.decrypt(lower) is True:
                        print('The password is :'+lower)
                        break
                    elif pdfReader.decrypt(upper) is True:
                        print('The password is :'+upper)
                        break
                    else:
                        print('Could not guess the password!. Thats a safe one to avoid brute force')

