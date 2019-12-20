from typing import NamedTuple
import math

class Coord(NamedTuple):
	x: int
	y: int

coords = set()
with open('input.txt') as input:
	for y,line in enumerate(input):
		for x,word in enumerate(line):
			if word == "#":
				coords.add(Coord(x, y))

def astroid_counter(coords):
	degrees_list = []
	for coord in coords:
		tmp_counts = set()
		for comparison in coords:
			if coord == comparison:
				continue
			else:
				myradians = math.atan2(coord.y-comparison.y, coord.x-comparison.x)
				mydegrees = math.degrees(myradians)
				tmp_counts.add(mydegrees)
		if len(degrees_list) < len(tmp_counts):
			degrees_list = tmp_counts.copy()
			best_asteroid = coord
	return(degrees_list, best_asteroid)

#def asteroid_destroyer(degrees_list, best_asteroid):


degrees_list, best_asteroid = astroid_counter(coords)
degrees_list = list(degrees_list)
degrees_list.sort()
print(degrees_list)