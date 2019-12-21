import operator
from typing import NamedTuple
import math

class Coord(NamedTuple):
	x: int
	y: int

base = Coord(28, 29)
coords = set()

with open('input.txt') as input:
	for y,line in enumerate(input):
		for x,word in enumerate(line):
			if word == "#":
				coords.add(Coord(x, y))

def astroid_counter(coords):
	visible_asteroids_d = {}
	for coord in coords:
		tmp_counts = {}
		for comparison in coords:
			if coord == comparison:
				continue
			else:
				myradians = math.atan2(coord.y-comparison.y, coord.x-comparison.x)
				mydegrees = math.degrees(myradians)
				if mydegrees in tmp_counts.keys():
					if math.sqrt((comparison.x - base.x) ** 2 + (comparison.y - base.y) ** 2) < math.sqrt((tmp_counts.get(mydegrees).x - base.x) ** 2 + (tmp_counts.get(mydegrees).y - base.y) ** 2):
						tmp_counts[mydegrees] = comparison
				else:
					tmp_counts[mydegrees] = comparison
		if len(visible_asteroids_d.keys()) < len(tmp_counts.keys()):
			visible_asteroids_d = tmp_counts.copy()
	return(visible_asteroids_d)

visible_asteroids_d = astroid_counter(coords)
visible_asteroids_s = set()
#Making a list, sorting it twice~
for values in visible_asteroids_d.values():
	visible_asteroids_s.add(values)
#This magic line dictates that we want the lazer to start pointing up (90 degrees) and then move clockwise (+ sign after degrees, - is counterclockwise)
sorted_list = sorted(visible_asteroids_s, key=lambda visible_asteroids_s: (90 + math.degrees(math.atan2(*tuple(map(operator.sub, visible_asteroids_s, base))[::-1]))) % 360)
print(sorted_list)
print(sorted_list[199].x * 100 + sorted_list[199].y)
