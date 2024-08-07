# CST 173 - Delta College
# This program prompts for a rectangle length & width.  It then
# calculates and displays the rectangle area, perimeter, and diagonal.

import math

# Input rectangle attributes
print("For given rectangle:")
length = float(input("==> Enter length (meters): "))
width  = float(input("==> Enter width  (meters): "))

# Processing
area      = length * width
perimeter = 2 * length + 2 * width
diagonal  = math.sqrt(length * length + width * width)

# Output
print()
print ("For rectangle dimensions")
print ("  Length: %5.1f meters X %5.1f meters" % (length, width))
print ("  Perimeter: %8.1f meters"        % (perimeter))
print ("  Area:      %8.3f square meters" % (area))
print ("  Diagonal:  %8.3f meters" % (diagonal))

