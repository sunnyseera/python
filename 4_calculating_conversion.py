
print()

birth_year = input('Birth Year: ')  # Python treats this as a string variable
print(type(birth_year))             # Show the type of variable
 

age = 2021 - int(birth_year)        # Converts String to INT. 
print(type(age))

print(age)
print()

######################################################################################

print()
weight_in_lbs = input('What is the weight (lbs) : ')
weight_in_kgs = float(weight_in_lbs) * 0.45
print('Weight in kgs:', weight_in_kgs)