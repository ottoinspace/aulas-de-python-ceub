#listas
# Faça um programa que receba 5 valores e Adicionar esses valores na lista e depois mostrar a quantidade de valores armazenado na lista e imprimir a lista

lista = []

for c in range(5):
    lista.append(int(input('Insira um numero: ')))
print(lista)

variavel = lista.pop(3)
print(variavel)

#organizando a lista
lista.sort()
print(lista)

#revertendo os valores da lista
lista.reverse()
print(lista)  

# [1, 3 , 4, [5, 6 ,7]]

#media da lista
media = sum(lista)/len(lista)
print(media)

#estatistica
