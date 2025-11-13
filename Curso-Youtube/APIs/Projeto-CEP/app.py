import requests
import streamlit as st

def buscar_cep(cep):
    endpoint = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        ''

st.image('https://i.imgur.com/NLJqefj.png')
st.title('Consultar informações de CEPs')

cep = st.text_input('Digite o CEP que você deseja consultar: ')
pesquisar = st.button('Pesquisar')

if pesquisar:
    dados = buscar_cep(cep)

    if dados:
        st.success('Informações do CEP encontradas com sucesso!')
        st.text(dados)
    else:
        st.error('Infelizmente não foi possível encontrar o CEP digitado')