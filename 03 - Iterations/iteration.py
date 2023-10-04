#bucle while

n1 = 5
while n1 > 0:
    print(n1)
    n1 -= 1

print('Terminado')

#los dos ejemplos de abajo, son bucles del tipo indefinidos... ya que no sabemos cuando finalizaran, a menos que se realice una interrumpción o break
while True:
    line = input('Ingrese una palabra:')
    if line == 'hecho':
        break #corta con el bucle del ciclo
    print(line)
print('Finalizado')

while True:
    line = input('> :')
    if line == '#':
        continue #la palabra continue, vuelve al bloque inicial while en este caso... es decir salta de este punto al inicio nuevamente
    if line == 'done':
        break
    print(line)
print('Terminado')


#bucle definido
print('Bucle definido: \n')
for i in [5,4,3,2,1] :
    print(i)
print('Finalizado')

amigos = ['Bassi', 'Feto', 'Facu', 'Cami']

for amigo in amigos:
    print('Hola perris', amigo)
print('finalizado')