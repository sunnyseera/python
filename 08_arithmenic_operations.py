print()

print(10+3)
print(10-3)
print(10/3)
print(10//3)
print(10 % 3)  # modulus 
print(10 ** 3) # 10 to the power 3

x = 10
x = x + 3
print(x)
x = 10
x += 3  # Exact same as the line above but is using augmentative assignment
print(x)

x = 10 + 3 * 2
print(x) # Python will do multiplication first so the result is 16

# Math Functions 
print()
print()

x = 2.9 
print(round(x)) # Rounds the number 
print(abs(-29)) # Gives you positive number

print()
print()
#########################################################
#  Using the MATH LIBRARY 
print()
print()

import math

# https://docs.python.org/3/library/math.html
# Documentation for the module

x = 2.9 
print(math.ceil(2.9))   # Round UP using the MATH Library
print(math.floor(2.9))  # Round DOWN using the MATH Library