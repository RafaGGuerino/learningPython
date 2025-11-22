# %% 

import pandas as pd

idades = [
    19,
    12,
    16,
    72,
    64,
    30,
    90,
    23
]

nomes = [
    'Rafael',
    'João',
    'Gabriela',
    'Ana',
    'Mariana',
    'Miguel',
    'Henrique',
    'Marcos'
]

serie_idades = pd.Series(idades)

serie_nomes = pd.Series(nomes)

# %%

# Vamos "pendurar" as series no data frame

df = pd.DataFrame()

df['idades'] = serie_idades

df['nomes'] = serie_nomes

df

# %%

print(df.iloc[0])

print('\n\n')
# Quero saber agora o nome da primeira pessoa do data frame

print(df.iloc[0]['nomes'])