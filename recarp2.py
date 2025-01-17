"""
list is a collection of items in a particular order.
it can contain strings, ints or a mix of both in [] separated by commas.

"""
cars=["mercedes","audi","toyota","ghost","ferrari", "hatchbacks", "sedans", "SUVs", "coupes", "convertibles","pickup trucks"]
print(type(cars))
print(cars)

"""
accessing individual items in a list.
the first item in a list is at index zero. while the last item is accessed at index -1.

"""
print(cars[0])
#you can also print a range of items i.e.,
print(cars[0:3])
#using individual items of a list
print("I am not sure there is a car known as ",cars[3].title())

"""
working with lists. looping through entire lists.
the concept of looping is important because it’s one of the most common 
ways a computer automates repetitive tasks

"""
for i in cars:
    print(i.title() + ",are is a nice rides.")
    print("I have always wanted to own a ",i.title() + ".\n") #this repeats the statement a number of times equal to the number of cars

"""
making numerical lists. using the range parameter
"""
number_list=list(range(1,5))
print(number_list)
#print a list of even numbers from 100 to 1000
even_list=list(range(100,1001,2))
print(even_list)

#x=int(input("enter the value of the first integer"))
#y=int(input("enter the value of the second integer"))
squares=[]
for value in range(12,20):
    square=value**2
    squares.append(square)
print(squares)

"""
looping through a loop
"""
print("here are the 3 best cars: ")
for i in cars[:3]:
    print(i.title())

"""
Tuples- don't change through the program.
()
"""
names=("mercy","Caro","Jecks","peter","Joan")
print(type(names))

for i in names:
    print(i)

"""
IF STATEMENTS.
"""
print("THE IF STATEMENT")
cars=["mercedes","audi","toyota","ghost","ferrari", "hatchbacks", "sedans", "SUVs", "coupes", "convertibles","pickup trucks"]

for car in cars:
    if car=="audi":
        print(car.upper() + ", THIS IS WHAT I LOVE")
    else:
        print(car.title())
"""
EXAMPLE 2 
if-else statements.
"""
x=100
if x>=1000:
    print("x is lager than 1000")
else:
    print("x is smaller than 1000")
