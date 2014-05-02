people = 20
cats = 30
dogs = 15

#la condicion que people sea menor que cats se cumple se hace lo que esta dentro del if
if people < cats:
    print "Too many cats! The world is doomed!"

#La condicion no se cumple por lo cual no se entra al if
if people > cats:
    print "Not many cats! The world is saved!"

#La condicion no se cumple por lo cual no se entra al if
if people < dogs:
    print "The world is drooled on!"

#la condicion se cumple, entra al if e imprime
if people > dogs:
    print "The world is dry!"

dogs += 5
# Con el nuevo valor de dogs, se cumple la condicion y se entra al if
if people >= dogs:
    print "People are greater than or equal to dogs."

# La condicion se cumple, entra al if
if people <= dogs:
    print "People are less than or equal to dogs."

# Se cumple, imprime. 
if people == dogs:
    print "People are dogs."
