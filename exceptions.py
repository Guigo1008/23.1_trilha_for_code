def recebe_pin():
    senha = input("Digite seu PIN (Numero!) >> ")
    try:
        senha = int(senha)

    except:
        print("Senha invalida, tente digitar um numero!")
        senha = input("Digite seu PIN (Numero!) >> ")

    print(senha)

recebe_pin()