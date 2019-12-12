from intcode import intcode_program

intcode = []
with open('testinput.txt') as input:
	for i in input.readlines():
		code = i.split(',')
	for c in code:
		intcode.append(int(c))

def gen_phase_codes():
	phase_codes = []
	for a in range(5, 10):
		for b in range(5, 10):
			if b == a:
				continue
			for c in range(5, 10):
				if c == a or c == b:
					continue
				for d in range(5, 10):
					if d == c or d == b or d == a:
						continue
					for e in range(5, 10):
						if e == d or e == c or e == b or e == a:
							continue
						else:
							phase_codes.append(str(a) + str(b) + str(c) + str(d) + str(e))
	return phase_codes

def compute(intcode, phase_code):
	state = True
	output = 0
	run = 0
	intcode_state = [[],[],[],[],[]]
	while state == True:
		for i in phase_code:
			i = int(i)
			if run == 0:
				output = intcode_program(intcode, [i, 0])
				print(str(i) + " and " + str(output) + " and run: " + (str(run)))
				run += 1
			elif run < 7 and run != 0:
				output = intcode_program(intcode, [i, output])
				print(str(i) + " and " + str(output))
				run += 1
			elif run >= 7:
				output = intcode_program(intcode, [output])
				print(str(i) + " and " + str(output))
				run += 1
				if output == False:
					return answer
				else:
					answer.append(output)
test_code = '56789'
answer = []

print(compute(intcode, test_code))