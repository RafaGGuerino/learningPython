# %%

# Escrevendo em um arquivo

nome_arquivo = 'historia_02.txt'

txt = 'meu novo arquivo!!'

with open(nome_arquivo, mode='w') as open_file:
    open_file.write(txt)

# %%

# Escrevendo adicionando

txt = 'Escrevendo mais coisas no meu arquivo!!'

with open(nome_arquivo, mode='a') as open_file:
    open_file.write(txt)