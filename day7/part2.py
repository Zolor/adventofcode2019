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
'''
0 = A, 1 = B, 2 = C, 3 = D, 4 = E
'''
def compute(intcode, phase_code):
	output = 0
	run = 0
	intcode_state = [[],[],[],[],[]]
	while True:
		for i,e in enumerate(phase_code):
			i = int(i)
			e = int(e)
			if run == 0:
				output, lista, state = intcode_program(intcode, [e, i], 0)
				intcode_state[i].extend([lista, state])
				run += 1
			elif run < 5 and run != 0:
				output, lista, state = intcode_program(intcode, [e, output], 0)
				intcode_state[i].extend([lista, state])
				run += 1
				print("elif run < 5" + str(intcode_state))
			elif run >= 5:
				#print(intcode_state[i][1])
				output, lista, state = intcode_program(intcode_state[i][0], [output], intcode_state[i][1])
				intcode_state[i][0] = lista
				intcode_state[i][1] = state
				print(intcode_state[i][0])
				run += 1
				if output == False:
					return answer
				else:
					answer.append(output)

test_code = '56789'
answer = []

print(compute(intcode, test_code))
print(answer)
