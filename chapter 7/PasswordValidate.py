import re

text='my pw is abcdef45@'
pwRegex=re.compile(r'[a-zA-Z0-9#@$]{8}')
mo=pwRegex.findall(text)


def PasswordValidDetect(pw):
    pwRegex=re.compile(r'([a-zA-Z0-9#@$]){8,14}')
    pwResult=pwRegex.search(pw)
    if pwResult!=None:
        print('That password meets requirements, you may proceed to use it further.')
    else:
        print('That doesnt qualify.Please change your password ASAP.')
    
    
password=input('Check if your password is valid before using :')
PasswordValidDetect(password)

# other way to do it, so one could also revert back w an error

pwLenRegex=re.compile(r'.{8,14}')
pwCharRegex=re.compile(r'[#@$]{1,}')
pwUpperAlphaRegex=re.compile(r'[A-Z]{1,}')
pwLowerAlphaRegex=re.compile(r'[a-z]{1,}')
pwDigitRegex=re.compile(r'[0-9]{1,}')

def ValidatePassword(pw):
    if pwLenRegex.search(pw) is None:
        print('Must be more than 8 chars at least!')
    elif pwCharRegex.search(pw) is None:
        print('Must have at least one special character.')
    elif pwUpperAlphaRegex.search(pw) is None:
        print('Must have at least one upperCase letter.')
    elif pwLowerAlphaRegex.search(pw) is None:
        print('Must have at least one lowerCase letter.')
    elif pwDigitRegex.search(pw) is None:
        print('Must have at least one digit.')
    else:
        print('The password meets requirements. You may proceed to use it further, it is safe.')

password=input('Check if your password is valid before using :')
ValidatePassword(password)


    

