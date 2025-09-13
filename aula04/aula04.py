# OPERADORES ARITIMÉTICOS
numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(modulo)
print(exponenciacao)

# OPERADORES DE ATRIBUIÇÃO
numero_1 = 5
numero_1 += 10

print(numero_1)

numero_2 = 5
numero_2 -= 2

print(numero_2)

# OPERERADORES DE COMPARAÇÃO
a = (20 * 5)
b = (21 * 5)
print(b > a)
print(b < a)
print(b >= a)
print(b <= a)   
print(b == a)
print(b != a)

numero_1 = 2
numero_2 = 4

soma = numero_1 + numero_2

if soma < 10:
    print("soma não é maior que 10")
else:
    print(print("soma é maior ou igual a 10"))
    
soma_1 = 7 + 8
soma_2 = 10 + 5

if soma_1 == soma_2:
    print("Os resultados são iguais")
else:
    print("Os resultados são diferentes")
    
# OPERADORES LÓGICOS
a = 5
b = 10

print((a > 0)  and (b == 0))
print((a > 0 ) and (b != 0))

a = 5
b = 10

print((a > 0)  or (b == 0))
print((a != 5) or (b == 0))

a = 5
b = 10

print(not(a < b))
print(not(a == b))

# COMANDOS CONDICIONAIS
a = int(input("Digite um número inteiro: "))
impar = ((a % 2) == 1)
if impar:
    print("Número ímpar")
    
print("Fim do programa")


a = int(input("Digite um número inteiro: "))
if (a % 2) == 1:
    print("Número ímpar")

print("Fim do programa")


a = int(input("Digite um número inteiro: "))
if (a % 2) == 0:
    print("Número par")
if (a % 2) == 1:
    print("Número ímpar")
    
print("Fim do programa")


a = int(input("Digite um número inteiro: "))
if (a % 2) == 0:
    print("Número par")
else:
    print("Número ímpar")
    
print("Fim do programa")    


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a > b:
    print("O maior número é", a)
else:
    print("O maior número é", b)


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a == b:
    print("Os dois números são iguais")
else:
    if a > b:
        print("O maior número é o primeiro")
    else:
        print("O maior número é o segundo") 
        
        
clima = input("Como está o clima hoje?")
if clima == "ensolarado" or "sol" or "quente":
    print("Vamos para a praia!")
else:
    print("Vamos assistir Netflix?")
    
    
tempo = input("Está fazendo sol hoje")
dinheiro = input("Você tem dinheiro?")
if (tempo == "sim" and dinheiro == "sim"):
    print("Vamos para a praia!")
else:
    print("Vamos assistir Netflix?")