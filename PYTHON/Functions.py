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

