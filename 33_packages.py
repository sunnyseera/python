print()

# A package is a folder for multiple modules 

# Import the package
import ecommerce.shipping

#Utilise the package
ecommerce.shipping.calc_shipping()

##################################################################################

# We can just import the fucntion that we want to make is shorter 
from ecommerce.shipping import calc_shipping
calc_shipping()

##################################################################################

