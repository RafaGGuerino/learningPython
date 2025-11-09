# %%
# Criando dicionário e manipulando 
rafael = {
    'nome':'Rafael',
    'sobrenome':'Guerino',
    'filhos':False,
    'formacao':['médio', 'software'],
    'cargos':[
        {'nome':'estagiário', 'empresa':'Prefeitura'},
        {'nome':'pleno', 'empresa':'São Martinho'}
    ]
}

#print(rafael)

print(rafael['cargos'][-1]['empresa'])