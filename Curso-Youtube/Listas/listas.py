# %%
# Listas suportam valores de diversos tipos
rafael = ['Rafael', 'Guerino', 19, True, 'Solteiro', 950.98]

print(rafael)

# %%
type(rafael)

# %%
# Calculando média 

idades = [19, 21, 22, 20, 42]

print('A média de idade é igual a:', sum(idades)/len(idades))

print('Menor idade:', min(idades))

print('Maior idade:', max(idades))

# %%
rafael = ['Rafael Guerino', 19, True, ['Estagiário', 'Jr', 'Pl', 'Sr', 'Aposentado'], 'Solteiro', ['Gabriela', 'Isadora', 'Nathália']]

print(len(rafael))

print(rafael[-1][0])

# Printando a última mulher

mulheres = rafael[-1]

print('Última mulher:', mulheres[-1])
# %%
# Imprimindo os 4 primeiros elementos

print(rafael[0:4])

print(rafael[3][-2:])

# %%
# Usando steps

salarios = [1200, 3000, 8000, 19000]

print(salarios)

# Uma forma de mostrar em ordem contrária a lista
print(salarios[::-1])

# Como estão adicionados de forma crescente, podemos usar os steps

print(salarios[0::2])

# Adicionando um valor

salarios.append(950.56)

print(salarios)

# %%
# Pedindo para o usuário adicionar valores a uma lista até parar

lista = []

print(lista)

while True:
    numero = input('Digite um número para adicionar a lista: ')

    if numero == '':
        break;
    else:
        lista.append(int(numero))

print(lista)

# Ordenando em ordem crescente a lista

lista.sort()
print(lista)

# Ordenando em ordem decrescente

lista.sort(reverse=True)
print(lista)