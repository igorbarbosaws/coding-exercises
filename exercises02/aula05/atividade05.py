#Ex 01

notas = []

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

maior_nota = max(notas)
menor_nota = min(notas)

print(f"Notas registradas: {notas}")
print(f"Média final: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")

if media >= 7:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")

#Ex 02

saldo = 1000

print("Bem-vindo ao Senac Bank!")

while True:
    print("\Escolha uma opção:  ")
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")

    opcao = input("Opção desejada: ")

    if opcao == "1":
        print(f"Seu saldo é : R$ {saldo:.2f}")

    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: R$ "))
        if valor_saque > saldo:
            print("Erro: Saldo insuficiente para executar a operação.")
        elif valor_saque <= 0:
            print("Erro: Valor inválido para saque.")
        else:
            saldo -= valor_saque
            print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")

    elif opcao == "3":
        valor_deposito = float(input("Digite o valor do deposito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito realizado. Novo saldo: R$ {saldo:.2f}")
        else:
            print("Erro: Valor de deposito inválido.")
    
    elif opcao == "4":
        print("Obrigado pela paciência. Volte sempre!")
        break

    else:
        print("Erro: Opção inválida")