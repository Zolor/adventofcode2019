import time
start_time = time.time()

fet_lista = []
tmp_lista = []
with open('input.txt') as input:
	for i in input.read():
		i = int(i)
		tmp_lista.append(i)
	fet_lista = tmp_lista * 10000

offset = fet_lista[0:7]
offset = int(str(offset[0]) + str(offset[1]) + str(offset[2]) + str(offset[3]) + str(offset[4]) + str(offset[5]) + str(offset[6]))
fet_lista = fet_lista[offset:len(fet_lista)]
for x in range(100):
	tmp = 0
	for i in reversed(range(0, len(fet_lista))):
		tmp += fet_lista[i]
		fet_lista[i] = tmp % 10

print(''.join([str(c) for c in fet_lista[:8]]))

print("--- %s seconds ---" % (time.time() - start_time))
