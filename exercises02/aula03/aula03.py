# # If

# idade = int(input("Digite sua idade: "))
# if(idade>18):
#     print("Você é maior de idade.")
# if(idade<18):
#     print("Você é menor de idade.")

# # Else

# age = int(input("Qual a sua idade? "))
# if age >= 18:
#     print("Vocêé maior de idade.")
# else:
#     print("Você é menor de idade.")

# # Elif

# idade = int(input("Informe a sua idade: "))
# if(idade>=18):
#     print("Você é maior de idade.")
# elif(idade<0):
#     print("Idade inválida.")
# else:
#     print("Você é menor de idade.")

# Switch Case c/ módulo

# from exemploModulo import *

# n1=float(input("Digite o 1º número: "))
# operacao=(input("Digite a operacação(+,-,*,/): "))
# n2=float(input("Digite o 2º número: "))

# match(operacao):
#     case '+':
#         soma(n1,n2)
#     case '-':
#         subtracao(n1,n2)
#     case '*':
#         multiplicacao(n1,n2)
#     case '/':
#         divisao(n1,n2)

from exemploModulo import *

print(f"1.Oficina G3\n2.CBJr\n3.GNR\n4.Linkin Park\n")
banda = input("Digite o nome de uma das bandas: ").lower()

match(banda):
    case "oficina g3" | "cbjr":
        nacional()
    case "gnr" | "linkin park":
        internacional()
    case _:
        msgErro()