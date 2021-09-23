print()

# Program to Convert from LBS to KGS

weight = int(input('Weight: '))
unit   = input('(L)bs or (K)gs: ')

if  unit == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.")
elif unit == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds.")
elif unit != "K" or "L" :
    print("Incorrect Selection")