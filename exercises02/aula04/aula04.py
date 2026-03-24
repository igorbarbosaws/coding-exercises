#While

numero = 0
somaPar = 0
somaImpar = 0

while numero <=100:
    print(numero,"\n")
    numero+=1
    if(numero %2 == 0):
        somaPar+=numero
    else:
        somaImpar+=numero

print(f"A soma dos pares é {somaPar}")
print(f"A soma dos impares é {somaImpar}")

#For
palavra = "Igor Barbosa"
cont = 1

for letra in palavra:
    print(f"{cont}ª letra: {letra}\n")
    cont+=1

#Ex 2
for i in range(5):
    print(f"Numero {i}\n")