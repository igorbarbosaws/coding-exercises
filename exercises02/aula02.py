# Declarar Variáveis
nome = "Igor"
idade = 28
altura = 1.78

#print("Bem vindo ",nome,"sua idade é",idade,"anos.")
print(f"Bem vindo, {nome}! Sua idade é {idade} anos.")

nome2 = input("Digite seu nome:")
idade2 = int(input("Digite sua idade: "))
altura2 = float(input("Digite sua altura: "))

#print ("Olá, ",nome2,"sua idade é",idade2,"anos e sua altura é",altura2)
print(f"Olá, {nome2}! Sua idade é {idade2} e sua altura é {altura2}")

# Operadores Aritiméticos:
# Soma + 
# Subtração -
# Multiplicação *
# Divisão /
# Resto % 

# Operadores Relacionais
# Maior que >
# Menor que <
# Igual ==
# Menor ou igual <=
# Maior ou igual >=
# Diferente !=

# Operadores Lógicos
# AND --> Retorna verdade somente se todos os testes logicos forem verdade
# OR --> Retorne falso somente se todos testes lógicos forem falsos
# NOT --> Inverte o valor lógico

# Calculo de Área

lado = int(input("Digite o lado do quadrado: "))
area = lado**2
print(f"A área do quadrado de lado {lado} é igual a: {area}.")

# Utilizando if e else

base=int(input("Digite a base do quadrilátero: "))
altura=int(input("Digite a altura do quadrilátero: "))

if (base == altura):
    print("É um quadrado")
    print(f"E sua área é {base**2}")
else:
    print("É um retângulo")
    print(f"E sua área é {base**altura}")

# Testando o Match Case

print(f"1. Senhor dos Aneis\n2. Bad Boys\n3.Jogos Vorazes")
filme = input("Digite seu filme favorito da lista: ").lower()

match(filme):
    case "senhor dos aneis":
        print("Um ótimo filme")
    case "bad boys":
        print("Filme de comédia interessante")
    case "jogos vorazes":
        print("Assista a noite sozinho")
    case _:
#         print("Filme inválido")

# Desafio 01

nome = input("Qual o seu nome:? ")
cidade = input("Qual a sua cidade?")

print(f"Bem-vindo, {nome}! Como está o seu dia em {cidade}?")

# # Desafio 02

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

soma = numero1 + numero3
print(f"A soma do primeiro número com o terceiro é: {soma}")

multiplicacao = numero1 * numero2
print(f"O resultado da multiplicação do primeiro pelo terceiro número é: {multiplicacao}")

# # Desafio 03

temperatura = int(input("Informe a temperatura em graus Celsius: "))

conversao = (temperatura*1.8) + 32

print(f"A temperatura em Farenheit é: {conversao}")

# # Desafio 04

print(f"1. Oficina G3\n2. SKANK\n3. Linking Park")
filme = input("Escolha uma das bandas: ").lower()

match(filme):
    case "oficina g3":
        print("Essa é uma banda de Rock Gospel")
    case "skank":
        print("Essa é uma banda de Pop/Rock ")
    case "jogos vorazes":
        print("Essa é a melhor banda de Rock da história!")
    case _:
        print("Banda inválida")

# Desafio 05

print(f"1. Sport\n2. Nautico\n3. Santa Cruz\n4. América")
filme = input("Escolha um dos times: ").lower()

match(filme):
    case "sport":
        print("O maior do estado, possui 46 títulos.")
    case "nautico":
        print("26 Títulos, morreu no Hexa.")
    case "santa cruz":
        print("29 Títulos, o mais coitado.")
    case "america":
        print("6 títulos, o eterno Mequinha")
    case _:
        print("Banda inválida")
