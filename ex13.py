from sys import argv # 'sys' is a 'module' that was imported. argv  = argument variable. Arguent variables are input given to the script when it's run on the command line.

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# when you run this script in terminal you enter the 'arguments' for the 3 variables, e.g. 'python ex13.py foo fizz flam'