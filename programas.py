def saludo(n):
    for i in range(1,11):
        print(n,"*",i,"=", n*i )

   
saludo(5)
ejemplo=input("ingresar todos lo valores separados por un espacio...")
ejemplo = [int(x) for x in ejemplo.split()]

ejemplo = [1,5,6,9,4,12,25 ]
def separar_lista(lista):
    pares = []
    impares =  []
    for i in lista:
        if i %  2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares
separar_lista(ejemplo)
pares,impares = separar_lista(ejemplo)
print(pares)
print(impares)



