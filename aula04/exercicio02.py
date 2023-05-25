quantidade = int(input('Quantidade de notas: '))
media = 0
for i in range (quantidade):
    nota = float(input(f'Qual a nota {i}: '))
    media += nota

media = media/quantidade

print(f'media: {media: .2f}')

