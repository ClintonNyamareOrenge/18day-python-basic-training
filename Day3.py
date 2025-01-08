"""
today we will learn about python is, else statements
it deals with conditions, they can be either true, if the condition parameter
are met or false if the condition parameters are not met.
it is executed in a block
example; to check if a number is greater than fifty.
"""
num=24
if num<50:
    print('True')
else:
    print('False')
#True
"""
example two; 
ask a user an input and check if it is even or odd;
"""
number=float(input("enter your number: "))
if number%2 ==0:
    print('the number is an even. ')
else:
    print('the number is odd. ')
"""
Nested if, it is where an if statement is inside anm if statement.
example;
"""
year=int(input("enter the year you were born: "))
if year>=2001:
    age=(2025-year)
    print("you are a Genz.", age,"of age")
    if year<=2000:
        print("go and breastfeed don't join the riots: ")
    else:
        print("see you occupy parliament")
else:
    print("Go sleep old soul! ")
"""
you can use elif if the statements are too many, in this i will try to code
a simple program to enable school teachers give out grades;
"""
maths=float(input("Enter the marks scored in mathematics: "))
english=float(input("Enter the marks scored in English: "))
kiswa=float(input("Enter the marks scored in kiswahili: "))
science=float(input("Enter the marks scored in science: "))
social=float(input("Enter the marks scored in Social: "))

average=(maths+english+kiswa+science+social)/5

if average>80:
    print("Congratulation for exemplary results!", average,'points')
elif average>=70:
    print("first class, proceed to the next class: ", average,'points')
elif average>=60:
    print("second class upper, proceed to the next class: ", average,'points')
elif average>=50:
    print("second class lower, proceed to the next class: ", average,'points')
elif average>=30:
    print("pass, proceed to the next class, but repeat the failed units: ", average,'points')
else:
    print("Fail repeat the class: ")

"""
loops, this enable us to do a certain task a number of time 
util a certain objective is reached.
this helps us save time.
there are 3 types of loops, the for, while and nested loops.
"""
#while loop
x=10
while x<20:
    print("You are a legend")
    x=x+1
else:
    print("try again someday")

# a simple program to ask for a password until the correct password is given
password1=float(input("Please enter your password you will wish to use in this exercise: "))
print('note that enter the password you used above.')

password=float(input("Please enter your password: "))
while password!=password1:
    print("Your password incorrect please try again: ")
    password = float(input("Please enter your password again: "))
else:
    print("CONGRATULATION  you did it: ")

"""
For loop it is used to iterate over a sequence(a list,tuple or a string)
it has a counter that keeps track of where you are in a sequence
syntax for "counter" in "sequence":
            statement:
        else:
"""
x=[13,12,13,24]
for i in x:
    print(i)
#it prints the content in the list. the same will be done on the string.
"""
nested loops, this are loops inside loops
it can be a for loop inside a for loop, a while loop inside a while loop, a for in a while loop
or a while loop inside na for loop.
"""
x=[('A','B','C'),(1,2,3)]
for i in x:  #for the first part of the list
    for g in x:  #for the second part of the list
        print(g, end=" ") #to remove a new line
    print(x, end=" ")

"""
to break the loop after a certain condition has been made you use break function.
example;
"""
w="A code a day keeps . your mind from alcohol"
for i in w:
    if i == "." : # as soon as the codes get a . it stops executing
        break
    print(i)
w=2,3,5,66,4,3,2,2,4,5,56
for i in w:
    if i == 4 : # as soon as the codes get a 4 it stops executing
        break
    print(i)
"""
if you dont want to break from the loop after a certain condition is meet 
you can use the continue.
it skips the statement following it and returns control to the beginning of the loop.
"""
ox=(1,1,23,34,5576,5643)
for i in ox:
    if i >34 :
        continue
    print(i)