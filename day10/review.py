"""how to define a function
'''you start by typing the 
keyword def followed by the 
name of the function and then 
parenthese with a list of
 paramenters separated by commas. 
 last you add a colon after the 
 close parenthesis and indent the next
 line for the body of he function'''

 def f(x):
     return 2*x+3
    print "The end of the funcation"

'''The above function is named f.
 It takes one paramenter which should 
 be a number. The function returns
twice the paramenter plus 3'''

'''Once aa funcion is defined, you can use 
it by calling it. To call a function, you must use 
the function's name followed by parentheses
with the arguments of the function enclosed in
them. arguments are literals, objects, expressions
or return-value finction calls that takes the
place the paramenters in the function definition.
the arguments are associated with the paramenter
in the same postion as them in. Hence, the first 
argument is associated with the first parameter,
and so on.Last, the number of arguments must match 
number of paramenter whenever default values are not provided.'''

#function call with a literal
print f(2) #return 7

#function call with an expression
print f(3+4*6) #return 57

#function call with a function call
print f(f(6)) #return 33

v=89
#function call with a variable
print f(v) #return 181

def Greater(x,y):
    if x >=y:
        return x
    else:
        return y

'''Task 1: Define a function that takes two 
paramenter. It retuens the greater of the
 two paramenters. Assume that the parmeters
 are numbers'''

x=float (raw_input)("Enter first nuber: "))
y=float(raw_input)("Enter second number: "))

print Greater (x,y)

'''Task 2: Define a function that takes no 
 paramenters. It prompts the user to enter a 
 string. Afterwards, it returns the string 
 concatenated with itself'''

 def Echo():
     msg= raw_input("Enter a string")
     return msg + msg

print Echo()

'''Take 3: Define a funcation that takes

three parameters. It displays the value
of three more than the product of the
paramenter.Assume that the paramnters are numbers'''

def Display3(first, second, third):
    v= x * y * Z + 3
    print value

Display3(2,3,4)

#list
'''What is a list?'''
'''A list is an ordeed collection of objects'''
''' You access the elements of  a list with an
index which is a interger between -n to n-1
where n is the length of the list. Negative 
indices access the list in reverse and 
nonnegative indices access the list is
order. For any nonnegative index i, its equivalent negative index is n-i where
n is the length of the list.'''




#creating a list
1 = []  #[] are called subscript operators.
#The above is an empty list

K= list() #another way of creating an empty list

j= [1,2,3,4,5,6,7,8,9,10] #a list with content

#list methods
print "nThe Original lists"
print "l =", l
print "k =", k
print "j =", j

l.remove ('a')
k.remove ('a')
j.remove (5,12)

print "The lists after clear is called on j"
print "l =", l
print "k =", k
print "j =", j

l.pop ()
k.pop ()
j.pop ()

print "\nThe index of 5 in each list"
#print '1 =", l.index (5)"
print "k =", k
print "j =", j

l = [2,3,6,7,8]
k = [4,1,5,12,13]

print "\nThe index of 5 in wach list"
#print "1 =" 1.index(5)
print "k =", k.index(5)
print"j +", J.index(5)

#Loops
#while loop
i=1
while i <= 10:
    print i
    i += 1 #1 + i % 1

#counting to 20 starting from 1 but only odd number
i=1
while i <=20:
    if i % 2 == 0:
        print i
    i += 1

v = ""
while v !="hello":
    v = raw_input("Enter a string: 


#for loop
#it is used for traversing sequences
for i in range(1,11):
    print if

for i in range(1,21):
    print i

for i in range(1,21,2):
    print i

for i in range(1,21,2):
    print i % == 1;

for i in range(1,21,):
    print i % 2 == 1:

for i in "This is a string":
    print i 

h = []

for i in range(20):
    h.append (0)

print h, len(h)



#object
'''What is a objct'''
'''An instance of a Class'''

class Person:
    def __inti__(self,name):
        self.name + name
        self.age + 0


    def birthday(self):
        self.age += 1
_______________________________________________________________________


#create objects
t= Person("Jane Doe") #Created a Person object

print t.name, t.age

s= Person("Roger")

print s.name, s.age

t.birthday()

print t.name, t.age



