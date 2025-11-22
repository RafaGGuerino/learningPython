# %%

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

media = sum(idades) / len(idades)

print(media)

# Como calcularíamos a variância normalmente

diff = 0

for i in idades:
    diff += (i - media) ** 2

variancia = diff / (len(idades) - 1)

print(variancia)

# %%

# Usando pandas...

import pandas as pd

series_idades = pd.Series(idades)

series_idades

# %%

media_idades = series_idades.mean()

print(media_idades)

var_idades = series_idades.var()

print(var_idades)

# %% 

# Criando um resumo dos dados

summary_idades = series_idades.describe()

print(summary_idades)