#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota_aluno = float(input("Qual a sua nota na AV01? "))
while nota_aluno > 10:
    print("Nota inválida")
    nota_aluno = float(input("Qual a sua nota na AV01? "))

#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome_usuário = (input("Insira o seu nome de usuário: "))
senha = (input("Insira a sua senha: "))
while senha == nome_usuário:
    print("Senha inválida")
    senha = (input("Insira a sua senha: "))