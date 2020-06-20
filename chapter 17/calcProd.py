import time

def calcProduct(number):
    product=1
    for i in range(1,int(number)):
        product=product*i
    return product

startTime=time.time()
number=input('Calculate factorial of :')
prod=calcProduct(number)
endTime=time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

