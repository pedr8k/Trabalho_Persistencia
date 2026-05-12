# Passo 3a: Criando um array com 15 números inteiros desordenados
array = [75, 23, 98, 44, 12, 5, 81, 19, 36, 50, 2, 67, 10, 29, 3]

# Passo 3b: Primeiro laço para percorrer os elementos
for i in range(len(array)):
    
    # Passo 3c: Variável que guarda o índice do menor elemento (começa sendo i)
    id_minimo = i
    
    # Passo 3d: Segundo laço para buscar o menor valor no restante do array
    for j in range(i + 1, len(array)):
        
        # Passo 3e: Se o valor no id_minimo for maior que o valor em j...
        if array[id_minimo] > array[j]:
            # Passo 3f: ...o novo menor índice passa a ser j
            id_minimo = j
            
    # Passo 3g: Troca dos valores (o menor encontrado vai para a posição i)
    # Usamos a lógica: A, B = B, A para trocar os valores de lugar
    array[i], array[id_minimo] = array[id_minimo], array[i]

# Passo 3h: Imprimindo o resultado final
print("Array ordenado com Selection Sort:")
print(array)