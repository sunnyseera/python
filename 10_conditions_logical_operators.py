print()

has_high_income = True
has_good_credit = True
has_criminal_record = False

##########################################################################

# AND 
if has_high_income and has_good_credit:
    print('Eligble for loan')

print()

##########################################################################

# OR 
if has_high_income or has_good_credit:
    print('Eligble for loan')

print()

##########################################################################

# NOT EQUAL
if has_high_income != False:
    print('Eligble for loan')
    print()

if has_good_credit and not has_criminal_record:
    print("No criminal record, eligle for loan")
    print()

##########################################################################

# GREATER THAN
temperature = 30

if temperature >= 30:
    print("its hot.")
    print()
else:
    print("its not that hot")
    print()

#  == Equal
#  > Greather Than
#  < Less Than 
#  >= Greater than OR Equal too 
#  <= Less than OR Equal too 
#  != Does Not Equal 

##########################################################################

name = "Sunny"
print(len(name))

if len(name) < 3:
    print("Name is too short.")
    print()
elif len(name) > 50:    
    print("Name is too long.")
    print()
else:
    print("Name is good.")
    print()

##########################################################################