#Functions are named blocks of code designed to do one spedcific job.
 
def greet_user(username):
     print("\nPassing information to a function")
     print("Hello "  + username.title() + (", welcome to your first day of work!"))
     
greet_user('jane')

#In this function username is the parameter (piece of information needed by a function 
# to do its job) and 'jane' is the argument(piece of information passed from a function call
# to a function)


print("Passing Arguments")

def describe_friend(name, colour):
    print("\nPositional Arguments")
    print ("My best friend's name is " + name.title())
    print (name.title() + "'s favorite colour is "  + colour)
    
describe_friend('Adhiambo', 'beige')


def describe_friend(name, colour):
    print("\nKeyword Arguments")
    print ("My best friend's name is " + name.title())
    print (name.title() + "'s favorite colour is "  + colour)
    
describe_friend(colour = 'beige', name = 'Adhiambo')

def describe_friend(colour, name = 'Adhiambo'):
    print("\nDefault Value")
    print ("My best friend's name is " + name.title())
    print (name.title() + "'s favorite colour is "  + colour)
    
describe_friend(colour = 'beige')

print("\nReturn Values")

def real_name(first_name, last_name):
    print("\nReturning a Simple Value")
    full_name = first_name +' ' + last_name
    return full_name.title()

doctor = real_name('Jason', 'Kim')
print(doctor)


def real_name(first_name, last_name, middle_name= ' '):
    print("\nMaking an Argument Optional")
    if middle_name:
        full_name = first_name +' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name   
    return full_name.title()

doctor_one = real_name('Jason', 'Kim')
print(doctor_one)
doctor_two = real_name('Joslyn', 'Alex', 'Daizy')
print(doctor_two)

print("Returning a dictionary")
def real_name(first_name, last_name, age = ' '):
     print("\nReturning a Dictionary")
     name = {'first' : first_name, 'last' : last_name}
     if age:
         name['age'] = age
     return name
     
client = real_name('Justin', 'Tray', age = 27 )
print(client)

print("\nPrint Function with a while Loop")
def name(first_name, last_name):
   full_name = first_name +' ' + last_name
   return full_name.title()

while True:
        print("\nKindly let me know your first name?")
        print("(enter q' to quit)")
        
        f_name = input("First name: ")
        if f_name == 'q':
            break
         
        l_name = input("Last name: ")
        if l_name == 'q':
            break   
        

        real_name = name(f_name, l_name)
        print("\nHello, " + real_name + " !")


print ("\nPassing a List")
def available_colours(colours):
    for colour in colours:
        write = "Hello, " + colour +" really looks good on you!"
        print(write)
        
available_colours (['Blue', 'Orange', 'Green'])


pri

