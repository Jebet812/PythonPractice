def Simpleloop():
    print("\nSimple Loop using for loop")
    girls = ['Joyce', 'Brian', 'Colette']
    for girl in girls:
        print(girl.title() + " " + "you are beautiful" +  ".")
    
Simpleloop()

def Insideloop():
    print("\nInside Loop")
    girls = ['Joyce', 'Brian', 'Colette']
    for girl in girls:
        print(girl.title() + " " + "you are beautiful" +  ".")
        print("What is your favourite hobby" " " + girl.title() + "?\n")
        
    print("Thank you girls. You all have amazing hobbies")        
        
Insideloop()

def MakingNurmeriacallists():
    print("\nUsing range() Function in Numerical Lists")
    for value in range (1,8):
        print(value)
        
MakingNurmeriacallists()

def Usingrangetomakealist():
    print("\nUsing range() to make a list of numbers")
    numbers = list(range(1,8))
    print(numbers)
    
    print("\nPrint odd numbers")
    odd_numbers = list(range(1,15,2))
    print(odd_numbers)
    
    print("\nSquares")
    squares = []
    for value in range(10,20):
        square = value**2
        squares.append(square)
    print(squares)
    
    print("\nSimple for square")
    squares = []
    for value in range(10,20):
        squares.append(value**2)
    print(squares)
    
Usingrangetomakealist()

def Statistics():
    print("\nMax")
    numbers = [2, 9, 16, 0, 23, 6, 3]
    value = max(numbers)
    print(value)
    
    print("\nMin")
    numbers = [2, 9, 16, 0, 23, 6, 3]
    value = min(numbers)
    print(value)
    
    
    print("\nSum")
    numbers = [2, 9, 16, 0, 23, 6, 3]
    value = sum(numbers)
    print(value)

    
Statistics()