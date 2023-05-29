numero = 0
lista = []

while True:
    numero = float(input('digite um numero: \n'))
    if numero <= -1:
        break
    lista.append(numero)

print(f'O maior valor e: {max(lista)}')
print(f'O menor valor e: {min(lista)}')

#resposta altenartiva
x = 0
maior = float('-inf')
menor = float('inf')

x = int(input('Digite um numero: \n'))
while x <= -1:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    x = int(input('Digite um numero: \n'))

print(f'O maior valor e: {maior}')
print(f'O menor valor e: {menor}')