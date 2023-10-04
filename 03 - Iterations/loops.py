#como encontrar el numero más grande
num_grand = -1
print('Numero antes:', num_grand)

for num in [9, 41, 12, 3, 100, 78] :
    if num > num_grand:
        num_grand = num
    print(num_grand)

print('Numero despues:', num_grand)

flag = 0
print('Antes', flag)
for thing in [0, 12, 30, 40, 50, 6]:
    flag+=1
    print(flag, thing)

print('Despues', flag)

#sumar el total de un array
numeros = [1, 50, 40, 18, 23]

zork = 0

print('Valor sin total:', zork)

for numero in numeros:
    zork = zork + numero

print('Total:', zork)

#promedio de un array

count = 0
sum = 0

for numero in numeros:
    count += 1
    sum = sum + numero
print('El promedio de la suma de los 5 numeros es:', sum/count)

#buscar el valor 3 en un array

found = False
print('Antes', found)

for value in [9, 4, 31, 22, 3, 40]:
    if value == 3:
        found = True
    print(found, value)
print('Despues', found)


#encontrar el numero más pequeño de un array
smallNum = None

for num in [9, 41, 12, 2, 74, 15]:
    if smallNum is None:
        smallNum = num #en estas lineas comprobamos que el flag sea none, de ser así, asignará el primer valor del array como el valor más pequeño
    elif num < smallNum:
        smallNum = num #luego comprobará cual de todos los valores del array es el más pequeño. y lo guarda en la variable smallNum
print('El numero más pequeño es:', smallNum) #aqui imprimirá dicho valor

#el operador is y is not es como el equivalente a === y !== respectivamente. Comparan valor y tipo y devuelven true o false
#generalmente el uso de is se limita a booleanos (true, false) o del tipo 'None'
#Ejemplo

if 6 is 6.0:
    print(True, 'Verdadero')
else:
    print(False, 'Falso')