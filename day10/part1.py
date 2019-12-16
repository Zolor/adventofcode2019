from typing import NamedTuple

class Coord(NamedTuple):
	x: int
	y: int

coords = set()
with open('input.txt') as input:
	for y,line in enumerate(input):
		for x,word in enumerate(line):
			if word == "#":
				coords.add(Coord(x, y))
	print(coords)

def astroid_counter(coords):
	counts = []
	for coord in coords:
		count = 0
		for comparison in coords:
			if coord == comparison:
				continue
			
		

