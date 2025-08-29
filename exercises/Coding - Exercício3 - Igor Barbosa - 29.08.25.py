print("Qual a sua nota na primeira avaliação? ")
n1 = float(input())
print("Qual a sua nota na segunda avaliação: ")
n2 = float(input())
print("Qual a sua nota no seminário? ")
n3 = float(input())
media = n1 + n2 + n3 / 3
print("A sua média é: " + str(media))
if media >= 7:
    print("Aprovado, muito bem! ")
else:
    print("Reprovado, se esforce um pouco mais ... ")
