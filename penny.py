# pennies = int(input("How many pennies do you have? "))

# if(pennies >= 100):
#     dollars = pennies - 100 
#     print("$",dollars)

# if(pennies >= 25):
#     quarters = pennies  / 25
#     print(quarters,"Quarters")

# import os
# os.system('cls')

# startP - int(input"How many pennies do you have? ")

# def change(pennies):
#     dollars = int(pennies/100)

import os
import math 
os.system('cls')

pennies = int(input("How many pennies? "))
while pennies >= 5:
    if pennies >= 100:
     print(f"Dollars = {math.floor(pennies / 100)}")
     pennies -= 100 * math.floor(pennies / 100)
    elif pennies >= 25:
     print(f"Quarters = {math.floor(pennies / 25)}")
     pennies -= 25 * math.floor(pennies / 25)
    if pennies >= 10:
        print(f"Dimes = {math.floor(pennies / 10)}")
        pennies -= 10 * math.floor(pennies / 10)
    elif pennies >= 5:
        print(f"Nickles = {math.floor(pennies / 5)}")
        pennies -= 5 * math.floor(pennies / 5)
print(f"Pennies = {pennies}")