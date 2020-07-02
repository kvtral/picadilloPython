
# Script para mostrar funcionamiento de
# sys.argv 


import sys 

add = 0.0

# Tomamos el largo de los argumentos al ejecutar en linea de comandos
# ejemplo: :$python arg.py 1 2 3 4 5
n = len(sys.argv) 

# Recorremos y sumamos cada argumento hasta el largo n
for i in range(1, n):
    add += float(sys.argv[i]) 
 
print ("suma de los argumentos es  :", add) 
