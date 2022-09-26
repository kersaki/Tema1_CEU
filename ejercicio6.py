lista=[input('Introduzca los numeros deseados: ')]
lista_pares=[]
lista_impares=[]
for i in lista:
    if i % 2:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
