import time

# Pass - Deixa o fluxo do while continuar
# Break - Interrompe o fluxo do while
# Continue - Interrompe apenas a iteração atual

c = 0
while True:

    if c == 4:
        break
    
    print(c)
    time.sleep(1)
    c = c + 1
    

print(c)
print("Fui breakado.")