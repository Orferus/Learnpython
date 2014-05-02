#Se asigna el valor de la variable carros
carros = 100
#Se asigna el valor de la variable espacio en los carros
espacio_en_los_carros = 4.0
#Se asigna el valor de la variable conductores
conductores = 30
#Se asigna el valor de la variable pasajeros
pasajeros = 90
#Se asigna el valor de la variable carros no conducidos que corresponde al valor de los carros menos el de los conductores
carros_no_conducidos = carros - conductores
#Se asigna el valor de la variable carros conducidos que tiene el mismo valor de la cantidad de conductores
carros_conducidos = conductores
#Se asigna el valor de la variable capacidad de transporte que corresponde al valor de los carros conducidos por el especio en los carros.
#Como la variable espacio entre carros es float, el resultado se da en float.
capacidad_transporte = carros_conducidos * espacio_en_los_carros
#Se asigna el valor de la variable promedio pasajero por carro
promedio_pasajeros_por_carro = pasajeros/ carros_conducidos


print "Hay", carros, "carros disponibles."
print "Solo hay", conductores, "conductores disponibles."
print "Habran ", carros_no_conducidos, "carros libres hoy."
print "Podemos transportar", capacidad_transporte, "personas hoy."
print "Tenemos", pasajeros, "para transportar hoy."
print "Necesitamos poner ", promedio_pasajeros_por_carro, "pasajeros por carro."

#probando como calculadora

print "El numero de carros totales mas el numero de pasajeros es de" , carros + pasajeros

