from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()
browser.get('https://play2048.co/')
htmlElm=browser.find_element_by_tag_name('html')
while True:
    htmlElm.send_keys(Keys.UP)
    htmlElm.send_keys(Keys.RIGHT)
    htmlElm.send_keys(Keys.DOWN)
    htmlElm.send_keys(Keys.LEFT)
    

