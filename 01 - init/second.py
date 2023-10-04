""" inp = input('Piso europeo?: ')
usf = int(inp) + 1

#print the floor in us value
print('El piso estadounidense es:', usf)  """

#if and else sentences... with indentation

num1 = int(input('Ingrese un numero:'))
num2 = int(input('Ingrese un número distinto:'))


if num2 > num1:
    print('El segundo numero es más grande que el primero')
elif num1 > num2 :
    print('El primer numero es mas grande que el segundo')
else :
    print('Ambos números son iguales')