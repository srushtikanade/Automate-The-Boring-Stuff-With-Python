import re
# these are just trials I attempted to understand individual cases
text='*********hello,WORLD******'
stripRegex=re.compile(r'^[*]*$')
mo=stripRegex.findall(text)
print(re.sub('(\*)', '', text))

text1='&&&&&&&&&&&srush&&&&'
print(re.sub('([@!#$^&*%])', '', text1))

text2='     hey   '
print(re.sub(' ', '', text2))

text3='charspamspamcharmyworldspamcharspamchar'
print(re.sub(r'([spam])', '', text3))

def stripRegText(text,char=''):
    if char=="":
        LeftStripStr=re.sub('^\s+','', mytext2)
        print(re.sub('$\s+','',LeftStripStr))#this does the right side strip 
    else:
        charRegex=re.compile(r'[%s]' %char)
        print(charRegex.sub( '', mytext1))


mytext1='$$$$$$$$$MY RULES$$$$$$$$'
mytext2='     hello this is a trial Text string!    bye     '
stripRegText(mytext1,'$')
stripRegText(mytext2)


