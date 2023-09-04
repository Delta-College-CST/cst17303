# This program returns change from a dollar in coins

# Input cost per item (less than $1 and determine change)
cost = int(input("What is item cost (cents)? "))
change = 100 - cost

# Extract coinage for change - large-to-small
quarters = change // 25
leftover = change % 25
dimes    = leftover // 10
leftover = leftover % 10
nickels  = leftover // 5
pennies  = leftover % 5

# Output results
print ("Your change is:",change,"cents")
print ("  Quarters: ",quarters)
print ("  Dimes:    ",dimes)
print ("  Nickels:  ",nickels)
print ("  Pennies:  ",pennies)
