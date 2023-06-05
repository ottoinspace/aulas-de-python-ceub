senha = 0
print('Para acessar digite uma senha')
while True:
    senha = int(input('Digite a senha: '))    
    if senha != 1234:
        print('Senha invalida')
    else:
        print('Acesso Permitido')
        break