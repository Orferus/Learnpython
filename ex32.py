the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# bucle tipo for
for number in the_count:
    print "This is count %d" % number

# bucle tipo for
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# por el %r se puede usar cualquier tipo de dato, es decir una lista con cualquier tipo de dato
for i in change:
    print "I got %r" % i

#Con una blucle se puede llenar una lista 
elements = []

# el rango va de 0 a 5 porque son seis posiciones
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append es un metodo para agregar al final de la lista 
    elements.append(i)
for i in elements:
    print "Element was: %d" % i
