def intcode_program(lista, input_value, start_pos = 0):
	def parameter(instr, x):
		mode = instr // (10 ** (x + 1)) % 10
		if mode == 0:
			return lista[lista[start_pos + x]]
		elif mode == 1:
			return lista[start_pos + x]
		elif mode == 2:
			return lista[rel_base + lista[start_pos + x]]
		else:
			raise NotImplementedError(mode)

	def store(instr, x):
		mode = instr // (10 ** (x + 1)) % 10
		if mode == 0:
			return lista[start_pos + x]
		elif mode == 2:
			return rel_base + lista[start_pos + x]
		else:
			raise NotImplementedError(mode)
	input_counter = 0
	rel_base = 0
	while start_pos < len(lista):
		instr = lista[start_pos]
		opcode = instr % 100
		if opcode == 1:
			lista[store(instr, 3)] = parameter(instr, 1) + parameter(instr, 2)
			start_pos += 4
		elif opcode == 2:
			lista[store(instr, 3)] = parameter(instr, 1) * parameter(instr, 2)
			start_pos += 4
		elif opcode == 3:
			lista[store(instr, 1)] = input_value[input_counter] #input value
			start_pos += 2
			input_counter += 1
		elif opcode == 4:
			tmp = parameter(instr, 1)
			start_pos += 2
			return(tmp, lista, start_pos)
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
				lista[store(instr, 3)] = 1
			else:
				lista[store(instr, 3)] = 0
			start_pos += 4
		elif opcode == 8:
			if parameter(instr, 1) == parameter(instr, 2):
				lista[store(instr, 3)] = 1
			else:
				lista[store(instr, 3)] = 0
			start_pos += 4
		elif opcode == 9:
			rel_base += parameter(instr, 1)
			start_pos += 2
		elif opcode == 99:
			return(None, lista, start_pos)
		else:
			raise AssertionError(opcode)
