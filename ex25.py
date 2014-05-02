def break_words(stuff):
    """This function will break up words for us."""
    #parte la cadena cada vez que encuentra un espacio
    words = stuff.split(' ') 
    return words

def sort_words(words):
    """Sorts the words.""" #Devuelve el arreglo de palabras
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) #Halla el valor del arreglo en la posicion cero
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    #Halla el valor del arreglo en la ultima posicion
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    #Parte la cadena con la primera funcion y la manda como parametro
    #A la segunda que devuelve el arreglo de palabras
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    #Imprime la primera posicion y la ultima
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
