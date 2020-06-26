import pyinputplus as pyip
while True:
    prompt='Want to know how to keep an idiot busy for hours?\n'
    response= pyip.inputYesNo(prompt)
    if response=='no':
        break
    print('Thank you.Have a nice day!')

# in non-english language, by setting yes no values prior. This is in Hindi
while True:
    prompt='kya aapko busy rakhna hai khudko?\n'
    response= pyip.inputYesNo(prompt,yesVal='haan',noVal='nahin')
    if response=='no':
        break
    print('Theekay!')
