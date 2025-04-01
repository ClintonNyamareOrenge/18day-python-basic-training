import math
#EXERCISE 1, calculate the area of a rectangle:

length= float(input("Enter the length of the rectangle: "))
width= float(input("Enter the width of the rectangle: "))
area=length*width
print(f"the area of the rectangle is {area}")

#EXERCISE 2 the circumference of a circle o.5*pi*r**2

radius=float(input("Enter the radius of the circle: "))
circumference= math.pi*radius*2
print(f"the circumference of the circle is {circumference}cm2")

#Exercise 3 find the hypotenuse of a triangle.

height= float(input("Enter the height of the triangle: "))
length= float(input("Enter the length of the triangle: "))
hypotenuse= math.sqrt((pow(height, 2)+pow(length,2)))
print(f"the hypotenuse is {hypotenuse}")


