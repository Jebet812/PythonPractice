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
    

     