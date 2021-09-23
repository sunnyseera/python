print()

# Breaking up the code into multiple files 
# We use modules to better organise our code

# This is actually looking for a file in this folder called converters.py
import converters

# We can use the file to call its functions 
print(converters.lbs_to_kg(70))

#########################################################################################

# Import specific function from the modules 
from converters import lbs_to_kg

# We can then reference the module directly
print(lbs_to_kg(70))

#########################################################################################

