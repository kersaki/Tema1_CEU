lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
for letra in lista_1:
    if letra in lista_2:
        lista_3.append(letra)
print (lista_3)