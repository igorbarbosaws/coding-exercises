# Ex 01: 

soma_impares = 0
quantidade_impares = 0

for numero in range(1, 1001, 2):
    soma_impares += numero
    quantidade_impares += 1

print(f"A soma dos números ímpares entre 0 e 1000 é: {soma_impares}")
print(f"A quantidade de números ímpares nesse intervalo é: {quantidade_impares}")


# Ex 02:

numeros = []

print("Digite 10 números abaixo:")

for i in range(1, 11):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

maior_numero = max(numeros)
menor_numero = min(numeros)

print("-" * 30)
print(f"O maior número digitado foi: {maior_numero}")
print(f"O menor número digitado foi: {menor_numero}")

# Ex 03:

pares = 0
impares = 0

print("Informe 5 números:")

for i in range(1, 6):
    num = int(input(f"Informe o {i}º número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("-" * 30)
print(f"O total de números pares é: {pares}")
print(f"O total de números impares é: {impares}")

# Ex 04:

cantores = []

print("Quais os seus 5 cantores favoritos?")

for i in range(1, 6):
    nome = input(f"Digite o nome do {i}º cantor: ")
    cantores.append(nome)

cantores.reverse()

print("-" * 30)
print("Lista dos seus cantores favoritos em ordem invertida:")

for cantor in cantores:
    print(cantor)
