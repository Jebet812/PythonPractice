# Classes

class Babies():
    """A simple model for babies"""
    
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        
    def cry(self):
        """Simulate a baby sitting on command"""
        print(self.name.title() + " is crying now.")
        
    def laugh(self):
        """Simulate a baby sitting on command"""
        print(self.name.title() + " is laughing now.")
        

print("\nMaking an Instance from a Class")
 
class Baby():
    
     def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        
my_baby = Baby('Sandra', 2)
print("My baby's name is " + my_baby.name.title())
print(my_baby.name.title() + " is " + str(my_baby.age) + " years old")
    
print("\nCalling Methods")

class House():
    # Building a House
    
    def __init__(self, door, window, stair):
        # Initialize attributes of building a house
        self.door = door
        self.window = window
        self.stair = stair
        
    def get_a_house(self):
        # Return a descriptive house
        requirements = self.door + ', a '+ self.window + ' and a ' + self.stair
        return requirements
    
my_house = House('Panel door', 'Casement window', 'Spiral staircase')
print ("My new house will be made of a " + my_house.get_a_house())
        
        
print("\nSetting a Default Value for an Attribute")  

class House():
    # Building a House
    
    def __init__(self, door, window, stair):
        # Initialize attributes of building a house
        self.door = door
        self.window = window
        self.stair = stair
        self.floor = 2
        
    def get_a_house(self):
        # Return a descriptive house in the method
        requirements = self.door + ', a '+ self.window + ' and a ' + self.stair
        return requirements
    
    def floors(self):
        print("I only want " + str(self.floor) + " floors in the house.")
        
    
my_house = House('Panel door', 'Casement window', 'Spiral staircase')
print ("My new house will be made of a " + my_house.get_a_house())

my_house.floors()    

print("\nModifying Attribute Values")
 
print("\nModifying an attributes vakue directly")   
 
class House():
    # Building a House
    
    def __init__(self, door, window, stair):
        # Initialize attributes of building a house
        self.door = door
        self.window = window
        self.stair = stair
        self.floor = 2
        
    def get_a_house(self):
        # Return a descriptive house in the method
        requirements = self.door + ', a '+ self.window + ' and a ' + self.stair
        return requirements
    
    def floors(self):
        print("I only want " + str(self.floor) + " floors in the house.")
        
    
my_house = House('Panel door', 'Casement window', 'Spiral staircase')
print ("My new house will be made of a " + my_house.get_a_house())

my_house.floor = 3
my_house.floors()   

print("\nModifying an Attribute's Value Through a Method")

class House():
    # Building a House
    
    def __init__(self, door, window, stair):
        # Initialize attributes of building a house
        self.door = door
        self.window = window
        self.stair = stair
        self.floor = 2
        
    def get_a_house(self):
        # Return a descriptive house in the method
        requirements = self.door + ', a '+ self.window + ' and a ' + self.stair
        return requirements
    
    def floors(self):
        print("I only want " + str(self.floor) + " floors in the house.")
        
    
    def update_floors(self, story):
        self.floor = story
        
          
my_house = House('Panel door', 'Casement window', 'Spiral staircase')
print ("My new house will be made of a " + my_house.get_a_house())

my_house.update_floors(4)
my_house.floors()

print("\nIncrementing an Attribute's Value Through a Method")

class House():
    # Building a House
    
    def __init__(self, door, window, stair):
        # Initialize attributes of building a house
        self.door = door
        self.window = window
        self.stair = stair
        self.floor = 2
        
    def get_a_house(self):
        # Return a descriptive house in the method
        requirements = self.door + ', a '+ self.window + ' and a ' + self.stair
        return requirements
    
    def floors(self):
        print("I only want " + str(self.floor) + " floors in the house.")
        
    
    def update_floors(self, story):
        self.floor = story
        
    def add_stairs (self, another_stair):
        self.stair += another_stair
        print("The stair I am adding is")   
        
          
my_house = House('Panel door', 'Casement window', 'Spiral staircase')
print ("My new house will be made of a " + my_house.get_a_house())

my_house.update_floors(4)
my_house.floors()

my_house.add_stairs(2)
my_house.stair()


