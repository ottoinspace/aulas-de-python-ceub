# Uma agência de publicidade quer prestar seus serviços somente para a maior companhia, considerando a quantidade de funcionários. Para tal, conseguimos um conjunto de dados com o CNPJ (Cadastro Nacional de Pessoa Jurídica) e a quantidade de funcionários de várias empresas. Construa o programa que leia esses dados de entrada e mostre o CNPJ e a quantidade de funcionários da maior empresa, ou seja, da empresa com maior recursos humanos.

# Teste 1: Entrada: 111, 15;  110, 20;                Saída: Maior empresa: 110, qtd 20
# Teste 2: Entrada: 111, 15;  112, 20;  113, 10;  Saída: Maior empresa: 112, qtd 20
num_empresas = int(input('Quantas empresas? '))

cnpjs = []
funcionarios = []

for i in range(num_empresas):
    cnpj = int(input('Digite o CNPJ da empresa: '))
    qtd_funcionarios = int(input('Quantos funcionarios tem a empresa: '))

    cnpjs.append(cnpj)
    funcionarios.append(qtd_funcionarios)

indice_maior = funcionarios.index(max(funcionarios))
maior_cnpj = cnpjs[indice_maior]
maior_qtd_funcionarios = funcionarios[indice_maior]

print(f'Maior empresa: {maior_cnpj}, qtd {maior_qtd_funcionarios}')