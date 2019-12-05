'''
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
'''
#lista = list(range(150000, 159999))
lista = list(range(109165, 576723))
samling = {}
def code_cracker(number):
	n = str(number)
	for k, j in enumerate(n):
		if (k == 5):
			if (k == 5) and (j < n[k - 1]):
				try:
				    del samling[n]
				    return
				except KeyError:
				    print("Key " + n + " not found")
				return
			continue
		elif (k == 0) and (j <= n[k + 1]):
			if (j == n[k + 1]) and (j != n[k + 2]):
				samling.update({ n: {'contains_two_adjacent': True}})
				continue
		elif (k < len(n) - 1)  and (j >= n[k - 1]): #Check if prev. number is smaller
			if (k == 4) and (j == n[k + 1]) and (j != n[k - 1]):
				samling.update({ n: {'contains_two_adjacent': True}})
				continue
			elif (k != 4) and (j == n[k + 1] and (j != n[k + 2]) and (j != n[k - 1])):
				samling.update({ n: {'contains_two_adjacent': True}})
				continue
		else:
			try:
			    del samling[n]
			    return
			except KeyError:
				return

for i in lista:
	code_cracker(i)
print(len(samling))
