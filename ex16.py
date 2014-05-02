from sys import argv
#Se reciben dos parametros
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
#La w sirve para entrar en modo escritura.
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
#Aqui captura tres lineas nuevas para agregar ya que el archivo
#Esta abiero para escritura
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#Aqui se agregan las 4 lineas
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#Se cierra el documento
print "And finally, we close it."
target.close()
