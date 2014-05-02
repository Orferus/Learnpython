x = "Hay %d tipos de personas" % 10
binary = "binarios"
do_not = "no"
y = "Aquellas que saben %s y las que %s." % (binary, do_not)

print x
print y
#si la variable que se va a reemplazar es un string, la %r pone comillas
print "He dicho que: %r." % x
print "Tambien dije que : '%s'." % y

hilarious = False
joke_evaluation = "No es eso gracioso?!  %r" 

print joke_evaluation % hilarious

w = "Este es el lado izquierdo de..."
e = "un String con un lado derecho."
# el + en strings, concatena dos cadenas. 
print w + e
