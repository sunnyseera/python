print()

# Inheritance is a mechanism for reusing code 

# THIS IS THE PARENT CLASS
class Mammal: 
    def walk(self) :
        print("walk")

# The dog class will inherit all functions from the mammal class  
class Dog(Mammal) :
    def bark(self) :
        print("Woof!")

# The cat class will inherit all functions from the mammal class  
class Cat(Mammal) :
    pass # We are using pass to say that the mammal class gives us everything we need 

# Call and run the methods  
cat1 = Cat()  # This creates the cat object
cat1.walk()   # Call the methods

dog1 = Dog()
dog1.bark()