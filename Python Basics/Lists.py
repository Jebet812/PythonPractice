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

def Removingelementsinalistwithdel():
    print("\nRemoving Item Using the del statement")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    del colours[0]
    print(colours)
    
Removingelementsinalistwithdel()

def Removingelementsinalistwithpopmethod ():
    print("\nRemoving Item Using the pop () method")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    popped_colours = colours.pop()
    print(colours)
    print(popped_colours)
    
Removingelementsinalistwithpopmethod()

def Removingelementsinanypositiononlistwithpopmethod ():
    print("\nRemoving Item Using the pop () method in any position in a list")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    favourite_colour = colours.pop(2)
    print("My favourite colour of all time is" +" " +  favourite_colour + ".")

    
Removingelementsinanypositiononlistwithpopmethod()

def Removinganitembyvalue ():
    print("\nRemovinganitembyvalue")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    colours.remove('Green')
    print(colours)
    
    
Removinganitembyvalue()



print("Organizing a List")

def Sortingalistpermanently():
    print("\nSorting a list permanently with sort() method in alphabetical order")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    colours.sort()
    print(colours)
    
    print("\nSorting a list permanently with sort() method in reverse alphabetical order")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    colours.sort(reverse=True)
    print(colours)
    
Sortingalistpermanently()
    
def Sortingalisttemporarily():
    print("\nSorting a list temporarily with sorted() method")
    print("Original list")
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    print("\nThe sorted list in alphabetical order")
    print(sorted(colours))
    
    print("\nThe sorted list in reverse alphabetical order")
    print(sorted(colours, reverse=True))
    print("\nThe original list again")
    print(colours)
    
Sortingalisttemporarily() 

def Reverseorderofalist():
    colours = ['Red', 'Purple', 'Green', 'Orange']
    print(colours)
    
    colours.reverse()
    print(colours)

Reverseorderofalist()

def Findingthelengthofalist():
    print("\nFinding the length of a list")
    colours = ['Red', 'Purple', 'Green', 'Orange', 'Yellow', 'Maroon']
    len(colours)
    
Findingthelengthofalist()
