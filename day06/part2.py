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
	san_travel = []
	you_travel = []
	planet = planets["YOU"]
	while planet in planets:
		you_travel.append(planet)
		planet = planets[planet]
	print(you_travel)
	planet = planets["SAN"]
	while planet in planets:
		san_travel.append(planet)
		planet = planets[planet]
	print(san_travel)
	dups = set(san_travel) & set(you_travel)
	for d in dups:
		san_travel.remove(d)
		you_travel.remove(d)
	total = len(san_travel) + len(you_travel)
	print(you_travel)
	print(san_travel)
	return total


o = open(input).readlines()
#print(o)
print(loop(o))