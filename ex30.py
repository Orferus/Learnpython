people = 30
cars = 40
buses = 15

#Cars es mayor que people asi que entra al if.
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

#Como no se cumple la condicion del if, entra al elif  
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

#Como la condicion se cumple entra al if 
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
