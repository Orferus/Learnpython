# se define una funcion que recibe dos parametros
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# se obtienen los dos parametros de entrada
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# se define una funcion con un solo parametro de entrada
def print_one(arg1):
    print "arg1: %r" % arg1

# se define una funcion sin parametros de entrada
def print_none():
    print "No tengo argumentos."

#Se llaman las funciones dandole como parametros el numero que cada exige.
print_two("David","Valderrama")
print_two_again("David","Valderrama")
print_one("Uno!")
print_none()
