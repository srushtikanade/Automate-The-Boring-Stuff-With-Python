import ezsheets
ss = ezsheets.upload('example.xlsx')
ss.title
ss.downloadAsODS() # Downloads the spreadsheet as an OpenOffice file.
ss.downloadAsCSV() # Only downloads the first sheet as a CSV file.
ss.downloadAsTSV() # Only downloads the first sheet as a TSV file.
ss.downloadAsPDF() # Downloads the spreadsheet as a PDF.
ss.downloadAsHTML() # Downloads the spreadsheet as a ZIP of HTML files.

