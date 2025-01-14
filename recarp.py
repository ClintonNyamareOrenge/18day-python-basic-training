"""
strings.
characters enclosed in single or double quotes.
use of methods, a method is an action that python can perform on a piece of data.
"""
name = "clinton"
print(name.upper())  #to change case, use the variable name followed by a dot.
print(name.title())

"""
concatenating- this is combining strings using the + sign.
"""
first_name = "clinton"
last_name = "nyamare"
full_name = first_name + " " + last_name
print(full_name.title())

"""
lists- allow you to store a set of data in one place
       it is a collection of items in a particular order.
       use square brackets []. 
"""
my_classmates = ["denver", "alice", "brian", "zeky", "babu"]
print(my_classmates)

"""
accessing elements in a list by use of indexes.
the indexing starts from zero to n-1
example;
"""
print(my_classmates[0])  #print the first name in the list.
print(my_classmates[0:4])  #print the first name to the 3rd.
print(my_classmates[4].upper())  #you can manipulate how the item is written
print(my_classmates[-1])  #used to access the last item without need of knowing the number of items in the list.
print(my_classmates[::-1])  #print the list backwards.
#you can use individual names from a list i.e;
message = "I follow" + " " + my_classmates[0].upper() + " " + "on X and LinkedIn"
print(message)

"""
changing, adding and removing elements
lists are mutable/dynamic.
we will use the list my_classmates.
"""
#adding, we use insert or append.
#empty list.
cars=[]
cars.append('mark x')
cars.append('bugatti')
cars.append('lambo')
print(cars)

#let's change the name of the last value in the list
my_classmates[-1] = "Kanini"
print(my_classmates)
#let's add a new name to the list
my_classmates.append("musyoka")  #append adds the value to the end of the list
print(my_classmates)
my_classmates.insert(2, "joshua")  #to add a value to a specific position.
print(my_classmates)

#removing elements use del, pop, remove
del my_classmates[5]  #using indexing
print(my_classmates)

#sometimes you may want to use the value of an element after removing it.
#pop() element removes the value of the last element in a list but lets you work with the element after you have removed it
my_movies = ["the end is near", "panda", "dexter", "the moon"]
print(my_movies)
popped_movies = my_movies.pop()

print('the movie i liked most was ' + popped_movies.upper())
#you can pop individual items from specific places through indexing.
popped_movies2 = my_movies.pop(2)

print('the movie i hated was ' + popped_movies2.upper())
print(my_movies)
#sometimes you don't know the position of the value you want to remove but yoi know the value by name.
#you can use the remove() attribute.
#lets use my_movie list.
my_movies.remove('panda')
print(my_movies)

#organizing a list.
#you can sort a list permanently using the sort() method.
expensive_cars=['bmw','audi','subaru','toyota']
expensive_cars.sort()
print(expensive_cars)
#to sort temporary you can use the sorted() argument instead of sort()
numbers=[1,7,30,64,5]
print(numbers)
print(sorted(numbers))  #prints the sorted list
print(numbers)   #prints the original list

#printing the list in reverse, we can use .reverse
#changes the order of the list permanently.
numbers.reverse()
print(numbers)

