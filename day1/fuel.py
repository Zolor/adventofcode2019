'''
What is the sum of the fuel requirements for all of the modules on your spacecraft?

Bonus 2nd star:

What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel?
(Calculate the fuel requirements for each module separately, then add them all up at the end.)

'''
import math

sum = 0
filepath='input.txt'

def fuel_calc(input):
    return math.floor(input/3)-2

with open(filepath) as fi:
    for cnt, line in enumerate(fi):
        calc = (fuel_calc(int(line)))
        while calc > 0:
            sum += calc
            calc = (fuel_calc(calc))
    print(sum)
