spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['apples', 'bananas']
spam3= ['apples']

def commaCodeList(mylist):
    if len(mylist)<2:
        print('Please add more elements, this works on longer lists')

    else:
        print(",".join(mylist[:-1]),end="")
        print(' and ' + mylist[-1])

commaCodeList(spam)
commaCodeList(spam2)
commaCodeList(spam3)
