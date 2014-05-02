from sys import argv
from os.path import exists

script, from_file, to_file = argv
#se pasan en secuencia los dos strings a reemplazar
print "Copying from %s to %s" % (from_file, to_file)

#Abre el archivo y lo lee
in_file = open(from_file)
indata = in_file.read()
#Lo anterior se puede hacer en una sola linea de codigo que queda
#in_file = open(from_file, 'r')

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
#verifica si el archivo existe
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
#Abre el archivo y por la w, lo escribe
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
#cierra
