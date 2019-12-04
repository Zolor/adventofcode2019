'''
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
'''

input = str(range(109165, 576723))

def code_cracker(input):
	result = []
	for i, j in enumerate(input[:-1]):
	    if j  == input[i+1]: 
       		if input[i] == input[i+1]:
				result.append[input]
	print(result)
	
#	for i in input:
#		for letter in i:
#			pos = int(i.index(letter))
#			print(type(pos))
#			p = str(i)
#			if int(letter) == i[pos ++ 1]:
#				result.append[i]
#				break
#	print(result)

code_cracker(input)
