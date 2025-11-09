# %%
# Criando funções em python

def juros_compostos(aporte:float, taxa:float, anos:int)->float: 
    """
    juros_compostos serve para calcular o retorno financeiro à partir de um aporte. 
    Deve-se considerar o aporte, a taxa de juros e o tempo (anos) para o cálculo do valor.

    aporte:
        um número float que represente o valor em R$
    
    taxa:
        um número float, entre 0 e 1, que represente a taxa de juros considerada.
    
    anos:
        um número inteiro >=1 que represente o período de tempo em anos.
    """
    return aporte * (1 + taxa) ** anos

juros_compostos(1000, 0.18, 5)
# %%

juros_compostos(1000, 0.13, 4)

# Pode mudar a ordem dos parâmetros também

juros_compostos(taxa=0.13, anos=4, aporte=1000)

# %%
# Fazendo funções usando *args, a fim de não usar uma lista
def soma(a:float, b:float, *args)->float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args)+2)

print(soma(20,50,60,80,90))

print(soma(20,70,30))

print(media(30,50,60))

# No *args, cria-se uma LISTA/TUPLA

# %%
# Fazendo outro esquema...**KWARGS
def calc_imposto(preco:float, tx_base:float, **kwargs:dict)->float:
    imposto = preco *tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
        # imposto = imposto + preco * kwargs[i]
    
    return imposto

#calc_imposto(2000, 0.03, municipio=0.01, estadual=0.02)

# Criando um dicionário com os impostos

impostos_gerais = {
    'municipal':0.01,
    'estadual':0.005,
    'nacional':0.001
}

# Atenção ao usar o dicionário na função! Precisa dos **!
calc_imposto(2000, 0.03, **impostos_gerais)

# No **kwargs, cria-se um DICIONÁRIO