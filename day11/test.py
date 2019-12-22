from intcode import intcode_program

intcode = []
with open('input.txt') as input:
	for i in input.readlines():
		code = i.split(',')
	for c in code:
		intcode.append(int(c))

output, lista, start_pos = intcode_program(intcode, [0])
print(output)
output, lista, start_pos = intcode_program(intcode, [], start_pos)
print(output)
print(start_pos)