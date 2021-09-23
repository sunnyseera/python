print()

# Pass in argurments to your function that your function expects
def greet_user(firstname, lastname) : 
    print()
    print(f"Hello {firstname} {lastname}!")
    print("Welcome ")
    print()


# You can actually just use a keyword argument to tell the function which parameter is for what variable
print("Start")
greet_user(lastname="John", firstname="Smith")     
print("Finish")
