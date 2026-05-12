# Criando um array (lista) de 15 números inteiros aleatórios
numeros = [45, 12, 89, 3, 27, 56, 1, 99, 34, 18, 72, 5, 61, 22, 10]

# 1. Ordenação Crescente
numeros.sort() 
print("Números em ordem crescente:")
print(numeros)

# 2. Ordenação Decrescente (usando reverse=True)
numeros.sort(key=None, reverse=True)
print("\nNúmeros em ordem decrescente:")
print(numeros)

print("-" * 30) # Linha separadora

# Criando um array de strings com os campos solicitados
dados = ["nome", "dataNascimento", "cpf", "rg"]

# 1. Ordenação de Strings (Crescente - Alfabética)
dados.sort()
print("Strings em ordem alfabética:")
print(dados)

# 2. Ordenação de Strings (Decrescente)
dados.sort(key=None, reverse=True)
print("\nStrings em ordem decrescente:")
print(dados)