#leear archivo con input, entrada de texto
#para contar la cantidad de lineas que tiene ese archivo con la palabra "subject".
fname = input('Ingrese nombre de archivo:')
try:
    fhand = open(fname)
except:
    print('El archivo ingresado, no puede ser leido, o no existe en el directorio :(')
    quit() #cerrar el programa


count = 0
for line in fhand:
    if line.startswith('Subject'):
        count +=1

print('El archivo', fname, 'posee un total de', count, 'líneas de texto con la palabra "subject" al comienzo del mismo.')