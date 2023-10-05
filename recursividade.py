def fatorial(numero):
    fat = 1
    while numero > 1:
        fat *= numero
        numero -= 1
    return fat

def fatorial1(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial1(numero - 1)

print(fatorial1(5))