#las listas son como los arrays de JS
#a diferencia de los strings, son mutables

list = ['Papa', 'Zanahoria', 'Tomate', 'Lechuga', 'Pan', 'Leche', 'Falopa']
print(list)

list[3] = 'Rucula' #cambiamos el valor de la posición 3 por 'Rucula' en vez de lechuga y luego imprimimos

print(list)

#se puede usar la funcion len() para ver el largo de una lista
#ej

print(len(list))

#la función range, nos devuelve el rango de elementos de una lista, expresado en el orden de indice 
#ejemplo
#nuestra lista tiene un total de 7 elementos, lo cual los indices se mostrarian así [0,1,2,3,4,5,6]

print(range(len(list)))

for i in range(len(list)):
    listA = list[i]
    print('Voy a comprar:', listA)