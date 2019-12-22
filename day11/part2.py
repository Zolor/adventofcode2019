from typing import NamedTuple
from intcode import intcode_program

intcode = [0]*10000
with open('input.txt') as input:
	for i in input.readlines():
		code = i.split(',')
	for c in range(len(code)):
		intcode[c] = (int(code[c]))

class Coord(NamedTuple):
	x: int
	y: int

#Make a dict that keeps track of coordinates, create new entries as we go
panel = {}
def rob_the_painter(intcode):
	robot_pos = Coord(50, 50)
	robot_facing = "UP"
	output = 0
	output_direction = 0
	state = 0
	rel_base_state = 0
	intcode_state = intcode
	panel[robot_pos] = 1
#	print(panel)
	def paint(output_direction, output_color, robot_facing, robot_pos):
		if robot_facing == "UP":
			panel[robot_pos] = output_color
			if output_direction == 0:
				robot_pos = Coord(robot_pos.x - 1, robot_pos.y)
				robot_facing = "LEFT"
			elif output_direction == 1:
				robot_pos = Coord(robot_pos.x + 1, robot_pos.y)
				robot_facing = "RIGHT"
			return robot_facing, robot_pos
		elif robot_facing == "DOWN":
			panel[robot_pos] = output_color
			if output_direction == 0:
				robot_pos = Coord(robot_pos.x + 1, robot_pos.y)
				robot_facing = "RIGHT"
			elif output_direction == 1:
				robot_pos = Coord(robot_pos.x - 1, robot_pos.y)
				robot_facing = "LEFT"
			return robot_facing, robot_pos
		elif robot_facing == "RIGHT":
			panel[robot_pos] = output_color
			if output_direction == 0:
				robot_pos = Coord(robot_pos.x, robot_pos.y + 1)
				robot_facing = "UP"
			elif output_direction == 1:
				robot_pos = Coord(robot_pos.x, robot_pos.y - 1)
				robot_facing = "DOWN"
			return robot_facing, robot_pos
		elif robot_facing == "LEFT":
			panel[robot_pos] = output_color
			if output_direction == 0:
				robot_pos = Coord(robot_pos.x, robot_pos.y - 1)
				robot_facing = "DOWN"
			elif output_direction == 1:
				robot_pos = Coord(robot_pos.x, robot_pos.y + 1)
				robot_facing = "UP"
			return robot_facing, robot_pos

	while True:
		if robot_pos not in panel.keys():
			panel[robot_pos] = 0
		output_color, intcode_state, state, rel_base_state = intcode_program(intcode_state, [panel.get(robot_pos)], state, rel_base_state)
		if output_color == None:
			return panel
		elif output_color == 0 or output_color == 1:
			output_direction, intcode_state, state, rel_base_state = intcode_program(intcode_state, [], state, rel_base_state)
			if output_direction == None:
				return panel
			robot_facing, robot_pos = paint(output_direction, output_color, robot_facing, robot_pos)
		else:
			raise NotImplementedError(output_color)

rob_the_painter(intcode)
tmp_output = []
for x in range(100):
	tmp_output.append([])
	for y in range(100):
		if Coord(x, y) in panel.keys() and (panel.get(Coord(x, y)) == 1):
			tmp_output[x] += ["#"]
		else:
			tmp_output[x] += [" "]
	for line in tmp_output:
		print(line)
