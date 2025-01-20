"""
array is a container that holds multiple values of the same type.
var=array(type code[elements])
there are different type codes i.e i for signed int, c for character e.t.c
"""
from array import *
arr=array('i',[1,2,3,4])
print(type(arr))
print(arr)

"""
you can use slicing like in lists using indexing
"""
print(arr[0:3])

#arrayes can be used together with other conditional loops
for i in arr:
    print(i)
"""
we can manipulate the arrays that is, we can append,reverse, just add a . infront of the array
variable name and choose the needed choice from the list.
"""
arr.reverse()
print(arr)
arr.append(6)
print(arr)

"""
a short program to ask users to input array values to an array list..
"""
"""
from array import *
length=array('i',[])
x=int(input('enter the length of the array: '))
print("enter %d elements "%x)
for i in range(x):
    n=int(input())
    length.append(n)
print(length)
"""
"""
functions in python
functions is a set of code that performs some tasks.
def function_name(): 
    statements.
we start by defining a function using the def declaration.
"""
def welcome():
    print("good morning")
#the above function has no value unless it is called.
welcome() #calls the function by entering the name of the function.
def names():
    print("mercy","caro","peter")
names()

def add(a,b):
    total=a+b
    print(total ,  " ",  "is the sum")
add(10,20)
x=2
y=3
"""
add(x,y)
m=int(input("enter the value of the first number: "))
k=int(input("enter the value of the second number: "))
add(m,k)
"""
#to enable the function to take in unlimited values from the user.
print("multiple intakes.")
def total(*a):
    t=0
    for i in a:
        t= t + 1
        print("This is the total: ", t)
total(12,11)


"""
objects in python. objects are anything touchable.
class in python is a blueprint for similar objects. a class holds objects together.
i.e. person <class>
          features;
                  name
                  gender
                  age
"""
class Person:
    def __init__(self):
        self.name="Clinton"
        self.gender="Male"
        self.age=23

    def talk(self):
        print("Hello, my name is : ", self.name)
    def vote(self):
        if self.age>=18:
            print("I can vote")
        else:
            print("I am not eligible to vote")
    def gender(self):
        if self.gender!="Male":
            print("Go back to the kitchen")
        else:
            print("Be like a Marine, we live no one behind.")
obj= Person()
Person.talk(obj)
Person.vote(obj)
Person.gender(obj)

class Data:
    def __init__(self,x,y,z):
        self.name=x
        self.gender=y
        self.age=z

    def introduction(self):
        print("My name is",self.name," I am from Kenya")
    def duties(self):
        if self.gender!="Male":
            print("I am a woman")
        else:
            print("I am a man")
    def fight(self):
        if self.age>=18:
            print("I can enroll in the army")
        else:
            print("I am a still a child.")
obj1 = Data("Jacob","Male",22)
obj2 = Data("Mercy","Female",17)
Data.introduction(obj1)
Data.duties(obj1)
Data.fight(obj1)
Data.introduction(obj2)
Data.duties(obj2)
Data.fight(obj2)

"""
An object has:
            attributes: data describing the object.
            behaviour: Methods on the attributes.
inheritance is a mechanism for a new class to use the features of another class.

to be continued.........................
"""













