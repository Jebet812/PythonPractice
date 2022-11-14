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
    fruit = 'Watermelon'
    fruit == 'Watermelon'
    bool(fruit)
    
    fruit = 'Watermelon'
    fruit == 'Orange'
    bool(fruit)
    
conditionaltests()