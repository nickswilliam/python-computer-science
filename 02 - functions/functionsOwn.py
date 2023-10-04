def entrada():
    saludo = input('Ingrese 2 letras para definir su saludo en diferentes lenguajes. \n Ejemplo: es(español), en(ingles), fr(frances). \n')
    return saludo

def greet(lang): #parametro de la función = lang
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    elif lang == 'en':
        print('Hello')
    else:
        print('No hay traducción disponible para la entrada ingresada. :(')


greet(entrada())

#return values from a function

def greetings():
    return "Hello"

print(greetings(), 'Nicks')

def greetReturn(lang):

    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    elif lang == 'en':
        return 'Hello'
    else:
        return 'No hay saludos para la entrada mencionada :('



print(greetReturn(entrada()))


#multiple parametros en una función
#ej:
valor1 = int(input('Ingrese el primer número:'))
valor2 = int(input('Ingrese el segundo número:'))

def suma(a, b):
    return a + b

print(suma(valor1, valor2))
    