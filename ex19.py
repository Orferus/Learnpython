#se define la funcion que recibe dos parametros 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "Usted tiene %d quesos!" % cheese_count
    print "Usted tiene %d cajas de galletas!" % boxes_of_crackers
    print "Eso es suficiente para una fiesta!"
    print "Consigue una manta.\n"

#Se muestran diferentes formas de pasar los parametros a una funcion
print "Se pueden pasar los valores directamente:"
cheese_and_crackers(20, 30)


print "O se pueden usar variables desde nuestro script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "Podemos hasta hacer matematica dentro:"
cheese_and_crackers(10 + 20, 5 + 6)


print "Y se pueden combinar variables y matematicas :"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
