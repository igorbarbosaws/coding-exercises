# Executar uma frase (conjunto de string's)
def saudacao():
    print("Olá, mundo!")

saudacao()

# Executar uma expressão numérica
def quadrado(numero):
    return numero*numero

quadrado(2)
# Adicionar uma variável em uma função
# 1. dobrar um valor
def dobro(numero):
    return numero*2
valor = int(input("Digite um número: "))
print("O dobro é:  ", dobro(valor))

# 2. área de um retangulo
def area_retangulo(base, altura):
    return base*altura
print("Área : ", area_retangulo(5,3), "m²")

# 3. conversor de temperatura
def celsius_fahrenheit(celsius):
    return (celsius*9/5)+32
temp = float(input("Digite a temperatura em Celsius: "))
print(f'{temp} °C = {celsius_fahrenheit(temp):.1f}°F')

# ou, apenas chamar a função com o valor a ser convertido em parâmetro
def celsius_fahrenheit(celsius):
    return (celsius*9/5)+32

celsius_fahrenheit(30)

# Adicionar condicionais dentro da função
# 1. if
numero = int(input("Digite um número: "))
def imprimeQuadrado(numero):
    if numero==1:
        return
print("%d\t"%(numero*numero))

# 2. for
def quadrado(numero):
    return numero*numero
tamanho = 6
numQuadrado = 0

for i in range(tamanho):
    numQuadrado = quadrado(i)
    print("%d\t"%numQuadrado)

# 3. if e else
def calcular_media(n1,n2):
  media = (n1+n2)/2
  
  if media >= 7:
    return f'Média {media:1f} - Aprovado'
  else:
    return f'Média {media:1f} - Reprovado'
print(calcular_media(8.0,6.5))

# Importar bibliotecas nativas do Python
import math
numero = float(input("Informe um número para calcular a sua raiz: "))
raiz = math.sqrt(numero)

print("Resultado: %.1f"%raiz)