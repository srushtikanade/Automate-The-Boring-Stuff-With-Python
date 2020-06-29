import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
for rowNum in range(1,ss.max_row): # ezsheets start from row 1 not 0
    if int(ss[0].getRow(rowNum)[0]) * int(ss[0].getRow(rowNum)[1]) != int(ss[0].getRow(rowNum)[2]):
        print('There is error in row '+ str(rowNum))

