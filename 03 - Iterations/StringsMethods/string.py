str = 'Monty Python'

print(str[0:4]) #imprime desde la posición 0 a la 3 de la cadena M-O-N-T y no incluye la ultima, la numero 4

print(str[6:18]) #imprime desde la posición 6 a la ultima - no hay error si nos excedemos del total de caracteres

#omitir el principio o fin de una cadena

print(str[:2]) #corta la cadena hasta la posición < 2
print(str[7:]) #imprime desde la posición 7 hasta la ultima
print(str[:]) #imprime todos los caracteres de la cadena

#string concatenation

a = 'Hello '
b = 'There'
print(a + b)

#el operador in, en un string, es un indicador de verdadero o falso
#ejemplo

fruit = 'Manzana'

print('n' in fruit) #retorna el valor True
print('z' in fruit) #retorna el valor True
print('o' in fruit) #retorna el valor False

if 'm' or 'M' in fruit:
    print('Letra m encontrada')

#comparar cadenas de caracteres de acuerdo al orden alfabetico... teniendo en cuenta que las mayusculas son menores que que las minusculas
#para el ejemplo lo haré con minusculas solamente
#ejemplo:

if fruit < 'Banana':
    print('Tu palabra,' + fruit + ', viene antes que banana.')
elif fruit > 'Banana':
    print('Tu palabra,' + fruit + ',va despues que banana.')
else:
    print('Todo bien, son bananas')

#string library

greet = 'Hello bob'
low_greet = greet.lower() #lowercase de el saludo

print(low_greet)
print(greet.upper()) #upper lo pasa a mayusculas

str_to_capitalize = 'hola a todos mi nombre es nicolás.'
print(str_to_capitalize.capitalize()) #le agrega mayuscula al principio de la oración.

#str.find() ... Busca el primer elemento de coincidencia, y nos devuelve la posición en el cual se encuentra inicialmente la coincidencia
#ejemplo

find_za = fruit.find('za')
print(find_za) #en este caso la salida va a ser 3, ya que inicialmente za de Manzana se encuentra en el índice 3 y 4
#en el caso de no encontrar el indice de lo que le pasamos como argumento, nos devuelve un -1
#ejemplo

print(fruit.find('Pe'))

#search, and replace... replace() busca una palabra o caracter especifico y la reemplaza por otra/o caracter o cadena.
#ejemplo

saludo = 'Hola Lara, como estás?'
repl = saludo.replace('Lara', 'Nico') #La cadena de la izquierda representa el texto a reemplazar, la de la derecha, el texto que reemplazante.

print(repl) #la salida será "Hola Nico, como estás?"

#lstrip() remueve los espacios en blanco de la izquierda
#rstrip() remueve los espacios en blanco de la derecha
#strip() remueve los espacios en blanco del principio y del final
greet_blanks = '     Hola perris como va?     '
print(greet_blanks.lstrip()) # la salida es 'Hola perris como va?        '
print(greet_blanks.rstrip()) # la salida es '       Hola perris como va?'
print(greet_blanks.strip()) # la salida es 'Hola perris como va?'


#startswith() ... sirve para buscar si una cadena de texto comienza con X cadena o caracter
#devuelve el resultado en booleano
#ejemplo

texto = 'Por favor'
print('Comienza con la cadena "Por"', texto.startswith('Por')) #La salida será True
print('Comienza con la letra "p"', texto.startswith('p')) #La salida será False

#ejemplo de extracción de datos de un email con .find() y slice

data = 'From nickswilliam2012@gmail.com Lun 02 de Oct 2023 01:38:16'

arroba = data.find('@')
espacio = data.find(' ', arroba) #buscará un espacio desde la posición en donde se encuentra el '@'
tipo_email = data[arroba+1 : espacio] #hará un split de la información desde el arroba+1 es decir la 'g' hasta antes del espacio, es decir 'm'

print(tipo_email) #en este caso la salida será "gmail.com" 