# Desenvolva o programa que leia vários(N) números digitados e mostre estas informações: 
# A) Quantidade de elementos dados ;
# B) Soma dos valores ;
# C) media dos valores ;
# D) porcentagem(ate duas casas decimais ) de números pares ;
# (( Pode usar o comando While ou For ))

lista = []
while True:
    n = int(input('Digite um numero (para sair -1): '))
    if n >= 0:
        lista.append(n)
    else:
        break
numerosPares = 0
for n in lista:
    if n % 2 == 0:
        numerosPares += 1

print(f'Foram digitados {len(lista)} numeros')
print(f'A soma dos numeros e {sum(lista)}')
print(f'A porcentagem numeros pares e {(numerosPares/len(lista))*100: .2f}%')