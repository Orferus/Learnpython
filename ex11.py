#el rawinput sirve para capturar datos
print "cuantos anios tienes?",
age = raw_input()
print "que tan alto eres?",
height = raw_input()
print "cuanto pesas?",
weight = raw_input()

print "entonces, tienes %r anios, mides %r metros y pesas %r kilos." % (
    age, height, weight)
