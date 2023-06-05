salario = float(input("Qual o seu salario? "))

if salario < 1200 and salario >= 0:
    print('Fora da legislacao')
elif salario < 0:
    print('invalido')
else:
    print('Dentro da legislacao')