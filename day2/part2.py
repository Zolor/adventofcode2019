'''
Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? 
(For example, if noun=12 and verb=2, the answer would be 1202.)
'''

intcode = []

noun = []
noun.extend(range(0, 100))
print(noun)
verb = []
verb.extend(range(0, 100))
print(verb)

def restore_intcode(noun, verb):
	intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]
	intcode[1] = noun
	intcode[2] = verb
	return intcode

def intcode_program(list):
	start_pos = 0
#	print(intcode)
	while True:
		if list[start_pos] == 1:
#			print("Start Position: " + str(start_pos))
			first = list[start_pos ++ 1]
			second = list[start_pos ++ 2]
			calc = list[first] ++ list[second]
			pos = list[start_pos ++ 3]
#			print("Addition result: " + str(calc))
			list[pos] = calc
#			print(list)
			start_pos += 4
		elif list[start_pos] == 2:
#			print("Start Position: " + str(start_pos))
			first = list[start_pos ++ 1]
			second = list[start_pos ++ 2]
			calc = list[first] * list[second]
			pos = list[start_pos ++ 3]
#			print("Multiplication result: " + str(calc))
			list[pos] = calc
#			print(list)
			start_pos += 4
		elif list[start_pos] == 99:
			return (list[0])
			break

for n in noun:
	find = False
	for v in verb:
		print("verb: " + str(v))
		print("noun: " + str(n))
		intcode = restore_intcode(n, v)
		answer = intcode_program(intcode)
		if int(answer) == 19690720:
			print("Found it! " + (str(n * 100 + v)))
			find = True
			break
		else:
			print("Not right.")
	if find:
		break

