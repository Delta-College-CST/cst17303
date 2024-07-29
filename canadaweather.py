# This program converts a Canadian weather report to U.S. units

KPH_TO_MPH_CONVERSION =  0.6213711922

# Read location (as string) and then temperature and winds
location = input("Enter observation location: ")
tempC    = float(input("Enter temperature (deg C): "))
windKPH  = float(input("Enter wind speed (kph): "))

# Perform unit conversions
windMPH = windKPH * KPH_TO_MPH_CONVERSION
tempF = 9.0 / 5.0 * tempC + 32.0

# Output weather report
print()  # Blank line
print("Location: ", location)
print("Temperature: %5.1f deg F" % (tempF))
print("Wind speed:  %4.1f mph" % (windMPH))
