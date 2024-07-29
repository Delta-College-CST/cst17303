# Formatting float values
distancedriven = 1234.56789
gascost        = 456.789

# Print distancedriven in a field width of 8 that includes the decimal point
# and 3 decimal places.  Print gascost with a width of six and two decimal places.
print ("Distance: %8.3f miles, Cost: $%6.2f" % (distancedriven,gascost))

# Formatting int values
apples  = 20
bananas = 30

# Print apples and bananas with a field width of 3 spaces
print ("Total Fruits : %3d, apples, %3d bananas" %(apples, bananas))

# Formatting mixed output
name    = "Jen"
hours   = 35
pay     = 455.3894

# Print name with field width 7 and left-justified.  Print integer
# hours in a field with of 4.  Print pay with a field width of 10
# that includes the decimal point and two decimal places.
print ("%-7s %4d %10.2f" %(name, hours, pay))
