my_name = 'David'
my_age = 21 # not a lie
my_height = 1.70 # metros
my_weight = 64 # kilogramos
my_eyes = 'Cafe'
my_teeth = 'Blancos'
my_hair = 'Negro'

print "Hablemos sobre %s." % my_name
print "El mide %d metros." % my_height
print "El pesa %d kilos." % my_weight
print "De hecho, no estan pesado."
print "El tiene ojos %s y cabello %s ." % (my_eyes, my_hair)
print "Sus dientes son usualmente %s dependiendo del cafe." % my_teeth

# En esta linea lo que sea hace es pasar el parametro que se desea imprimir en una secuencia
#Es importa resaltar que cuando se imprime el valor del peso, se omite la parte decimal porque no tiene la %r
print "Si sumo %d, %d, y %d obtengo %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
