def es_vocal (x):
    temp = ""
    for n in x:
        if n != "A" or n != "E" or n != "I" or n != "O" or n != "U":
            print (n)
            temp = temp + n
    
    return (temp)



text = input ("Ingrese un texto para quitar las vocales: ")

text = es_vocal(text.upper())
print (text)