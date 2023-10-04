x = 21

if x < 10:
    print('Small number')
if x > 20:
    print('Big number')
print('end')

print('Block while: \n')


n = 5

while n > 0:
    print(n)
    n -= 1
print('Blastoff!')

print('Expressions: \n')

word = 'Hello there'
numb = 1
temp = 98.6

print(type(word))
print(type(numb))
print(type(temp))

na = 20
nb = 5
stringNumber = '123'
print(int(stringNumber))

'la palabra reservada int convierte un numero flotante a un entero y float, un entero en un flotante'
'la division entre 2 numeros fuerza a que el resultado sea de un numero flotante, por más que el resultado devuelva un numero entero'
print(int(na/nb))

'la palabra reservada input es para ingresar texto u otros objetos de entrada'
name = input('Quien so vo?: ')
print('Welcome', name)