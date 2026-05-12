# 3.a - Abrindo o arquivo com o método "open"
arquivo = open("loremipsum.txt", "r") # "r" significa 'read' (leitura)

# 3.b - Imprimindo todo o conteúdo
print("--- Conteúdo Total do Arquivo ---")
print(arquivo.read())

# Precisamos fechar e abrir ou resetar o ponteiro para ler de novo do início
arquivo.seek(0)

# 3.c - Imprimindo apenas a primeira linha
print("\n--- Apenas a Primeira Linha ---")
print(arquivo.readline())

# 3.d - Imprimindo apenas os 3 primeiros caracteres
arquivo.seek(0) # Volta para o início do texto
print("--- Primeiros 3 caracteres ---")
print(arquivo.read(3))

# Fechando o arquivo aberto com open()
arquivo.close()

# 3.e - Utilizando a instrução "with" (Forma mais moderna e segura)
print("\n--- Leitura utilizando a instrução 'with' ---")
with open("loremipsum.txt", "r") as arquivo_com_with:
    conteudo = arquivo_com_with.read()
    print(conteudo)