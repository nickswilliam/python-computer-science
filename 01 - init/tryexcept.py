#El bloque try - except... intentará ejecutar código en el bloque 'try', comprobando si encuentra error en la compilación
#en caso de que encuentre un error saltará al bloque except, caso contrario, ejecutará lo que se encuentre dentro del bloque try
#esta declaración condicional, sirve para evitar que hayan bloques de codigo que puedan fallar
#y evitar que nuestro programa o ejecución se detenga completamente
string = 'Hola perri'

try:
    convert = int(string)
except:
    convert = 3

print('Primero', convert)


string = '1234'

try:
    convert = int(string)
except:
    convert = 3

print('Segundo', convert)

astr = 'Hi falopita'

try: 
    print('Hola que tal buen diaaa')
    istr = int(astr) #en este caso, desde esta linea hacia abajo, no ejecturá el código, ya que hay un error en el mismo
    print('tuki')
except:
    istr = -11

print('Terminamo:', istr)