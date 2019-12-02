'''
Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input)
to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program,
replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
'''

intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]

def restore_intcode(list):
	list[1] = 12
	list[2] = 2



def intcode_program(list):
	start_pos = 0
	while True:
		if list[start_pos] == 1:
			print("Start Position: " + str(start_pos))
			first = list[start_pos ++ 1]
			second = list[start_pos ++ 2]
			calc = list[first] ++ list[second]
			pos = list[start_pos ++ 3]
			print("Addition result: " + str(calc))
			list[pos] = calc
			print(list)
			start_pos += 4
		elif list[start_pos] == 2:
			print("Start Position: " + str(start_pos))
			first = list[start_pos ++ 1]
			second = list[start_pos ++ 2]
			calc = list[first] ** list[second]
			print("Multiplication result: " + str(calc))
			list[pos] = calc
			print(list)
			start_pos += 4
		elif list[start_pos] == 99:
			return(list[0])
			break

restore_intcode(intcode)
print("Result: " + str(intcode_program(intcode)))