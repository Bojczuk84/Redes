texto = input("Digite nomecompleto e data de nascimento: ")
nome = texto.split()[:-1]
print(f'Nome: {nome[0]} {nome[-1]}')
print(f'Data de Nascmento: {data_nascimento}')