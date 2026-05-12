# Passo 2: Abre um arquivo (que será criado) chamado "texto.txt"
# O modo "w" significa 'write' (escrita). Se o arquivo não existir, o Python o cria.
arquivo = open("texto.txt", "w", encoding="utf-8")

# Passo 3: Cria uma lista vazia
texto = list()

# Passo 4: Utilizando o método "append" para adicionar frases à lista
texto.append("Esta é a primeira frase do meu arquivo.\n")
texto.append("O Python facilita muito a manipulação de arquivos.\n")
texto.append("Persistência de dados é um conceito fundamental para desenvolvedores.\n")

# Passo 5: Escreve o conteúdo da lista no arquivo
# O método writelines recebe uma lista e escreve cada item no arquivo
arquivo.writelines(texto)

# É muito importante fechar o arquivo para garantir que os dados sejam salvos
arquivo.close()

print("Arquivo 'texto.txt' criado com sucesso na sua pasta!")