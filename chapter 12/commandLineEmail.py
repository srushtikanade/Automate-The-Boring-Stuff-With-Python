#USAGE :commandLineEmail.py recipentAdd Subject MessageContent
#       argv[0]             argv[1]     argv[2]   argv[3:]



import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail')
if len(sys.argv)>2:
    sendTo=sys.argv[1]
    sendSubj=sys.argv[2]
    sendMsg=''.join(sys.argv[3:])
    userElem = browser.find_element_by_name('identifier')
    userElem.send_keys('your_real_username_here')
    userElem.send_keys(Keys.ENTER)
    
    passwordElem = browser.find_element_by_name('password')
    passwordElem.send_keys('your_real_password_here')
    passwordElem.send_keys(Keys.ENTER)
    
    composeElem=browser.find_element_by_class_name('z0')
    composeElem.click()

    toElem=browser.find_element_by_name('to')
    toElem.send_keys(sendTo)

    messageElem=browser.find_element_by_name('subjectbox')
    messageElem.send_keys(sendSubj)

    messageElem.send_keys(Keys.TAB + sendMsg + Keys.TAB + Keys.ENTER)

    browser.quit()
    
