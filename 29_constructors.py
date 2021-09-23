print()

# A constructor is a function that gets called at the time 
# of creating an object 

# Define the class 
class Point :

    # THIS IS THE CONSTRUCTOR 
    def __init__(self, x, y) :
        # Reference to current object
        self.x = x 
        self.y = y

    # Define a function within the class
    def move(self) : 
        # Things the function will do 
        print("move")

    def draw(self) :
        print("draw")

point = Point(10, 20)
print(point.x)

##################################################################

class Person :
    def __init__(self, name) :
        self.name = name
    def talk(self) :
        print(f"Hi I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()
