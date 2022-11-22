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


print("\nWorking with Part of a List")

def slicingalist():
    print("\nGenerate a subset of a list")
    boys = ['Charles', 'Michael', 'Timothy', 'Titus', 'Trevor']
    print(boys[2:4])
    

    print("\nGenerate a subset of a list ommiting first index")
    boys = ['Charles', 'Michael', 'Timothy', 'Titus', 'Trevor']
    print(boys[:4])
    
    print("\nGenerate a subset of a list ommiting last index")
    boys = ['Charles', 'Michael', 'Timothy', 'Titus', 'Trevor']
    print(boys[2:])
    
    
    print("\nGenerate the last 3 subset of a list")
    boys = ['Charles', 'Michael', 'Timothy', 'Titus', 'Trevor']
    print(boys[-3:])
    

slicingalist()

def loopingthroughalist():
    print("\nLooping through a list")
    boys = ['Charles', 'Michael', 'Timothy', 'Titus', 'Trevor']
    print("\nThese three boys scored top in math")
    for boy in boys[:3]:
        print(boy.title())
        
loopingthroughalist()


def copyingalist():
    print("\nCopying a List")
    snacks = ['Crackers', 'Crisps', 'Pizza']
    duez_snacks = snacks[:]
    
    snacks.append('Soda')
    duez_snacks.append('Ice cream')
    
    print("The snacks I carried are:")
    print(snacks)
    
    print("\nThe snacks my best friend carried are:")
    print(duez_snacks)
    
copyingalist()


print("\nTuples")

def Simpletuple():
    print("\nSimple Tuple")
    dimension = (100,20)
    print(dimension[0])
    print(dimension[1])
    
    
Simpletuple()


def Loopingintuple():
    print("\nLooping through All Values in Tuple")
    dimensions = (100,20)
    for dimension in dimensions:
         print(dimension)

Loopingintuple()

def Writingoveratuple():
    print("\nWriting over a Tuple")
    dimensions = (100,20)
    print("\nOriginal Dimensions")
    for dimension in dimensions:
         print(dimension)
         
     
    dimensions = (100,20)
    print("\nChanged Dimensions")
    for dimension in dimensions:
         print(dimension)  
         
Writingoveratuple()  