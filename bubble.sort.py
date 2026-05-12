# Passo 3a: Criando o método bubbleSort
def bubbleSort(array):
    # Passo 3b: Primeiro laço para percorrer todo o array
    for i in range(len(array)):
        
        # Passo 3c: Segundo laço para comparar os elementos dois a dois
        # O "- i - 1" serve para não olhar os números que já "flutuaram" para o fim
        for j in range(0, len(array) - i - 1):
            
            # Passo 3d: Se o elemento atual for maior que o próximo, eles trocam de lugar
            if array[j] > array[j + 1]:
                # Criamos a variável auxiliar (como um pote vazio para guardar o valor)
                temp = array[j]
                # Fazemos a troca
                array[j] = array[j + 1]
                array[j + 1] = temp

# Passo 3e: Declarando um array de 15 números desordenados
lista_numeros = [64, 34, 25, 12, 22, 11, 90, 5, 40, 18, 9, 2, 55, 30, 1]

# Passo 3f: Aplicando o seu método criado
bubbleSort(lista_numeros)

# Passo 3g: Imprimindo o resultado
print("Array ordenado com Bubble Sort:")
print(lista_numeros)