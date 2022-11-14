# If statements allows you examine the current state of a program and respond appropriately to the state.

def asimpleifstatement():
    print("\nA simple if statement")
    cars = ['toyota', 'mazda', 'benz', 'bmw']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())

asimpleifstatement()


print("\nConditional Tests")
#An expression that can be evaluated as *true* or false is a *conditional test

def  conditionaltests():
    print("\nCheck for Equality")
    fruit = 'Orange'
    if fruit == 'Watermelon':
        print('Watermelon')
    else:
        print('Not Watermelon')
    
       
conditionaltests()


def  ignoringcase():
    print("\nIgnoring case when Checking for equality")
    fruit = 'Watermelon'
    fruit.lower() == 'watermelon'
    print('Watermelon')
        
ignoringcase()

def checkinginequality():
    print("\nChecking for Inequality")
    dress = 'red'
    if dress != 'pink':
        print("Return dress to Zara")
        
checkinginequality()

def numericalcomparisons():
    print("\nNumerical Comparisons")
    size = 16
    if size != 16: 
        print("Deliver it to Nairobi.")
    else:
        print("Return the dress to Zara.")
        
numericalcomparisons()

print("\nChecking multiple conditions")

def checkingmultipleconditions():
    print("\nUsing and to check multiple conditions")
    size_1 =  16
    size_2 = 10
    if size_1 >= 16 and size_2 <= 9:
        print (True)
    else:
        print(False)
        
    print("\nUsing or to check multiple conditions")
    size_1 =  16
    size_2 = 10
    if size_1 >= 16 or size_2 <= 9:
        print (True)
    else:
        print(False)
        
checkingmultipleconditions()



    
    
def checkingwhetheravalueisinalist()      :
    print("\nChecking Whether a Value is in a List")
    bought_shoes =  ['Heels', 'Loafers', 'Sneakers']
    if 'Sneakers' in bought_shoes:
        print (True)
    else:
        print(False)
        
        
    bought_shoes =  ['Heels', 'Loafers', 'Sneakers']
    if 'Sandals' in bought_shoes:
        print (True)
    else:
        print(False)
    
checkingwhetheravalueisinalist()  

print("\nBoolean Expressions")   
#A *Boolean value is either a *True* or *False* 

print("\nif Statements")
#Already covered a simple if statement, if-else statement.

#Python uses if-elif-else syntax to run each conditional test in order until one passes

def ifelifelse():
    print("\nThe if-elif-else chain")
    age = 25
    if  age < 6:
        print("You wear a size 0")
    elif age < 16:
        print("You wear a size 6-12")
    else :
        print("You might have to visit the store to be measured")

ifelifelse()

def multipleelifblocks():
    print("\nUsing Multiple elif Blocks")
    age = 25
    if  age < 6:
        print("You wear a size 0")
    elif age < 16:
        print("You wear a size 6-12")
    elif age < 25:
        print("You wear a size 12-18")
    else :
        print("You might have to visit the store to be measured")
    
multipleelifblocks()

def omittingelseblock():
    print("\nOmmiting the Else Block")
    age = 70
    if  age < 6:
        print("You wear a size 0")
    elif age < 16:
        print("You wear a size 6-12")
    elif age < 25:
        print("You wear a size 12-18")
    elif age >= 25:
        print("You might have to visit the store to be measured")

omittingelseblock()

def testingmultipleconditions():
    print("\nTesting Multiple Conditions")
    bought_snacks = ['chocolate', 'icecream', 'pizza']
    if 'chocolate' in bought_snacks:
        print("Add chocolate.")
    if 'icecream' in bought_snacks:
        print("Add icecream.")
    if 'pizza' in bought_snacks:
        print("Add pizza.")
        
    print("\nProceed to cart")

testingmultipleconditions()

print("\nUsing if Statements with Lists")

def checkingforspecialitems():
    print("\nChecking for Special Items")
    dress_colours = ['red', 'purple', 'brown']
    for dress_colour in dress_colours:
        if dress_colour == 'brown':
            print("The brown dress is unavailable. Can you choose another colour?")
        else:
            print("Adding" + " " +dress_colour + " "+ "dress to cart.")
        
checkingforspecialitems()


def checkingthatalistisnotempty():
    print("\nChecking thata list is not empty")
    dress_colours = ['red', 'purple', 'brown']
    if dress_colours:
        for dress_colour in dress_colours:
            print("Adding" + " " +dress_colour + " "+ "dress to cart.")
    else:
        print("There are no dresses in that colour.")
        
checkingthatalistisnotempty()


def usingmultiplelists():
    print("\nUsing Multiple Lists")
    dress_colours_available = ['red', 'purple', 'brown', 'green', 'orange', 'blue']
    dress_colours =  [ 'green', 'orange', 'blue', 'maroon']
    for dress_colour in dress_colours:
        if dress_colour in dress_colours_available:
            print("Adding" + " " +dress_colour + " "+ "dress to cart.")
        else:
            print("There are no dresses in that colour.")
        
usingmultiplelists() 