fhand = open('test.txt')
print(fhand) #la invocación de la función open, simplemente nos retornará el tipo de archivo y en que codificación está el mismo.
#<_io.TextIOWrapper name='mbox-short.txt' mode='r' encoding='cp1252'> en este caso nos devuelve esto

#para leer un archivo usamos el bucle iterador for

for word in fhand:
    print(word) #nos imprimirá cada línea del archivo de texto

#contar el número de líneas del archivo con python

hand_count = open('test.txt')
count = 0
for line in hand_count:
    count = count + 1
print('Cantidad de lineas del archivo:', count)

#leer cantidad de caracteres de un archivo
hand_char = open('test.txt')
inp = hand_char.read() #esta declaración, leeará cada una de las cadenas de caracteres del archivo
print(len(inp), 'Cantidad de caracteres total') #con el len, veremos la longitud de caracteres en total del archivo
print(inp[:50]) #decimos que corte el texto desde el comienzo hasta la linea 50

#buscar dentro de un archivo
#buscamos si la primera linea del archivo comienza con la palabra "From:"

search_hand = open('mbox-short.txt')
for line in search_hand:
    if line.startswith('From:'):
        print(line) #nos va a imprimir cada vez que encuentre la palabra From: con una linea nueva \n abajo

#de otra forma mas correcta puede ser, hacerlo con rstrip()
search2 = open('mbox-short.txt')
for line in search2:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)


#como usar el "in" y el "continue" para seleccionar lineas de texto del archivo
print('\n')
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not '@uct.ac.za' in line: #en este caso le estamos diciendo que si no encuentra en el archivo "@uct.ac.za" en cada linea, que continue iterando el bucle...
        continue
    print(line) #aqui estará imprimiendo las lineas que contengan "@uct.ac.za"