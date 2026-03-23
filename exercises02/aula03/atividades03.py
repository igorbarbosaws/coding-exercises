# Ex 01: Criar um algoritmo em Python que receba um filme e mostre estilo e o diretor. Criem funções para apresentar a informação. Escolha ao menos 5 filmes.

print(f"1. Rocky Balboa\n2. O Masacre da Serra Elétrica\n3. Harry Potter\n4. O Agente Secreto")
filme = input("Escolha um dos filmes: ").lower()

match(filme):
    case "rocky balboa":
        print("Filme de superação, dirigido pelo astro Sylvester Stallone")
    case "o masacre da serra eletrica":
        print("Filme clássico de terror, direção de Tobe Hooper.")
    case "harry potter":
        print("Filme de fantasia, escrito por J. K. Rowling.")
    case "o agente secreto":
        print("Filme nacional, concorreu ao oscar com a direção de Kleber Mendonça Filho")
    case _:
        print("Filme inválido")

# Ex 02: Criar um algoritmo em Python que receba o tamanho de 3 lados e informe se eles formam um triângulo. Caso sim, informe qual o tipo de triângulo (equilátero, isósceles ou escaleno)

lado1 = int(input("Digite o 1º lado do triangulo: "))
lado2 = int(input("Digite o 2º lado do triangulo: "))
lado3 = int(input("Digite o 3º lado do triangulo: "))

if(lado1+lado2 >lado3 and lado2+lado3 > lado1 and lado1+lado3 > lado2):
    print("Isso de fato é um triangulo.")
    if(lado1 == lado2 and lado1 == lado3):
        print("Esse é um triangulo equilátero.")
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("Esse é um triangulo isoceles.")
    else:
        print("Esse é um triangulo escaleno.") 
else:
    print("Isso não é um triangulo")

# Ex 03: Criar um algoritmo em Python que receba um mês e informe a estação do ano (verão, primavera, inverno ou outono).

print(f"Alguns preferem o frio, outros o calor ...")
mes = input("Me informe um mês do ano: ").lower()

match(mes):
    case "dezembro" | "janeiro" | "fevereiro":
        print("Calorão! Estamos no verão.")
    case "março" | "abril" | "maio":
        print("As folhas caem, o Outono chegou!")
    case "junho" | "julho" | "agosto":
        print("Que frio, mas antes o frio do Inverno do que morrer de calor.")
    case "setembro" | "outubro" | "novembro":
        print("Quão bela é a primavera!")
    case _:
        print("Opção inválida.")

