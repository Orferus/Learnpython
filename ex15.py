from sys import argv

script, filename = argv

txt = open(filename) #el comando open abre el archivo

print "Aqui esta el archivo %r:" % filename
print txt.read() #read lee el archivo

print "Dame el nombre del archivo otra vez:"
file_again = raw_input("> ") #Guarda la direccion del archivo para poder abrirlo abajo

txt_again = open(file_again)

print txt_again.read()
#Vuelve a leer el archivo asignado en la nueva variable txt_again 
