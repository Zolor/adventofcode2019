from intcode import intcode_program

intcode = []
with open('input.txt') as input:
	for i in input.readlines():
		code = i.split(',')
	for c in code:
		intcode.append(int(c))

answer = 0
for a in range(5):
	for b in range(5):
		for c in range(5):
			for d in range(5):
				for e in range(5):
					if a not in [b,c,d,e] and b not in [c, d, e] and c not in [d, e] and d != e:
						output = 0
						for phase in [a, b, c, d, e]:
							output = intcode_program(intcode, [phase, output])
						if output >= answer:
							answer = output
print(answer)