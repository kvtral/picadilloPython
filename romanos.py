import sys, re

def checks(argum,patron):
 #http://docs.python.org/library/re.html
 #re.search returns None if no position in the string matches the pattern
 if re.search(patron, argum):
  print ('Error: lo ingresado no es un numero decimal')
  sys.exit(1)

roma = {1000: 'M',900:'CM',500:'D',400:'CD', 100:'C',90:'XC', 50:'L',40:'XC',10: 'X',9:'IX',5: 'V',4:'IV',1:'I'}
claves = sorted((roma.keys()))
claves.reverse()
print (claves)


numero = 1234
patron = r'[^\0-9]'
checks(str(numero),patron)


if numero >= 4000:
 print ('Error: numero demasiado grande para conversion')
 sys.exit(2)
salida = ''

for clave in claves:
 while clave <= numero:
  salida = salida + roma[clave]
  numero = numero - clave
print (salida)