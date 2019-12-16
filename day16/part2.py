import time
start_time = time.time()

fet_pattern = []
fet_pattern_finns = False
fet_lista = []
tmp_lista = []
with open('input.txt') as input:
	for i in input.read():
		i = int(i)
		tmp_lista.append(i)
	fet_lista = [val for val in tmp_lista for _ in range(10000)]

base_pattern = [0, 1, 0, -1]
def pattern_maker(input, iter):
	if iter == 0:
		end_pattern = base_pattern
	else:
		end_pattern = [val for val in base_pattern for _ in range(0, (iter + 1))]
	end_pattern = end_pattern * (len(input) // len(end_pattern) + 1)
	end_pattern.remove(end_pattern[0])
	return(end_pattern)

def runner(input, fet_pattern_finns):
	output = []
	for i in range(len(input)):
		if fet_pattern_finns == False:
			pattern = pattern_maker(input, i)
			fet_pattern.append(pattern)
		zip_list = [a*b for a,b in zip(input,fet_pattern[i])]
		output.append(abs(sum(zip_list)) % 10)
	fet_pattern_finns = True
	return output

for x in range(100):
	tmp_list = runner(fet_lista, fet_pattern_finns)
	fet_lista = tmp_list
output = ''.join([str(fet_lista[i]) for i in range(len(fet_lista)) if i < 8])
print(output)
print("--- %s seconds ---" % (time.time() - start_time))
