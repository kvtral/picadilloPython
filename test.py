# Uso de colorama y de importación de modulos desde otro archivo

import rut
from colorama import Fore, Style

x = input("Ingresa el rut sin digito verificador: ")
d = str(rut.verificador(x))

print (Fore.BLUE + x+ Fore.RED + "-"+ Fore.YELLOW +d)

