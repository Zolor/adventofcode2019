from intcode import intcode_program
import collections

with open('input.txt') as input:
	for i in input.readlines():
		code = [int(part) for part in i.strip().split(',')]
		intcode_dict = collections.defaultdict(int, enumerate(code))

output, lista, start_pos, rel_base = intcode_program(intcode_dict)
print(output)
print(lista)

