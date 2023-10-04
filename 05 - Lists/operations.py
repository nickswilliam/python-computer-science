#concatenacion de listas

a = [1, 2 , 3]
b = [ 4, 5, 6]
c = a + b

print(c)

#las listas pueden ser cortadas o "slicings" usando ":"
#ejemplo

sliceList = ['Papa', 'Zanahoria', 'Tomate', 'Lechuga', 'Pan', 'Leche', 'Falopa']
print(sliceList[4:6]) #acá indicamos que tome desde la posición 4 "pan" hasta la 6, no inclusive [pan, leche]
print(sliceList[2:]) #de la posición 2 en adelante hasta el fin del array
print(sliceList[:2]) #hasta la posición 2, no inclusive

x = list() #nos crea una lista vacia la funcion list()

""" print(type(x))
print(dir(x)) #imprime la lista de metodos disponibles para las listas """

#metodo append
#agrega un elemento al final de la lista, si la lista está vacía, el primer elemento agregado con append, sera el de indice 0
stuff = list()
stuff.append('Libro')
stuff.append(100)

print(stuff)
stuff.append('galleta')
print(stuff)

#encontrar valores en una lista como pregunta, devolviendo valores booleanos

eg = [1, 9, 21, 10, 16]
print(9 in eg) #devuelve True
print(600 in eg) #devuelve False

#el metodo sort() nos permite ordenar los elementos de una lista de acuerdo al tipo de elemento y por orden numerico y alfabetico

amigos = ['Feto', 'Tramontina', 'Bassi', 'Camilu', 'Anto', 'Dani', 'Ariadna']
amigos.sort()
print(amigos)

#funciones integradas y listas

numeros = [ 3, 41, 12, 9, 74, 15]

print(len(numeros)) #total de elementos de la lista
print(max(numeros)) #numero más grande de la lista 74
print(min(numeros)) #numero más pequeño de la lista 3
print(sum(numeros)) #suma todos los numeros de la lista 154
print(sum(numeros)/len(numeros)) #promedio de todos los numeros