i = 0
numbers = []
#bucle tipo while que va a llenar el arreglo con el valor de i hasta que sea < 6, es decir hasta 5
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
#Agrega el elemento al final de la lista
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

#imprime toda la lista con un for
print "The numbers: "
for num in numbers:
    print num
