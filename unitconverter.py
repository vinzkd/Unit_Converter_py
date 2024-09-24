# Unit converter script
# By Vinz Karl Damuag
# I went super crazy with this script and had a lot of fun making it
import math # import functions like round() and math.degrees()
# Title and instructions
print('\nUnit converter by Vinz\n')
print('Use abbreviations for units')
print('Type "round" to set the number of decimal places to round to\n')
while True:
# Placeholder variables
# If I dont define them early, it'll mess up the dictionaries with formulas
initial_unit = 0 # Unit you want to convert from
final_unit = 0 # Unit you want to convert to
decimals = 2 # Default number of decimal places to round to
# Inputting answer (amount you want to convert)
answer = input('Enter value: ')
while answer == 'round': # Lets you choose how many decimal places to round to
(only for values above 0)
decimals = int(input('Enter number of decimal places to round to: '))
answer = input('\nEnter value: ')
if answer != 'round':
pass
while len(str(answer)) == 0: # In case you forget to input a number
print('\nError: Input value\n')
answer = input('Enter value: ')
while True:
try:
answer = float(answer)
break
except ValueError: # In case you input a character that's not a number
print('\nError: Enter a number\n')
answer = input('Enter value: ')
# Dictionaries of units
# conversions are based on one unit
# e.g. meters in km, meters in nm, meters in ft, etc.
units_length = {
# Length
# Base: 1 meter
'm': 1, # meter
'nm': 1*10**-9, # nanometer
'um': 1*10**-6, # micrometer
'mm': 0.001, # millimeter
'cm': 0.01, # centimeter
'dm': 0.1, # decimeter
'dam': 10, # decameter
'hm': 100, # hectometer
'km': 1000, # kilometer
'in': 0.0254, # inch
'ft': 0.3048, # foot
'yd': 0.9144, # yard
'mi': 1609.344, # mile
'NM': 1852, # nautical mile
}
units_mass = {
# Mass
# Base: 1 gram
'g': 1, # gram
'ng': 1*10*-9, # nanogram
'ug': 1*10**-6, # microgram
'mg': 0.001, # milligram
'cg': 0.01, # centigram
'dg': 0.1, # decigram
'dag': 10, # decagram
'hg': 100, # hectogram
'kg': 1000, # kilogram
't': 1*10**6, # metric ton
'oz': 28.3495, # ounce
'lb': 453.59237, # pound
'tn': 907185, # US ton
'st': 6350.29 # stone
}
units_volume = {
# Volume
# Base: 1 liter
'l': 1, # liter
'ml': 0.001, # milliliter
'cl': 0.01, # centiliter
'dl': 0.1, # deciliter
'dal': 10, # decaliter
'hl': 100, # hectoliter
'kl': 1000, # kiloliter
'nm3': 1*10**-24, # cubic nanometer
'um3': 1*10**-15, # cubic micrometer
'mm3': 1*10**-6, # cubic millimeter
'cm3': 0.001, # cubic centimeter
'dm3': 1, # cubic decimeter
'm3': 1000, # cubic meter
'dam3': 1*10**6, # cubic decameter
'hm3': 1*10**9, # cubic hectometer
'km3': 1*10**12, # cubic kilometer
'gal': 3.78541, # US gallon
'qt': 0.946353, # US quart
'pt': 0.473176, # US pint
'c': 0.24, # US cup
'floz': 0.0295735, # US fluid ounce
'T': 0.0147868, # US tablespoon
't': 0.00492892, # US teaspoon
'ft3': 28.3168, # cubic feet
'in3': 0.0163871 # cubic inch
}
units_time = {
# Time
# Base: 1 hour
'h': 1, # hour
'ns': 1/(3.6*10**12), # nanosecond
'us': 1/(3.6*10**9), # microsecond
's': 1/3600, # second
'min': 1/60, # minute
'day': 24, 'days': 24,
'week': 168, 'weeks': 168,
'month': 730, 'months': 730,
'year': 8760, 'years': 8760,
'decade': 87600, 'decades': 87600,
'century': 876000, 'centuries': 876000
}
units_temperature = {
# Temperature conversions
'C': (answer-32)*5/9, # Celcius
'F': (answer*9/5)+32, # Fahrenheit
'K': 273.15 # Kelvin (C to K)
}
units_angle = {
# Angle measures
# the math module has this built in :D
'deg': math.degrees(answer), # degrees
'rad': math.radians(answer) # radians
}
# My solution to making a list of all dictionaries
units = {}
units.update(units_length)
units.update(units_mass)
units.update(units_volume)
units.update(units_time)
units.update(units_temperature)
units.update(units_angle)
# Code for inputting units
initial_unit = input('Enter initial unit: ')
while initial_unit not in units: # In case you spell a unit wrong or typed
something random
print('\nError: Invalid unit\n')
initial_unit = input('Enter initial unit: ')
while len(str(initial_unit)) == 0: # In case you input nothing
print('\nError: Input unit\n')
initial_unit = input('Enter initial unit: ')
final_unit = input('Enter final unit: ')
while final_unit not in units:
print('\nError: Invalid unit\n')
final_unit = input('Enter final unit: ')
while len(str(final_unit)) == 0:
print('\nError: Input unit\n')
final_unit = input('Enter final unit: ')
# Conversions
# Length units
if initial_unit in units_length:
if final_unit in units_length:
result = answer*units_length[initial_unit]/units_length[final_unit]
else: # In case you convert the wrong units (e.g. 20 meters to 7 grams)
print('\nError: Incompatible units or incorrect abbreviation\n')
# Mass units
if initial_unit in units_mass:
if final_unit in units_mass:
result = answer*units_mass[initial_unit]/units_mass[final_unit]
else:
print('\nError: Incompatible units or incorrect abbreviation\n')
# Volume units
if initial_unit in units_volume:
if final_unit in units_volume:
result = answer*units_volume[initial_unit]/units_volume[final_unit]
else:
print('\nError: Incompatible units or incorrect abbreviation\n')
# Time units
if initial_unit in units_time:
if final_unit in units_time:
result = answer*units_time[initial_unit]/units_time[final_unit]
else:
print('\nError: Incompatible units or incorrect abbreviation\n')
# Temperature
# (slightly different from the others because it involves formulas)
if initial_unit in units_temperature:
if final_unit in units_temperature:
if final_unit == 'C' or 'F' and initial_unit == 'C' or 'F':
result = units_temperature[final_unit]
if initial_unit == 'C' and final_unit == 'K':
result = answer+units_temperature['K']
if initial_unit == 'F' and final_unit == 'K':
result = units_temperature['C']+units_temperature['K']
if initial_unit == 'K' and final_unit == 'C':
result = answer-units_temperature['K']
if initial_unit == 'K' and final_unit =='F':
result = (answer-units_temperature['K'])*9/5+32
else:
print('\nError: Incompatible units or incorrect abbreviation\n')
# Angle measures
if initial_unit in units_angle:
result = units_angle[final_unit]
# Print output
while True:
try:
if result > 1:
result = round(result, decimals)
print('\n'+str(result)+' '+str(final_unit)+'\n')
del result
break
except NameError: # Prevents some variable errors
break
