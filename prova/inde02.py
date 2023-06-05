# Criar um lista com 5 numero diferentes 
# A )Acrescente o valor 3 e 4  na lista 
# B ) Faça com que eles virem uma lista decrescente 
# C ) Depois mostre o tamanho da lista 
# D ) Apaga a primeira posição da lista e coloca o valor 35
# E ) Imprimir a lista

lista = [1, 6, 7, 4, 8]
lista.append(3)
lista.append(4)
lista.sort()
lista.reverse()
print(f'Lista tem {len(lista)} numeros')
lista[0] = 35
print(lista)
