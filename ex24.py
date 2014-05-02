print "Let's practice everything."
#Se utlizan \' para que python no confunda esas comillas con el fin del string
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
#Tambien se hace doble backslash, saltos de linea y tabulaciones.

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#Se utilizaron triples comillas para escribir mucho.
print "--------------"
print poem
print "--------------"

#Se hace matematica y se asigna valor a una variable
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#Se crea una funcion que recibe un parametro
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
#se igualan tres variables a los retornos de la funcion secret_formula.
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
#se reescribe el valor inicial 
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
