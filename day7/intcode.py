def intcode_program(list, input_value, start_pos):
	def parameter(instr, x):
		mode = instr // (10 ** (x + 1)) % 10
		if mode == 0:
			return list[list[start_pos + x]]
		elif mode == 1:
			return list[start_pos + x]
		else:
			raise NotImplementedError(mode)
#	if state == None:
#		#print("State is None! " + str(state))
#		input_counter = 0
#		start_pos = 0
#	else:
	input_counter = 0
	print("Before intcode: " + str(start_pos))
#		start_pos = state
#		print("State! " + str(start_pos))
	while start_pos < len(list):
		instr = list[start_pos]
		opcode = list[start_pos] % 100
		if opcode == 1:
			list[list[start_pos + 3]] = parameter(instr, 1) + parameter(instr, 2)
			start_pos += 4
		elif opcode == 2:
			list[list[start_pos + 3]] = parameter(instr, 1) * parameter(instr, 2)
			start_pos += 4
		elif opcode == 3:
			list[list[start_pos + 1]] = input_value[input_counter] #input value
			start_pos += 2
			input_counter += 1
		elif opcode == 4:
			start_pos += 2
			print("After intcode program: " + str(start_pos))
			return(parameter(instr, 1), list, start_pos)
		elif opcode == 5:
			if parameter(instr, 1):
				start_pos = parameter(instr, 2)
			else:
				start_pos += 3
		elif opcode == 6:
			if not parameter(instr, 1):
				start_pos = parameter(instr, 2)
			else:
				start_pos += 3
		elif opcode == 7:
			if parameter(instr, 1) < parameter(instr, 2):
				list[list[start_pos + 3]] = 1
			else:
				list[list[start_pos + 3]] = 0
			start_pos += 4
		elif opcode == 8:
			if parameter(instr, 1) == parameter(instr, 2):
				list[list[start_pos + 3]] = 1
			else:
				list[list[start_pos + 3]] = 0
			start_pos += 4
		elif opcode == 99:
			return False
		else:
			raise AssertionError(opcode)