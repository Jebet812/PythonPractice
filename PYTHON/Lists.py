print("Lists")

def Simplelist():
    print("\na simple list")
    fruits = ['mangoes', 'oranges', 'bananas', 'apples']
    print(fruits)
    
Simplelist()

def Elementsinalist():
    print("\nAccessing elements in a List")
    fruits = ['mangoes', 'oranges', 'bananas', 'apples']
    print (fruits[1].title())
    
Elementsinalist()

def Indexingpositions():
    print("\nAccesing the last item on the list")
    fruits = ['Mangoes', 'Oranges', 'Bananas', 'Apples']
    print(fruits[-1])
    
Indexingpositions()

def Individualvalues():
    print("\nUsing individual values on a list")
    fruits = ['Mangoes', 'Oranges', 'Bananas', 'Apples']
    print( "My favourite fruit is"  +  " " + fruits[-1].title() + ".")
    
Individualvalues()


print("Changing, Adding and Removing Elements")

def Modifyelementsinalist():
    print("\nModifying Elements in a List")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    colours[0] = 'Brown'
    print(colours)
    
Modifyelementsinalist()

def Addingelementsinalist():
    print("\nAdding Elements in a List using append")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    colours.append('Brown')
    print(colours)
    
Addingelementsinalist()

def Addingelementsinanemptylist():
    print("\nAdding Elements in an empty List using append")
    colours = []
    print(colours)
    
    colours.append('Pink')
    colours.append('Yellow')
    print(colours)
    
Addingelementsinanemptylist()

def Addingelementsinalistusinginsert():
    print("\nAdding Elements in a List using insert")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    colours.insert(1, 'Pink' )
    print(colours)
    
Addingelementsinalistusinginsert()

def Removingelementsinalist():
    print("\nModifying Elements in a List")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    colours[0] = 'Brown'
    print(colours)
    
Modifyelementsinalist()