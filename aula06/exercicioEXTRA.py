i = 0
soma = 0

while True:
    nota = int(input('digite uma nota: \n'))
    if nota == -1:
        break
    soma = soma + nota
    i += 1
media = soma / i
print(f'Sua media e {media}')