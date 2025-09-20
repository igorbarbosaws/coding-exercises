# # 01
numero = int(input("Digite um número"))

if(numero > 0):
    print("O número é positivo.")
elif(numero < 0):
    print("O número é negativo.")
else:
    print("O número é neutro.")

# # 02
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a == b:
    print("Os números são iguais.")
else:
    print("Os números são diferentes")
    
# # 03
nome = input("Qual é o seu nome?")
if (nome == "Optimus Prime"):
    print("Bem-vindo, você é um guerreiro Cybertron")
else:
    print("Seu nome é ", nome)
    
# # 04
idade = input("Olá! Qual a sua idade? ")
idade = int(idade)

if idade < 12:
   print('Você é uma criança.')
elif idade >= 12 and idade <= 18:
    print('Você éum adolescente.')
elif idade >= 19 and idade <= 24:
    print('Você é jovem.')
elif idade >= 25 and idade <= 40:
    print('Você é adulto.')
elif idade >= 41 and idade <= 60:
    print('Você tem meia idade.')
else: 
    print('Você é idoso.')