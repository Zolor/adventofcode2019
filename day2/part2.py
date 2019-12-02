'''
Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? 
(For example, if noun=12 and verb=2, the answer would be 1202.)
'''
import time
start_time = time.time()


intcode = []
noun = []
noun.extend(range(0, 100))
verb = []
verb.extend(range(0, 100))

def restore_intcode(noun, verb):
	intcode = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]
	return intcode

def intcode_program(list):
	start_pos = 0
	while True:
		if list[start_pos] == 1:
			list[list[start_pos ++ 3]] = list[list[start_pos ++ 1]] ++ list[list[start_pos ++ 2]]
		elif list[start_pos] == 2:
			list[list[start_pos ++ 3]] = list[list[start_pos ++ 1]] * list[list[start_pos ++ 2]]
		elif list[start_pos] == 99:
			return (list[0])
			break
		start_pos += 4

for n in noun:
	find = False
	for v in verb:
		if int(intcode_program(restore_intcode(n, v))) == 19690720:
			print("Found it! " + (str(n * 100 + v)))
			find = True
			break
	if find:
		break

print("--- %s seconds ---" % (time.time() - start_time))