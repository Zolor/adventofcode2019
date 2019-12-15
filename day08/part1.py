import sys

def list_maker(input):
	c = 25 * 6
	#Take List make it string
	input = ''.join(input)
	print(len(input))
	#Calculate amount of numbers in string divide by c
	#tot = len(input) / c
	#Divide the string into a list of c entries and return list
	output = [input[i:i+c] for i in range(0, len(input), c)]
	return output

def decoder(input):
	x = 0
	output = 0
	for i in input:
		#Calculate amount of 0's in string
		if (x >= i.count('0')) or (x == 0):
			print(x)
			x = i.count('0')
			output = i.count('1') * i.count('2')
			print(output)
		#If amount of 0 is < x update x
			#Update output to calculate amounts of 1s and 2s in this string
	return output
		#Return output


input = sys.argv[1]
o = open(input).readlines()
print(decoder(list_maker(o)))
