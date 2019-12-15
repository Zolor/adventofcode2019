from intcode2 import intcode_program
import collections

with open('input.txt') as input:
	for i in input.readlines():
		code = [int(part) for part in i.strip().split(',')]
		intcode_dict = collections.defaultdict(int, enumerate(code))

print(intcode_program(intcode_dict))