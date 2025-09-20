# 01
cupom = input("Digite seu cupom promocional recebido na aula ")
aula1 = "aula1"
aula2 = "aula2"

if cupom == aula1:
   print(' seu desconto é de 15%.')
elif cupom == aula2:
    print(' Seu desconto é de 10%.')
else:
    print(' Seu desconto é de 05%')
# 02  
idade = input("Olá! Qual a sua idade? ")
idade = int(idade)

if idade < 18:
   print('Você é menor de idade.')
elif idade >= 18 and idade < 65:
    print('Você é adulto.')
else: 
    print('Você é idoso.')
# 03
tempo = input('Está fazendo sol?')

if(tempo == 'sim'):
  dinheiro = input('Você tem dinheiro?')
  if (dinheiro == 'sim'):
    print('Vamos à praia?')
  else:
    print('Vá ligar o ventilador.')
else:
  print('Vamos assistir Netflix?')
# 04
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = peso / (altura ** 2)

print("Seu IMC é: %4f" % imc)

if imc < 16:
  print("Magreza grave")
elif imc < 17:
  print("Magreza moderada")
elif imc < 18.5:
  print("Magreza leve")
elif imc < 25:
  print("Saudável")
elif imc < 30:
  print("Sobrepeso")
elif imc < 35:
  print("Obesidade Grau I")
elif imc < 40:
  print("Obesidade Grau II (severa)")
else:
  print("Obesidade Grau III (mórbida)")
# 05