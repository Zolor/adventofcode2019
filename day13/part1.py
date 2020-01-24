from intcode1 import intcode_program
import collections

with open('input.txt') as input:
	for i in input.readlines():
		code = [int(part) for part in i.strip().split(',')]
		intcode_dict = collections.defaultdict(int, enumerate(code))

output, d, start_pos, rel_base = intcode_program(intcode_dict)
count = 0
#lista = list (d.values())
output = output[2::3]

for x in output:
	if x == 2:
		count += 1
print(count)