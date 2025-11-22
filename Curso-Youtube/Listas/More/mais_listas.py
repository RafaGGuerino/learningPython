# %%

# Preenchendo listas usando for em apenas uma linha

y = [i for i in range(1,101)]

y

# %%

# Preenchendo listas usando resultados de funções

def eh_par(numero:int)->bool:
    """
        Função para retornar se um número inteiro é par.

        numero:
            número inteiro (int) que será verificado se é par ou não
        
        O retorno da função é booleano (True / False)
    """
    return numero % 2 == 0

x = [eh_par(i) for i in range(1,101)]

x

# %%

# Só quero os números pares agora

w = [i for i in range(1,101) if eh_par(i) == True]

w
