# %%

# Lendo arquivos csv

nome_arquivo = 'data.csv'

with open(nome_arquivo) as open_file:
    lines = open_file.readlines()

#for linha in data:
#    print(linha)

# Vamos deixar isso mais interessante...

# Criando o dicionário...
dados = dict()

# Formatando a primeira linha para ser os campos da tabela
chaves = lines[0].strip('\n').split(';')

# Definindo as chaves do dicionário com a lista formatada
for c in chaves:
    dados[c] = []

# Preenchendo o dicionário com os seus respectivos dados
for l in lines[1:]:
    valores = l.strip('\n').split(';')

    for i in range(len(chaves)):
        dados[chaves[i]].append(valores[i])


for i in dados:
    print('\n' + i + ': ')
    
    for j in dados[i]:
        print(j)
