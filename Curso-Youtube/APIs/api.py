# %%

import requests     # Realização de requisições na Web
import json     # Manipular json de lista/dicionários para arquivos json
from tqdm import tqdm       # Cria a barra de progresso
import pandas as pd     # Tendo um gostinho de pandas...

# %% 

# url = 'https://viacep.com.br/ws/14850021/json/'

# resposta = requests.get(url)

# print(resposta) # <Response [200]> --> OK!

# %%
# resposta.text

# dados = resposta.json()

# print(dados)

# print(type(dados)) # Dicionário

# %%

# Coletando a informação de vários ceps

ceps = [
    '01001000',
    '20040020',
    '30110050',
    '40010000',
    '70040010',
    '80010000',
    '90010000',
    '60010000',
    '69010000',
    '14850021'
]

url = 'https://viacep.com.br/ws/{cep}/json/' # Criando um placeholder para realizar a tarefa

dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i)) # Para utilizar o placeholder, precisamos usar o método format

    if resposta.status_code == 200: # Verificando se a requisição tem resposta OK para depois preencher a lista
        dados.append(resposta.json())
# %%

# print(dados[5]['localidade'])

# %%

dataset = pd.DataFrame(dados)

dataset.to_csv('ceps.csv', sep=';')

# %%

# Salvando os ceps em um arquivo txt

with open('ceps.json', 'w', encoding='utf-8') as open_file: # Importante usar enconding para aceitar acentos
    
    json.dump(dados, open_file, ensure_ascii=False, indent=4) # indent para proporcionar a identação
