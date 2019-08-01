def countTon(num): 
    #num will be the absolute value of itself
    num = abs(num)
    for i in range(1,num+1):
        print i

'''
i=1
print i
i +=1
'''
def Factors (num) :
    num = abs (num)
    factors = [] #list()
    #This is a loop 
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)

    return factors

n = raw_input("Enter a number: ")
n = int(n)



print Factors(n) 