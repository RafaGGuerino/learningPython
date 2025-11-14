# %%
import requests
import pandas as pd

url = 'https://api.opendota.com/api/heroes'

resposta = requests.get(url)

# %%

df = pd.DataFrame(resposta.json())

df.to_csv('heroes_dota_2.csv', sep=';', index=False) # Index false para remover a coluna index