import random
numberOfStreaks = 0
coinFlip=[]
streak=0
for experimentNumber in range(10000):
    for i in range(100):
        coinFlip.append(random.randint(0,1))

    for i in range(len(coinFlip)):
        if i==0:
            pass
        elif coinFlip[i]==coinFlip[i-1]:
            streak+=1
            

        if streak==6:
            numberOfStreaks+=1
    coinFlip=[]

print('Chance of streak: %s%%' % (numberOfStreaks / (100)))
