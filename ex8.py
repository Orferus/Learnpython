formatter = "%r %r %r %r"
#formatter es un string que va a imprimir cuatro parametros
#al ser el formato tipo %r va a imprimir todas las cadenas que se le pasen
#como parametro con comillas.
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#Si se remueve algun parametro o solo se ponen 3 atributos en las cadenas que
#se van a reemplazar, bota un error. 
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
