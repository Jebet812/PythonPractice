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
    print("\nLooping through all the Keys in a dictionary")
    favourite_car = {
        'Jay' : 'benz',
        'Jane': 'bmw',
        'Jason' : 'audi',
        'Jasmine' : 'Honda'
    }
    friends = ['Jasmine', 'Jay']
    for name in favourite_car.keys():
        print(name.title())
        
        if name in friends:
            print("Hi" + " " + name.title() +
                  ", you really would love to own a" + " " +
                  favourite_car[name].title())
            
loopingthroughkeys()
    
def loopingthroughkeysinorder() :
    print("\nLooping through Keys in Order")
    favourite_car = {
        'Jay' : 'benz',
        'Jane': 'bmw',
        'Jason' : 'audi',
        'Jasmine' : 'Honda'
    }
    for name in sorted(favourite_car.keys()):
        print(name.title() + " " +"good luck saving to purchase the car!")
        
loopingthroughkeysinorder()
        
def loopingthroughvalues():
    favourite_car = {
        'Jay' : 'benz',
        'Jane': 'bmw',
        'Jason' : 'audi',
        'Jasmine' : 'Honda',
        'Jared' : 'audi'
    }
    print("The students mentioned the following cars as favourites:")
    for car in set(favourite_car.values()):
        print(car.title())
               
#To avoid repetition use set to mention value only once        
        
loopingthroughvalues()
    
    
print("Nesting")
#Nesting is when you want to store a set of dictionaries in a list or a list of items as a value
#in a dictionary.

def alistofdictionaries():
    print("\nA list of dictionaries")
    girls = []
    
    for girl_number in range (30):
        new_girl = {'hair' : 'ginger', 'height' : 'tall', 'eyes' : 'brown'}
        girls.append(new_girl)
    
    for girl in girls[0:3]:
        if girl['hair'] == 'ginger':
            girl['hair'] = 'brown'
            girl['height'] = 'short'
            girl['eyes'] = 'blue'
            
    for girl in girls[0:5]:
        print(girl)
                
    print("...")
    
    print("Total number of girls:" + str(len(girls)))
    
    
alistofdictionaries()

def alistindictionary():
    print("\nA List in dictionary")
    favourite_car = {
        'Jay' : ['benz', 'honda'],
        'Jane': ['bmw'],
        'Jason' : ['audi', 'toyota'],
        'Jasmine' : ['Honda', 'suzuki'],    
    }
    
    for name, cars in favourite_car.items():
        print("\n" + name.title() + " " + "loves these cars:")
        for car in cars:
            print("\t" + car.title())
            
alistindictionary()

def adictionaryindictionary():
    print("\nA Dictionary in a Dictionary")
    boys = {
        'James': {
            'first' : 'Arnold',
            'last' : 'James',
            'Age' : 'six',
            
        },
         'Ingrid':{
            'first' : 'John',
            'last' : 'Ingrid',
            'Age' : 'fifteen',
            
        },
          'Trevor':{
            'first' : 'Bill',
            'last' : 'Trevor',
            'Age' : 'twenty',
            
        },
        
    }
    
    for name, information in boys.items():
        print("\nBoy:" + name)
        full_name = information['first'] + " " + information['last']
        age = information['Age']
        
        print("\tFull name: "  + full_name.title())
        print("\tAge:" + age.title())
        
adictionaryindictionary()
    
    
    
        
   