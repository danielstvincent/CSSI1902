num = raw_input ("Enter a number: ")
num = int (num) #converts num to an int
#convert num to an int
num = int (num) 

if type(num) != type(int()):
    print "Not an interger"
elif num < 1 or num > 10:
    print "Out of Range"
elif num % 2 ==0:
    if num ==2: 
        print "Your number is prime"
    else:
        print "Your number is not prime"
else:
    if num == 3 or num == 5 or num ==7: 
        print "Your number is prime"
    else:
        print "Your number is not prime"

