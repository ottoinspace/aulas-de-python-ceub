lista = []

while True:
    num = int(input(f'Qual o numero: '))
    if num <= -1:
        break
    else:
        lista.append(num)

numerosPares = 0
for num in lista:
    if num % 2 == 0:
        numerosPares += 1

porcentagemPares = (numerosPares / len(lista)) *100

print(f'Voce digitou {len(lista)}')
print(f'A soma dos valores e {sum(lista)}')
print(f'A media dos valores e {sum(lista)/len(lista): .2f}')
print(f'A porcentagem de numeros pares e {porcentagemPares: .2f}%')
