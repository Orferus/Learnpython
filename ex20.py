from sys import argv

script, input_file = argv
#Se define una funcion para leer el archivo
def print_all(f):
    print f.read()

#el seek y el parametro numerico indican desde donde leer
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Primero, se imprime todo con la primera funcion:\n"

print_all(current_file)

print "Ahora, nos devolvemos hasta el caracter 0."

rewind(current_file)

print "Ahora, imprimamos tres lineas:"

#Esta funcion, recibe como parametro la linea que va a aumentar a medida que avanzamos (Current_line)
#Y el otro parametro es el archivo.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
