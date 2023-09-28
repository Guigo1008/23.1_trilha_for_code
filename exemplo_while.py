# Vamos construir um cronometro com Python.

# Importanto biblioteca que interage com o sistema operacional.
import os
# Importando biblioteca que introduz o conceito de tempo no Python.
import time

segundo = 0
minuto = 0

while True:
    os.system('cls')
    if segundo == 60:
        segundo = 0
        minuto = minuto + 1
        
    if segundo < 10:
        print(f'0{minuto}:0{segundo}')
    else:
        print(f'0{minuto}:{segundo}')

    time.sleep(1)
    segundo = segundo + 1