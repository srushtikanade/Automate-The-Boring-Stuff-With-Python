import time,pyperclip

print('Please ENTER to begin.Afterward,press ENTER to "click" the stopwatch.press Ctrl-C to quit.')
input()
print('Started')
startTime=time.time()
lastTime=startTime
lapNum=1
try:
    while True:
        input()
        lapTime=round(time.time()-lastTime,2)
        totalTime=round(time.time()-startTime,2)
        #print('Lap #%s: %s (%s)' % (str(lapNum), str(totalTime), str(lapTime)), end='') This is the line before we extended the project for prettified stopwatch
        lap='Lap#{}{}({})'.format((str(lapNum)+':').ljust(3),str(totalTime).rjust(5),str(lapTime).rjust(6))
        print(lap,end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
        pyperclip.copy(lap)
except KeyboardInterrupt:
    print('\nDone')
