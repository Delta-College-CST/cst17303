# CST 173 - Delta College
# This program prompts for a rectangle length & width.  It then
# calculates and displays the rectangle area and perimeter

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
print ("For rectangle dimensions",length,"meters X",width,"meters:")
print ("  Perimeter: %8.1f meters"        % (perimeter))
print ("  Area:      %8.2f square meters" % (area))
print ("  Diagonal:  %8.3f square meters" % (diagonal))
