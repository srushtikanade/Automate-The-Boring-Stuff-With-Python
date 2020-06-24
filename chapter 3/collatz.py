
def collatz(number):
    stepsTaken=0
    if number<0:
        print('Please enter positive integer; greater than 1')
    elif number>1:
        while number!=1:
            
            if number %2==0:
                
                number=number//2
                print(number)
                stepsTaken+=1
            else:
                number=3*number+1
                print(number)
                stepsTaken+=1
        print('The collatz sequence is teriffic! Collatz for number '+ str(mynumber) +' took '+str(stepsTaken)+' steps to reach 1')
        
            
           
        

mynumber=int(input('Enter a positive integer you want to run collatz function on :'))
collatz(mynumber)

