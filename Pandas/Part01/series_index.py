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

series_idades = pd.Series(idades)

# %%

print(idades[0])
print(series_idades[0])

# %%

series_idades[-1]

# Erro de chave...

# %%

series_idades = series_idades.sort_values()

print(series_idades)

# %%

series_idades[0]

# Note que continua igual, pois os valores são associados aos índices

# %%

print(series_idades.iloc[0])
print(series_idades.iloc[-1])

# Usando o iloc, a serie vai funcionar como uma lista no que se diz respeito aos índices 
# (ignora as chaves)

# %% 

# Agora conseguimos fazer slice, como nas listas

series_idades.iloc[:3]

series_idades.iloc[::-1]

# %%

# Setando os indexes

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

indexes = [
    'Rafael',
    'João',
    'Gabriela',
    'Ana',
    'Mariana',
    'Miguel',
    'Henrique',
    'Marcos'
]

series_idades = pd.Series(idades, index=indexes)

print(series_idades)

# %%

# Buscando nessa série agora

series_idades['Ana']

# Ou...

series_idades.iloc[-1]

print(series_idades[[-1]])