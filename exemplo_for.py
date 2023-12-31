# Salvando o texto como um tipo de dado.
texto = """Python é uma linguagem de programação de alto nível, [5] interpretada de script, 
imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada 
por Guido van Rossum em 1991. [1] Atualmente, possui um modelo de desenvolvimento 
comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software 
Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações 
formais, a linguagem, como um todo, não é formalmente especificada. O padrão na pratica 
é a implementação CPython. A linguagem foi projetada com a filosofia de enfatizar a 
importância do esforço do programador sobre o esforço computacional. Prioriza a
 legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe 
 concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e 
 frameworks desenvolvidos por terceiros."""

# Inicializar a variavel que armazerá o novo texto.
novo_texto = ""

# Transformando o texto em uma lista de palavras.
lista_de_palavras = texto.split(' ')

# Usamos o for com um iterador para varrer a lista de palavras.
for indice in range(len(lista_de_palavras)):
    if lista_de_palavras[indice] == "Python":
        lista_de_palavras[indice] = "Fython"

# Usou o for com um gerador para voltar a lista de palavras modificada para texto.
for palavra in lista_de_palavras:
    novo_texto = novo_texto + palavra + " "

print(novo_texto)