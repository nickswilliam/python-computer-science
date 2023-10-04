#def es la palabra clave para definir una función

def printMessage():
    name = input('Hello whats your name?: \n')
    print('Hi,', name)

""" printMessage() """ #invocación de la función creada

#la función 'max' busca el caracter más grande de la A-Z, y si es en minuscula, lo toma como el valor más grande.
#es decir si escribo: 'Hola' el valor mas grande será la 'o', si escribo 'HOla', será la 'l'
#ej:

bigChar = max('Hola')  #en este caso el caracter mas grande es la U
print(bigChar, 'Caracter mas grande')

#la función 'min' busca el caracter de menor valor de la A-Z y que sea en mayuscula,
# por ejemplo si tengo la palabra "Hola", el valor de retorno será la "H", si en cambio tengo la palabra "HAla", el retorno será "A"
# a su vez, el caracter ' ' espacio o blank es el de menor valor

minChar = min('Hola mundo')
print(minChar)
minChar2 = min('HOla')
print(minChar2)

print(1 + 2 * float(3) / 4 - 5)

