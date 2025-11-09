# %%

nome_arquivo = 'historia.txt'

# %%

# Maneira menos usual e sujeita a erros

# Abrindo o arquivo
open_file = open(nome_arquivo)

# Se printarmos o open_file...
# print(open_file)

# Lendo o conteúdo do arquivo

conteudo = open_file.read()

print(conteudo)

# Fechando o arquivo
open_file.close()

# %% 

# Maneira mais comum

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

# Dessa maneira, ele fecha o arquivo automaticamente