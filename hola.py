from random import *

salto = randint(0,10)
resta = randint(0,10)
if resta == salto: 
    print("Te rompiste la pierna")
elif salto - resta > 0:
    print(f"Saltaste {salto - resta} metros")
else:
    print(f"Saltaste {salto - resta} metros, rompiste las leyes de la fisica")