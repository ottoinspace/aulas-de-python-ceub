# Criar um lista que ter esses valores ( 20 , 40 ,30 ,10 , 0 )
# faz como que eles virarem uma lista decrescente
# Apaga a posição dois(2) e mostrar o valor apagado
# Inserir o valor dois (2) na posição quatro (4)
# tamanho da lista

lista = [20, 40, 30, 10, 0]

lista.reverse()
print(lista)

variavel = lista.pop(2)
print(variavel)
print(lista)

lista.insert(4, variavel)
print(lista)

print(len(lista))

