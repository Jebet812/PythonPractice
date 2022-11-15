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
    