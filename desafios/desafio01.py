# Desafio 01 - Cervejaria do Ingo
# Autor: Ingo Barboza
print("Olá! Seja bem vindo a Cervejaria do Ingo!")
print("Aqui você encontra as melhores cervejas do Brasil.")
print("Escolha sua cerveja favorita pelo número:")

opcoes = "1-Antártica R$6.00; 2-Skol R$6.50; 3-Brahma R$8.20; 4-Sol R$8.25; 5-Nortenha R$16.80; 6-Proibida R$4.80; 7-Devassa R$5.90; 8-Heineken R$9.00"
opcoes = "1-Antártica R$6.00; 2-Skol R$6.50; 3-Brahma R$8.20; 4-Sol R$8.25; 5-Nortenha R$16.80; 6-Proibida R$4.80; 7-Devassa R$5.90; 8-Heineken R$9.00"

cerveja = input(f"{opcoes}\nSua escolha (1-8): ")

try:
    q = float(input("Quantas cervejas você deseja? "))
except ValueError:
    print("Quantidade inválida. Por favor, insira um número.")
    exit()

nome = None
valor_unitario = 0.0

if cerveja == '1':
    nome = "Antártica"
    valor_unitario = 6.00
elif cerveja == '2':
    nome = "Skol"
    valor_unitario = 6.50
elif cerveja == '3':
    nome = "Brahma"
    valor_unitario = 8.20
elif cerveja == '4':
    nome = "Sol"
    valor_unitario = 8.25
elif cerveja == '5':
    nome = "Nortenha"
    valor_unitario = 16.80
elif cerveja == '6':
    nome = "Proibida"
    valor_unitario = 4.80
elif cerveja == '7':
    nome = "Devassa"
    valor_unitario = 5.90
elif cerveja == '8':
    nome = "Heineken"
    valor_unitario = 9.00
else:
    print("Opção de cerveja inválida! Por favor, escolha um número de 1 a 8.")
    exit()

valor_total = valor_unitario * q

print("-" * 30)
print(f"Pedido: {int(q)}x {nome}")
print(f"Valor Unitário: R$ {valor_unitario:.2f}")
print(f"Valor Total: R$ {valor_total:.2f}")
print(f"\nO total para {int(q)} cerveja(s) de {nome} é de R$ {valor_total:.2f}.")
print("-" * 30)