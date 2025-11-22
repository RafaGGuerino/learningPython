# %% 

import pandas as pd

url = 'https://datacaixa.com.br/ajuda/duvidas-gerais/informacoes-fiscais/tabela-de-codigo-da-uf-do-ibge/?srsltid=AfmBOop0KzL_vNe-iz9-5Pal2SYfqFHOuWTmaoR6w7tN8Y1UqPb2gl8a'

dfs = pd.read_html(url)

dfs

# Retorna como uma lista...

type(dfs)

# %%

# Vamos testar qual que eu quero

df_uf = dfs[0]

# Nesse caso é só 0 mesmo que funciona, pois tem apenas uma tabela na página

df_uf.to_csv('uf.csv', index=False, sep=';')