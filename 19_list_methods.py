print()

numbers = [5,7,1,2.4]

numbers.append(13)   # Add Number to END of list 
print(numbers)

numbers.insert(3, 20) # Add number at the 3rd index of a list 
print(numbers)

numbers.remove(7) # Remove number 7 from the list
print(numbers)

numbers.clear() # Remmove list 
print(numbers)

numbers = [5,7,1,2,5,5,4]
print(50 in numbers)   # Check if the number is in the list - returns a boolean 

print(numbers.count(5)) # Count how many times 5 appears in the lust 

numbers.sort() # sort list 
print(numbers)

numbers.sort() # sort list in decending
numbers.reverse()
print(numbers)

numbers2 = numbers.copy() # Make a copy of the list
print(numbers2)

###########################################################################################

# Check for duplicates in a list

numbers = [5,7,1,2,5,5,4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)