print()

# This is used for storing information in key value pairs. 

# Dictionary is denoted as a {}
customer = {
    "Name": "Sunny Seera",
    "Email" : "sunnyseera@test.com",
    "Age" : 30,
    "is_verified" : True,
    "Phone": "10101010"
}
print(customer)

# Print a value in the dictionary
print(customer["Name"])

# This will allow searching for a value that does not exist 
print(customer.get("name")) 
# This will allow searching for a value that does not exist + Give a default value
print(customer.get("name", "The value is Name and not name")) 

# Change a value in the dictionary
customer["Name"] = "Jack Smith"
print(customer["Name"])

##################################################################################
print()

# Program to convert numbers into words

phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output = ""

for char in phone:
    output += digits_mapping.get(char, "!") + " "
    print(output)
