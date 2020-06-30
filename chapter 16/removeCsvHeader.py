# removeCsvHeader.py - Removes the header from all CSV files in the current

import csv,os

os.makedirs('headerRemoved', exist_ok=True)
for csvFilename in os.listdir('.'):
    if csvFilename.endswith('.csv'):
        print('Removing header from ' + csvFilename + '...')
        csvRows=[]
        csvFileObj=open(csvFilename)
        readerObj=csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num>1: # since the header would be in 1st line, after it the data is appended to list
                csvRows.append(row)
        csvFileObj.close()
        newcsvFileObj=open(os.path.join('headerRemoved', csvFilename), 'w',newline='')
        newcsvWriter = csv.writer(newcsvFileObj)
        for row in csvRows:
                           newcsvWriter.writerow(row)
        newcsvFileObj.close()
                           
                         
        
