fruit = 'Manzana'

letra = fruit[3] #le indicamos que de la palabra Manzana, queremos la de indice 3, recorre: 0, 1, 2, 3 es la 'z'
print(letra)

#la función "len" nos devuelve el largo de una cadena string 

print(len(fruit), '\n')

index = 0

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

for letter in fruit:
    print(letter)


#contador de letras 'A' en la palabra "manzana"
count = 0

for letter in fruit:
    if letter == 'a':
        count += 1
print(count, 'Cantidad de "A"s en manzana')