# %% Testando unpack e relembrando *args

def soma(*args):
    soma = 0
    for i in args:
        soma += int(i)
    return soma

def set_numeros():
    numeros = []

    while True:
        numero = input('Digite um número: ')

        if numero == '':
            break
        
        numeros.append(numero)
    
    return numeros

numeros = set_numeros()

resultado = soma(*numeros)

print(f'O resultado da soma dos números é: {resultado}')