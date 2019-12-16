import time
start_time = time.time()

fet_lista = []
with open('input.txt') as input:
	for i in input.read():
		i = int(i)
		fet_lista.append(i)

#fet_lista = [1,2,3,4,5,6,7,8]
base_pattern = [0, 1, 0, -1]
def pattern_maker(input, iter):
	if iter == 0:
		end_pattern = base_pattern
	else:
		end_pattern = [val for val in base_pattern for _ in range(0, (iter + 1))]
	end_pattern = end_pattern * (len(input) // len(end_pattern) + 1)
	end_pattern.remove(end_pattern[0])
	return(end_pattern)

def runner(input):
	output = []
	for i in range(len(input)):
		pattern = pattern_maker(input, i)
		zip_list = [a*b for a,b in zip(input,pattern)]
		output.append(abs(sum(zip_list)) % 10)
	return output

for x in range(100):
	tmp_list = runner(fet_lista)
	fet_lista = tmp_list
output = ''.join([str(fet_lista[i]) for i in range(len(fet_lista)) if i < 8])
print(output)
print("--- %s seconds ---" % (time.time() - start_time))