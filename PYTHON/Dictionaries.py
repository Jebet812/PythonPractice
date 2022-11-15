#A dictionary is a collection of key-value pairs

def simpledictionary():
    print("\nA simple dictionary")
    girl_1 = {'eyes' : 'blue', 'hair' : 'ginger'}
    print(girl_1['eyes'])
    print(girl_1['hair'])
    
simpledictionary()

#Working with dictionaries

def accessvalue():
    print("\nAccesing values in a dictionary")
    girl_1 = {'eyes' : 'blue', 'hair' : 'ginger'}
    hair_colour = girl_1['hair']
    print("If girl's hair is" + " " + str(hair_colour) + " " +"she is beautiful.")
    
accessvalue()

def newkeyvaluepairs():
    print("\nAdding New Key-Value Pairs")
    girl_1 = {'eyes' : 'blue', 'hair' : 'ginger'}
    girl_1['height'] = 165
    girl_1['weight'] = 44
    print(girl_1)
    
newkeyvaluepairs()

def addtoempty():
    print("\nStarting with an Empty Dictionary")
    girl_1 = {} 
    girl_1['height'] = 165
    girl_1['weight'] = 44
    print(girl_1)
    
addtoempty()

def modifyvalues():
    print("\nModifying Values in a Dictionary")
    girl_1 = {'hair' : 'ginger'}
    print("The girl's hair colour is" + " " + girl_1['hair'])
    
    girl_1 = {'hair' : 'brown'}
    print("The girl's hair colour changed to" + " " + girl_1['hair'])
    
modifyvalues()

def removekeyvaluepairs():
    print("\nRemoving Key-Value Pairs")
    girl_1 = {'eyes' : 'blue', 'hair' : 'ginger'}
    del girl_1['hair']
    print(girl_1)
    
removekeyvaluepairs()
          
def similarobjects():
    print("\nA dictionary of similar objects")
    favourite_car = {
        'Jay' : 'Benz',
        'Jane': 'bmw',
        'Jason' : 'Audi'
    }
    print("Janes favourite car is a" + " " + 
          favourite_car['Jane'].upper())
    
similarobjects()

#Looping Through a Dictionary
def loopingthroughkeyvalue():
    print("\nLooping Through All Key-Value Pairs")
    favourite_car = {
        'Jay' : 'Benz',
        'Jane': 'bmw',
        'Jason' : 'Audi'
    }
    for name, car in favourite_car.items():
        print(car.title() + " " + "is" + " " +
              name.title() + "'s favourite car")
    
loopingthroughkeyvalue()

def loopingthroughkeys():
    print("\nLooping through allthe Keys in a dictionary")
    
