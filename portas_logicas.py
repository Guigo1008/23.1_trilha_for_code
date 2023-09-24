# Como funcionam?
falta_mel = False
falta_pao = True

# AND
# Porta pessimista
if falta_mel and falta_pao:
    print("AND: Precisamos ir ao mercado!")

# OR
# Porta otimista
if falta_mel or falta_pao:
    print("OR: Precisamos ir ao mercado!")

# NOT
# Porta do contra
print(not True)