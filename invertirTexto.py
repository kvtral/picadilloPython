""" def inverso (cadena):
    inversion = ""
    largo = len (cadena) * -1
    i = -1
    while i >= largo:
        inversion += cadena[i] 
        i -= 1
    return (inversion)

x = input ("Invierte el siguiente texto :")
print (inverso (x)) """
""" 
def palindormo (cadena):
    temp = ""
    i = -1
    for x in cadena:
        temp += cadena[i]
        i -= 1
    for r, x in enumerate(cadena):
        if temp[r] != cadena [r]:
            return False
    return True

palabra = input ("ingrese una palabra: ")
if (palindormo(palabra)):
    print (palabra, "es palindromo")
else:
    print (palabra, "NO es palindromo") """


""" def quitarVocales (cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    txt =""
    v = 0


    for c in cadena:
        if c not in vocales:
            txt += c
    print (txt)

quitarVocales ("Periquito") """

