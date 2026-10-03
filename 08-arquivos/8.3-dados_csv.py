import csv

dados_tabela = [
     ["Nome","Cargo","Idade"],
     ["Caio","Analista","30"],
     ["Marco","Professor","40"],
]

with open("08-4-dados-relatório.csv","w",encoding="utf-8",newline="") as arquivo_csv:
     escrever = csv.writer(arquivo_csv)
     escrever.writerows(dados_tabela)