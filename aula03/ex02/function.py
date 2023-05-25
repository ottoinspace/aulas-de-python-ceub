
#operador ternario
def par(num):
    print(f'{num} e multiplo de 2!') if num % 2 == 0 else print(f'{num} e multiplo de 1!')

#calculadora
def calculadora(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    produto = num1 * num2
    divisao = num1 / num2
    return f'Soma: {soma} Subtracao: {subtracao} Produto: {produto} Divisao: {divisao}'


