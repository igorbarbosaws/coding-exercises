nomes = ["Ana", "Maria", "José"]
print(len(nomes))
#len é uma função embutida

#Função com valor padrão
def saudacao(nome="Visitante"):
    print(f"Olá,{nome}!")

saudacao()
saudacao("Igor")

#Função com valor variável
def operacoes(a,b):
    soma = a + b
    sub = a - b
    return soma, sub

resultado = operacoes(10,5)
print("Soma e Subtração: ", resultado)

#Função com *args
def somar_todos(*numeros):
    return sum(numeros)

print(somar_todos(1,2,3,4,5))

#Função com **kwargs
def info_pessoa(**dados):
    for chave, valor in dados.items():
        print(f"{chave}:{valor}")

info_pessoa(nome="Igor", cidade="Recife", curso="ADS")