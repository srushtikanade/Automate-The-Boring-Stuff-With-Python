import pyinputplus as pyip

price=0
prompt='What bread type do you want?\n'
response= pyip.inputMenu(['wheat', 'white','sourdough'],prompt)
if response=='wheat':
    price+=10
elif response=='white':
    price+=7
elif response=='sourdough':
    price+=12
    
prompt='What protein type do you want?\n'
response= pyip.inputMenu(['chicken', 'turkey','ham','tofu'],prompt)
if response=='chicken':
    price+=10
if response=='turkey':
    price+=12
if response=='ham':
    price+=14
if response=='tofu':
    price+=15
    
prompt='Do you want cheese ?\n'
response= pyip.inputYesNo(prompt)
if response=='yes':
    prompt='What cheese type do you want?\n'
    response= pyip.inputMenu(['cheddar', 'swiss','mozzarella'],prompt)
    if response=='cheddar':
        price+=7
    if response=='swiss':
        price+=9
    if response=='mozzarella':
        price+=10
    
prompt='Do you want mayo?\n'
response= pyip.inputYesNo(prompt)
if response=='yes':
    price+=5

prompt='Do you want mustard?\n'
response= pyip.inputYesNo(prompt)
if response=='yes':
    price+=5

prompt='Do you want lettuce?\n'
response= pyip.inputYesNo(prompt)
if response=='yes':
    price+=5

prompt='Do you want tomatoes?\n'
response= pyip.inputYesNo(prompt)
if response=='yes':
    price+=5

print('You have to pay  %s  for this sandwich!' % (price))
prompt='How many sandwiches do you want?\n'
response= pyip.inputInt(prompt,min=1)
print('You have to pay  %s  for %s sandwich(s)!' % (price*response,response))





