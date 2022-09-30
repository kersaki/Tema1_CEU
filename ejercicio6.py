lista=[int(input('Introduzca los numeros deseados: '))]
lista_pares=[]
lista_impares=[]
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print(lista_pares)
print(lista_impares)
print(lista)
