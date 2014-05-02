#Se definen funciones para las operaciones de
#Suma
def add(a, b):
    print "Sumando %d + %d" % (a, b)
    return a + b
#Resta
def subtract(a, b):
    print "Restando %d - %d" % (a, b)
    return a - b
#Multiplicacion
def multiply(a, b):
    print "Multiplicando %d * %d" % (a, b)
    return a * b
#Division
def divide(a, b):
    print "Dividiendo %d / %d" % (a, b)
    return a / b


print "Hagamos matematica con solo funciones!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Edad: %d, Altura: %d, Peso: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
