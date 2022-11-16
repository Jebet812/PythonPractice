
def prompts_with_inputfunction():
    print("\nWriting Prompts with the Input() Function")
    name = input("Kindly enter your name: ")
    print("Hi there, " + name + ". Welcome!")
    
prompts_with_inputfunction()

def int_for_numerical_output():
    print("\nUsing int() to accept Numerical Input")
    shoe_size = input("What shoe size do you wear?")
    shoe_size = int(shoe_size)
    type (shoe_size)
    
    if shoe_size <= 15:
        print("Welcome, your shoe size is available.")
    else:
        print("Sorry, your shoe size is unavailable.")
        
    
int_for_numerical_output()

def modulo_operator():
#This divides a number by another and returns the remainder.
    print("\nThe modulo Operator")
    number = input("Enter number to see whether it is odd or even:")
    number = int(number)
    
    if number % 2 == 0:
        print("Yay, this is an even number!") 
    else:
        print("Yay, you found an odd number!")
        
modulo_operator()

#While Loops
def while_loop():
    number = 2
    while number < 10:
        print(number)
        number += 2
        
    
while_loop()     

def using_flag():
    print("\nUsing a Flag")
    prompt = "How are you feeling?" 
    prompt += "\n(Enter 'tired' to go home.)" 
    
    strong = True
    while strong:
        message = input(prompt)
        
        if message == 'tired':
            strong = False
        else:
            print(message)
            
using_flag()
    
    
def using_break():
    print("\nUsing a Break")
    prompt = "What country do you want to visit:" 
    prompt += "\n(Enter 'quit' when done.)"
    
    
    while True:
        country = input(prompt)
        
        if country == 'quit':
            break
        else:
            print(country.title() + " is an amaizing place to visit!")
            
using_break()