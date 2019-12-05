'''
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
'''
lista = list(range(150000, 159999))
#lista = list(range(109165, 576723))
resultat = []
def code_cracker(number):
	n = str(number)
	for k, j in enumerate(n):
		if (k == 5):
			break
		elif (k < len(n) - 1) and (j <= n[k + 1]):
			print(n)
			continue
		else:
			return(False)
	for k, j in enumerate(n):
		if (k < len(n) - 1) and (k < len(n) - 1) and (j == n[k + 1]) and (j != n[k + 2]):
			return(True)
		else:
			break

for i in lista:
	if code_cracker(i):
		resultat.append(i)
print(resultat)
print(len(resultat))
