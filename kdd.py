import time

# 1. Definição dos algoritmos (copiados das microatividades)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
def selection_sort(lista):
        id_min = i
        for j in range(i + 1, n):
            if lista[id_min] > lista[j]:
                id_min = j
        lista[i], lista[id_min] = lista[id_min], lista[i]
# --- INÍCIO DO PROCESSO ---
# a. Criar a lista para armazenar as palavras
palavras_base = list()
# b, c, d. Ler o arquivo e separar por palavras usando split()
print("Lendo arquivo e processando palavras...")
with open("loremipsum.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # split() quebra a frase em palavras onde houver espaço
        palavras_da_linha = linha.split()
        # Adiciona cada palavra na nossa lista principal
        for p in palavras_da_linha:
            # Transformamos em minúsculas para a ordenação ser justa
            palavras_base.append(p.lower())
# --- COMPARAÇÃO DE PERFORMANCE ---
# Testando Bubble Sort
lista_bubble = palavras_base.copy()
inicio = time.time()
bubble_sort(lista_bubble)
fim = time.time()
print(f"Bubble Sort levou: {fim - inicio:.6f} segundos")
# Testando Selection Sort
lista_selection = palavras_base.copy()
selection_sort(lista_selection)
print(f"Selection Sort levou: {fim - inicio:.6f} segundos")
# Testando Método Nativo .sort()
lista_nativo = palavras_base.copy()
lista_nativo.sort()
print(f"Método Nativo (.sort) levou: {fim - inicio:.6f} segundos")
# --- FINALIZAÇÃO ---
# Escolhendo o melhor (sempre será o Nativo ou Selection em listas pequenas)
# Vamos salvar o resultado do nativo no arquivo final
with open("palavras_ordenadas.txt", "w", encoding="utf-8") as f_final:
    for p in lista_nativo:
        f_final.write(p + "\n")
print("\nGlossário criado com sucesso no arquivo 'palavras_ordenadas.txt'!")