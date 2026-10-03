# Aqui usamos a função BULIT-IN nativa do PYTHON que escreve num arquivo LOCAL.
# O modo "w" cria o arquivo "relatorio.txt" na pasta raiz do projeto.
with open("08-relatorio-teste.txt","w") as arquivo:
     arquivo.write("Primeira Linha: Executada com sucesso!")

# Aqui usamos a função BULIT-IN nativa do PYTHON que escreve num arquivo LOCAL.
# O modo "w" cria o arquivo "relatorio.txt" na pasta raiz do projeto.
with open("08-relatorio-teste.txt","w",encoding="utf-8") as arquivo:
     arquivo.write("Primeira Linha: Executada com sucesso!")