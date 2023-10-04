text = "Hola soy raul el plomero"
text_split = text.split() #cortará cada uno de los elementos de la cadena, que se separan con espacios, y los guardará en una lista [Hola, soy, raul, el, plomero]

print(text_split)

#también se puede hacer split o división, con caracteres especificos
#ejemplo

linea = 'Hola.como.estas.todo.bien?.Que.es.de.tu.vida?'
linea_split = linea.split('.') #le pasamos como argumento, '.' el caracter .

print(linea_split)

#imprimir del archivo 'mbox-short.txt0' solamente los mails de los destinatarios

fhand = open('../04 - Reading files/mbox-short.txt')
for line in fhand:
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[1])

#imprimir el host de cada uno de los destinatarios que nos envian mail

fhand2 = open('../04 - Reading files/mbox-short.txt')
for line in fhand2:
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    pieces = email.split('@') #aquí separamos del email el @ para separar los elementos
    print(pieces[1]) #imprimimos en la posición 1, ya que en la 0 es lo anterior al @ y en la 1 es la información del host
    
    