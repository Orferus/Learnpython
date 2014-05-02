from sys import argv

script, user_name = argv
prompt = '> '
#se usa el prompt para indicar que se esta esperando una orden
print "Hola %s, yo soy %s script." % (user_name, script)
print "Me gustaria que respondieras unas preguntas."
print "Te caigo bien %s?" % user_name
likes = raw_input(prompt)

print "Donde vives %s?" % user_name
lives = raw_input(prompt)

print "Que clase de computador tienes?"
computer = raw_input(prompt)

print """
Entonces, dijiste que %r acerca de si te caigo bien.
Vives en %r.  No estoy seguro donde queda eso.
Y tienes un computador %r .  Excelente.
""" % (likes, lives, computer)
