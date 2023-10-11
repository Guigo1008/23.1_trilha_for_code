class Padeiro:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 0
        self.paes = 0
        pass

    def assar_paes(self, quantidade):
        if quantidade > 6:
            print("A capacidade maxima do forno eh 6.")
        else:
            self.paes += quantidade
        pass

class Cliente:
    def __init__(self, nome, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro
        self.paes = 0
        pass

    def comprar_paes(self, quantidade, padeiro):
        preco_pao = quantidade * 0.5
        if quantidade > padeiro.paes:
            quantidade = int(input(f"So ha {padeiro.paes} paes disponiveis. Quer comprar quantos?"))
            if quantidade > padeiro.paes:
                print("Nao ha paes suficientes para a compra.")
            else:
                self.dinheiro -= preco_pao
                self.paes += quantidade
                padeiro.dinheiro += preco_pao
                padeiro.paes -= quantidade
                print(f"Compra realizada com sucesso. Agora, {self.nome} tem {self.paes} paes e \
{self.dinheiro} reais. {padeiro.nome} tem {padeiro.paes} paes e {padeiro.dinheiro} reais.")
            
        elif self.dinheiro < preco_pao:
            print("Voce nao tem dinheiro suficiente para a compra.")
        else:
            self.dinheiro -= preco_pao
            self.paes += quantidade
            padeiro.dinheiro += preco_pao
            padeiro.paes -= quantidade
            print(f"Compra realizada com sucesso. Agora, {self.nome} tem {self.paes} paes e \
{self.dinheiro} reais. {padeiro.nome} tem {padeiro.paes} paes e {padeiro.dinheiro} reais.")
        pass

padeiro1 = Padeiro('Joaquim')
padeiro1.assar_paes(6)
cliente1 = Cliente('Maria', 10)
cliente1.comprar_paes(7, padeiro1)