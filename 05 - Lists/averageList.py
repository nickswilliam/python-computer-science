numlist = list()
while True:
    inp = input('Ingrese un numero:')
    if inp == 'hecho':
        break
    valor = float(inp)
    numlist.append(valor)

average = sum(numlist) / len(numlist)

print('El promedio de los números ingresados es:', average)