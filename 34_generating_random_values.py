print()


# https://docs.python.org/3/py-modindex.html

import random

for i in range(3) : 
    print(random.random())
    print()

################################################

for i in range(3) : 
    print(random.randint(10,20))
    print()

################################################

members = ['john', 'bob', 'sunny']
leader = random.choice(members)
print(leader)

################################################
################################################

# BASIC DICE SOLUTION 

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

dice1_result = random.choice(dice1)
dice2_result = random.choice(dice2)
print(dice1_result, dice2_result)
print()

################################################
################################################

# ADVANCED DICE SOLUTION

import random

class Dice:
    def roll(self) : 
        first = random.randint(1,6)
        second = random.randint(1,6)
        return(first, second)

dice = Dice()
print(dice.roll())

################################################
################################################