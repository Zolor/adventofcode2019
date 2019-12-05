'''
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
'''
#lista = list(range(100, 200))
lista = list(range(109165, 576723))
def code_cracker(lista):
    resultat = []
    for i in lista:
        n = str(i)
        for k, j in enumerate(n):
            if (k < len(n) - 1) and (j == n[k + 1]) and (j != n[k + 2]):
                resultat.append(i)
                break
#    print(resultat)
    remove = []
    for i in resultat:
        n = str(i)
        for k, j in enumerate(n):
            if (k < len(n) - 1) and (j > n[k + 1]):
                remove.append(i)
                break
    for i in remove:
        resultat.remove(i)
    print(len(resultat))
    
code_cracker(lista)
