import sys
#from PIL import Image

def list_maker(input):
	c = 25 * 6
	#Take List make it string
	input = ''.join(input)
	#Calculate amount of numbers in string divide by c
	#tot = len(input) / c
	#Divide the string into a list of c entries and return list
	output = [input[i:i+c] for i in range(0, len(input), c)]
	return output

def decoder(input):
	#Create a list with pixels 0 = Black, 1 = White, 2 = Transparent
	output = []
	x = 0
	y = 0
	while y < len(input[0]):
#		print("Y: " + str(y) + " and X: " + str(x))
		for i in input[x][y]:
			if i == "0":
				output.append(" ")
				y += 1
				x = 0
				break
			elif i == "1":
				output.append("@")
				y += 1
				x = 0
				break
			elif i == "2":
				x += 1
				continue
	return output

#def image_maker(input):
	#Create image from input

input = sys.argv[1]
o = open(input).readlines()
output = (decoder(list_maker(o)))

for i in range(6):
	print(output[i*25:(i+1)*25])

