print()

names = ['sunny', 'singh', 'seera']

print(names)
print(names[1])
print(names[-1])
print(names[2:])
print(names[0:2])

# Modify an element in a list 
names[2] = 'SINGH'
print(names)

# Find largest number in list
numbers = [3, 5 ,78, 35,2,4,4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

