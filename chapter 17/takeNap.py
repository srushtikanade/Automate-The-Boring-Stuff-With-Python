import threading,time
print('Start of program')
def takeANap():
    time.sleep(5)
    print('Wake up!')
threadObj=threading.Thread(target=takeANap)
threadObj.start()
print('End of program!')

# this is a multi-thread program wherein the last line gets executed before wake up as two threads simultaneously function
