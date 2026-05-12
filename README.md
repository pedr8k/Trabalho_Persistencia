# Trabalho Prático: Persistência de Dados e Ordenação em Python

Este projeto foi desenvolvido como parte de um trabalho acadêmico focado em manipulação de arquivos (persistência de dados) e comparação de performance entre diferentes algoritmos de ordenação utilizando a linguagem Python.

## 🚀 Funcionalidades

O projeto consiste em scripts que realizam as seguintes tarefas:
* **Leitura de Dados:** Extração de palavras de um arquivo de texto (`loremipsum.txt`).
* **Ordenação:** Implementação e comparação de três métodos:
    * **Bubble Sort:** Algoritmo simples de troca.
    * **Selection Sort:** Algoritmo baseado na busca pelo menor elemento.
    * **Método Nativo (.sort):** Algoritmo otimizado do próprio Python.
* **Persistência:** Gravação dos resultados ordenados em um novo arquivo (`palavras_ordenadas.txt`).
* **Medição de Tempo:** Comparação exata de quantos segundos cada método levou para processar os dados.

## 📂 Estrutura do Projeto

* `kdd.py`: Script principal que executa os testes de ordenação e salva o arquivo final.
* `array.sort.py`: Demonstração de ordenação de listas e dicionários.
* `bubble.sort.py`: Implementação isolada do Bubble Sort.
* `selection.sort.py`: Implementação isolada do Selection Sort.
* `loremipsum.txt`: Arquivo de entrada com o texto original.
* `palavras_ordenadas.txt`: Arquivo gerado após o processamento.
