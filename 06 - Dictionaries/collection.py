purse = dict() #crear un diccionario vacio
purse['dinero'] = 12
purse['caramelos'] = 3
purse['pañuelos'] = 2
print(purse)

#diccionarios literales

auto = {
    'año': 2009,
    'fabricante': 'Volkswagen',
    'motor': 'V8',
    'modelo': 'Suran senda'
}

print(auto)

#se pueden sumar elementos a un objeto en clave numerica, por ejemplo, de la siguiente manera

auto['año'] = auto['año'] + 2
print(auto)

#rastrear si un elemento pertenece o no a un diccionario
print('clavija' in auto) #esto devolverá False, ya que la clave 'clavija' no existe en este diccionario

#como contar elementos repetidos de una lista y guardarlos en un diccionario como cantidades de ese elemento
counts = dict()
nombres = ['Gustavo', 'Silvia', 'Pablo', 'Graciela', 'Pablo', 'Graciela', 'Silvia','Gustavo','Graciela','Silvia','Pablo', 'Graciela']
for nombre in nombres:
    if nombre not in counts: #aqui pregunta si el nombre no se encuentra dentro del objeto, que lo agregue y le asigne el valor 1
        counts[nombre] = 1
    else: 
        counts[nombre] = counts[nombre] + 1 #caso contrario, si ya existe, que le agregue 1 a la cuenta

print(counts)

#otra forma de hacerlo, es con el metodo get()

count = dict()
for name in nombres:
    count[name] = count.get(name, 0) + 1 #de esta forma indicamos que busque en el diccionario la clave valor con el nombre, si no la tiene, la crea y le agrega el valor 1, si ya la tiene: le sigue sumando 1
print(count)