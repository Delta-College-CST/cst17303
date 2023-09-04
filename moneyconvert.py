# This program prompts for dollar amount.  It then converts to
# Euros and British Pounds

# Constant declarations
EUROS_PER_DOLLAR  = 0.98
POUNDS_PER_DOLLAR = 0.83

# Input
dollars = float(input("Enter dollar amount: "))

# Convert currency
euros  = dollars * EUROS_PER_DOLLAR
pounds = dollars * POUNDS_PER_DOLLAR

# Output
print ("$",dollars,"=")
print ("         ",euros, "Euros")
print ("         ",pounds,"Pounds")
