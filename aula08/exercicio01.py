atleta = input('Atleta: ')

while atleta != '':
    salto = []

    for i in range(0, 5):
        saltos = int(input(f'{i + 1} Salto: '))
        salto.append(saltos)

    media = sum(salto)/len(salto)

    print('Resultado final')
    print()
    print(f'Atleta: {atleta}')
    print(f'Saltos: {salto}')
    print(f'Media dos saltos: {media}')
    print()
    atleta = input('Atleta: ')