print()

# If you run this and instead of a number put a string
# the program will crash with a Value Error 

age = int(input('Age: '))
print(age)

##############################################################################

# By using a try and except block we can say that if we get 
# a value error then do something else and not crash the program

try: 
    age = int(input('Age: '))
    print(age)
except ValueError : 
    print("Error: Invalid Value, use a number.")

##############################################################################

# Advanced Example 

try: 
    age2 = int(input('Age: '))
    income = 20000
    risk = income / age2
    print(age2)
except ValueError : 
    print("Error: Invalid Value, use a number.")
except ZeroDivisionError : 
    print("Error: Invalid Value, use a positive number.")