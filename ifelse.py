nota = float(input("Digite a nota >> "))

if nota >= 7.0:
    # Usei o aux dentro do escopo do nota mas ele deixa de existir fora do escopo
    aux = "Aprovado"
    print(aux)

elif nota >= 3.0:
    print("Recuperação")

else:
    print("Reprovado")

print(nota)

