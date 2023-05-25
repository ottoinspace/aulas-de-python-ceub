quantidade = int(input('Quantos numeros? '))

for i in range (quantidade):
    numero = int(input('Qual o numero: '))
    if numero <= 0:
        numero = 1
    print(numero)