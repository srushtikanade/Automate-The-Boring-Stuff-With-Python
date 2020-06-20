import pyautogui,datetime,time

now = datetime.datetime.now()
now_plus_10 = now + datetime.timedelta(minutes = 10)
if datetime.datetime.now()==now_plus_10:
    pyautogui.moveRel(10,0,0.5)


#alternate way, moves the cursor back to orignal position in a sec
try:
    while True:
        print('Every 10 minutes, the cursor moves and comes back to orignal position')
        pyautogui.moveRel(10,0,0.5)
        pyautogui.moveRel(-10,0,0.5)
        time.sleep(10*60)

except KeyboardInterrupt:
    print('Error occoured; please manually move cursor every 10 minutes!')

