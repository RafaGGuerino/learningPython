# %%

import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv', sep=';')

df_clientes

# %%

# Ver as primeiras linhas do data frame (padrão 5)

df_clientes.head(n=10)

# %%

# Ver por baixo

df_clientes.tail()

# %%

# Vendo sortidos, tipo pegando uma amostra

df_clientes.sample(10)

# %%

# Aparece na formatação (linhas, colunas)
df_clientes.shape

# %%

# Lista as colunas 
df_clientes.columns

# %%

df_clientes.index

# %%

df_clientes.info()