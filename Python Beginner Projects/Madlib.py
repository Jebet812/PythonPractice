# The project helps one familiarize themselves with working with f strings, 
# the input() function and general string concatenation in Python.

name= input('Name: ')
colour = input("Colour: ")
store = input("Store: ")
price = input("Price: ")

madlib = f"My name is {name}. I tend to wear dresses that are colour {colour}.\
I buy most of my dresses in  {store}. The prices cost around {price} dollars"

print(madlib)
    