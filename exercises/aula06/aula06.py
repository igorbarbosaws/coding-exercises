# Imprimindo todos os números inteiros de 1 até 100.
i = 1
while i <= 100:
    print(i)
    i = i + 1
print("Fim do programa!")

# imprimindo todos os números inteiros de 1 até n.

# Imprimindo todos os números inteiros de 100 até 1.
i = 100
while i >= 1:
    print(i)
    i = i - 1
print("Fim do programa!")

# Imprimindo todos os números inteiros até um número definido.
n = int(input("Digite um número inteiro positivo: "))
i = 1
while i <+ n:
    print(i)
    i = i + 1
print("Fim do programa!")
# Criando um contador de números.
contador = 0
while contador < 4:
      print(f"Contador: {contador}")
      contador += 1

Estrutura de repetição: While
# a
total_geral = 0
i = 1
while i <= 3:
    qtd_acai = int(input("Informe a quantidade de açaís vendidos %d dia "))
    total = qtd_acai * 3.00
    print("Foram vendidos R$ %.2f de açaí." %total)
    i = i + 1
# b
total_geral = 0
i = 1
while i <= 3:
    qtd_acai = int(input("Informe a quantidade de açaís vendidos %d dia(s) atrás: "))
    total = qtd_acai * 3.00
    print("Foram vendidos R$ %.2f de açaí." %total)
    total_geral = total_geral + total
    i = i + 1

print("Foram vendidos R$ %.2f de açaí nos %d dias." %(total_geral,i-1))

#Contador 2
num = 100
contador_pares = 0
while num <= 200:
      if num % 2 == 0:
        contador_pares = contador_pares + 1
      num = num + 1
print(contador_pares)
    