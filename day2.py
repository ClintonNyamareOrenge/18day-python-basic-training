"""
today we will learn about string and dictionaries in python
lets start with strings;
a string can be a number or a series of words enclosed by a single or double quotes
note that when a sting has a quote in between its letters or number be sure to enclose it with a double quote
if it has a double quote then enclose it with a single quote.
example;
"""
word="clinton"
word1="clinton's ball is lost. "
word2='clinton said, "you will make it oneday" '
"""
you can write a multiple line string using a triple quotes either double or single 
"""
long_string=(''' a code a day keeps a bug away
you should learn the basics in order to become a pro one day
use free platforms to lear and build small projects ''')

#you can use the len attribute to find the length of a string.
print(len(long_string))
#you can also slice the strings just like in lists
print(long_string[0:100])
"""
to print each value of a string separately you can use a for loop, more on this later.
example
"""
y="Clinton Nyamare"
for i in y:
    print(i)
"""
remember if you replace i with y in the print statement the string will be printed a certain
number of times.
if you want all the characters to be printed on the same line use , end=" "
There are many ways to play with a string, lets say you want to print the characters in uppercase
just after the string name add a . and choose from a dropdown some may require additional information some don't example;
"""
f="keep in the good work soon you will see the efforts. "
print(f.upper())
print(f.isalnum())
print(f.find("i")) #will print the index of the value.
#there are a lot of options to choose from.

"""
to concatenate string you simply use + sign but this will be complicate when having multiple strings
example;
"""
str1="welcome"
str2="brother"
#to make them a single line use;
word3=(str1 + " " + str2)
print(word3)
str3="to my lovely course"
#when you have more than one string we use {} as placeholders and use .format method
result='{} {} {}'.format(str1, str2, str3)
print((result))


"""
Dictionaries 
is a unordered collection of data stored as a pair of key and value
syntax, var_name={key1:value1, key2:value2}
example;
"""
dic1={"name":"Clinton", "age":23, "profession":"student"}
print(dic1)
#we can also create a dictionary using the dict i.e;
dic2=dict({1:"name",2:"age",3:"profession"})
print(dic2)
#you can have nested dictionaries i.e;
dic3={"name":{1:"name",2:"age",3:"profession"}, "age":23, "profession":"student"}
print(dic3) #note that the key value is another dictionary
#you can add elements to a dictionary i.e;
dic3["addedKey"]={"addedvalue"}
print(dic3) #the added characters can be int or string.
 #to delete an element of a dictionary we use .pop(keyvalue)
dic3.pop("name")
print(dic3)
"""
there are a lot of methods that can be used with dictionaries. just type the name of the dictionary followed
by a . then chose from a drop down.
"""
print(dic3.items())


"""
play along with the different methods. see you tomorrow. 
"""