import re

#text='today is 15/10/1909'
#dateRegex=re.compile(r'(\b([1-9]|[12][0-9]|3[01])\b)/(\b([1-9]|1[0-2])\b)/(\d{4})')
#inputDate=dateRegex.search(text)


day,month,year = [0,0,0]

#checks for valid format,informs if leap year, months with accurate number of days and informs if it is the last day today

def checkValidDate(date):
    dateRegex=re.compile(r'(\b([1-9]|[12][0-9]|3[01])\b)/(\b([1-9]|1[0-2])\b)/(\d{4})')
    inputDate=dateRegex.search(date)
    day,month,year = int(inputDate.group(1)),int(inputDate.group(3)),int(inputDate.group(5))
    print(day,month,year)
    if year<1000 or year>2999:
        print('Year error; Although valid format')
        return False
    if inputDate==None:
        print('Invalid format.')
    if year% 4 == 0 :
        print('It is a leap year!')
        if day==29 and month==2:
            print('Today is an extra day in leap year!')      
    if day==31:
        print('Today is the last day of this month. It was a long month.')

    if month==4 or month==6 or month==9 or month==11:
        print('This month has 30 days.')
        if day==30:
            print('Today is the last day of this month.')
        if day==31:
            print('Valid format, Day error!')
            
        
    else:
        print('The format as well as date is correct.')
    



myDate=(input('Please input a date: '))
checkValidDate(myDate)

