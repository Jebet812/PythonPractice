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
        
checkingmultipleconditions()
    
    
def checkingwhetheravalueisinalist()      :
    print("\nChecking Whether a Value is in a List")
    
        
    
 
    
    
    
    