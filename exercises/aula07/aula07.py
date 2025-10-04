# While
i = 0
while i<10:
    print(i)
    i=i+1

# For
for i in range(10):
    print(i)

for i in range(3,11):
    print(i)

for i in range(1,11,2):
    print(i)

# Lista é um conjunto de variáveis

pedidos = ['Pizza', 'Hamburguer', 'Batata frita']
for pedido in pedidos:
    print(f"Preparando {pedido}")

#Ex.
print(list(range(10)))

print(list(range(1,11)))

print(list(range(0,31,5)))

print(list(range(0,-10,-1)))

# Função range():
for i in range(1,10,2):
    print(i)

for mesa in range(1,10,2):
    print(f"Mesa {mesa} disponível")


# Mostrando apenas a variável na posição 1 como indicado.
minha_lista = [10,20,30]
print(minha_lista[1])

# Adicionando novas variáveis a lista.
minha_lista = [10,20,30]
print(minha_lista[1])
minha_lista.append(40)
minha_lista.insert(4,50)
print(minha_lista)

# Removendo variáveis da lista.
minha_lista = [10,20,30]
print(minha_lista[1])
minha_lista.insert(4,40)
minha_lista.remove(30)
print(minha_lista)

#1. Crie uma lista chamada minhaLista com os seguintes itens: 76, 92.3, "oi", True, 4, 76. Depois execute os seguintes comandos:
#a. Inserir "pera" e 76 no final da lista.
#b. Inserir o valor "gato" na posição de índice 3.
#c. Inserir o valor 99 no início da lista.
#d. Encontrar o índice de "oi".
#e. Remover True da lista.

#1.a
minha_lista = [76,92.3,"oi",True,4,76]
minha_lista.insert(5,"pera")
print(minha_lista)

#1.b
minha_lista = [76,92.3,"oi",True,4,76]
minha_lista.insert(5,"pera")
minha_lista.insert(3,"gato")
print(minha_lista)

#1.c
minha_lista = [76,92.3,"oi",True,4,76]
minha_lista.insert(6,"pera")
minha_lista.insert(4,"gato")
minha_lista.insert(0,99)
print(minha_lista)

#1.d
minha_lista = [76,92.3,"oi",True,4,76]
minha_lista.insert(6,"pera")
minha_lista.insert(4,"gato")
minha_lista.insert(0,99)
print(minha_lista[3])

#1.e
minha_lista = [76,92.3,"oi",True,4,76]
minha_lista.insert(5,"pera")
minha_lista.insert(4,"gato")
minha_lista.insert(0,99)
minha_lista.remove(True)
print(minha_lista)

#Tabuada
print('=== Gerador de tabuada ===')
print()
n1 = int(input('Deseja ver a tauada de: '))
cont = 1
while cont < 11:
    tab = n1 * cont
    print()
    print(n1, 'x', cont, '= ', tab)
    cont += 1

#Tabuada de Multiplicação (de 1 a 10)
num = int(input('Tabuada de: '))
for i in range(1,11):
    print(num, 'x', i, '=', num*i)

#Adicionar um item na lista
uma_lista = [4,2,8,6,5]
uma_lista = uma_lista + ["dato"]
print(uma_lista)

#Adicionar vários itens na lista
uma_lista = [4,2,8,6,5]
uma_lista = uma_lista + ["dato"] + ["Cachoro"] + ["35"]
print(uma_lista)

#Escrever um item de uma tupla através de sua posição
minha_tupla = (10,20,30)
print(minha_tupla[1])

#"Adicionar" itens em uma tupla
minha_tupla = (10,20,30)
print(minha_tupla[1])
minha_tupla = minha_tupla + (40,50)
print(minha_tupla)

#Escrever itens de um dicionário
meu_dicionario = {'nome':'João','idade':30}
print(meu_dicionario['nome'])
meu_dicionario['idade'] = 31
print(meu_dicionario['idade'])
