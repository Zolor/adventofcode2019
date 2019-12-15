'''
orbital relationship is written AAA)BBB, which means "BBB is in orbit around AAA".

The total number of direct and indirect orbits in this example is 42.

key orbits around value
'''

import sys

input = sys.argv[1]

def loop(input):
	planets = {}
	for i in input:
		i = str(i)
		print("input: " + str(i))
		i = i.rstrip('\n')
		parent, name = i.split(')')
		planets[name] = parent
	print(planets)
	total = 0
	for planet in planets:
		print("Planet: " + planet)
		while planet in planets:
			total += 1
			planet = planets[planet]
			print(planet)
	return total


o = open(input).readlines()
#print(o)
print(loop(o))