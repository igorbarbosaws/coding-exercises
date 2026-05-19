# class Lapis:
#     def __init__(self, modelo, cor, tamanho, ponta):
#         self.modelo = modelo
#         self.cor = cor
#         self.tamanho = tamanho
#         self.ponta = ponta
#         print(self.modelo, self.cor, self.tamanho, self.ponta)

#     def riscar(self):
#         print("Está riscando")

#     def pintar(self):
#         print("Está pintando")

#     def escrever(self):
#         print("Está escrevendo")


# modelo = input("Informe o modelo: ")
# cor = input("Informe a cor: ")
# tamanho = input("Informe o tamanho: ")
# ponta = input("Informe a ponta: ")
# objeto = Lapis (modelo, cor, tamanho, ponta)
# objeto.riscar()

# class Bola:
#     def __init__(self, cor, marca):
#         self.cor = cor
#         self.marca = marca
#         print("Valores iniciais: ", self.cor, self.marca)
#     def mudarCor(self):
#         self.cor_bola=input("Informe uma nova cor: ")
#         print(f'A cor anterior é: {self.cor}')
#         print(f'A nova cor é: {self.cor_bola}')

# objeto = Bola("Branca", "Penalty")
# objeto.mudarCor()

from pessoa import Pessoa

nome = input("Digite seu nome: \n")
idade = input("Digite sua idade: \n")
altura = input("Digite sua altura: \n")
peso = input("Digite seu peso: \n")

objeto = Pessoa(nome, idade, altura, peso)

Pessoa('Ana', 24, 1.68, 56)
Pessoa('Igor', 28, 1.78, 70)
Pessoa('Luisa', 2, 0.95, 20)