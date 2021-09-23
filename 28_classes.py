print()

# Use Classes to define new types 


# Define the class 
class Point :
    # Define a function within the class
    def move(self) : 
        # Things the function will do 
        print("move")
    def draw(self) :
        print("draw")

# Creates a new object of our class 
point1 = Point()

# We can now use the functions that we created within out class! 
point1.draw()

# More Advanced Usage
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 30
print(point2.x)
point2.draw()