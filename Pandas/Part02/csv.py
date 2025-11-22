# %%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')

df

# %%

# df.to_csv('clientes.csv') --- Desse jeito, ele salva com índice 

df.to_csv('clientes.csv', index=False, sep=';')
# Agora ele não salva mais o index e usa ; como separador

# %% 

# Salvando em outros tipos (parquet)

df.to_parquet('clientes.parquet', index=False)

# %%

df_2 = pd.read_parquet('clientes.parquet')

df_2

# %%

# Vamos ler um Excel agora (.xlsx)

df = pd.read_csv('clientes.csv', sep=';')

df.to_excel('clientes.xlsx', index=False)  

# %%

# Vamos tentar ler o arquivo excel que criamos agora

df_3 = pd.read_excel('clientes.xlsx')

df_3

# %%

# Lendo com separador ;

df_bobo = pd.read_csv('../data/bobo.csv', sep=';')

df_bobo