print()

for x in range(4): 
    x = x + 1
    for y in range (3):
        y = y + 1 
        print(f'({x}, {y})')

#####################################################################

print()

numbers = [5, 2, 5, 2, 2] 

for item in numbers: 
    print('x' * item)
print()

#####################################################################

for item in numbers: 
    output = ''
    for count in range(item):
        output += 'x'
    print(output)
