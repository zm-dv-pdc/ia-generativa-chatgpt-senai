# Criando um dicionário / dicionário = {chave:valor, chave:valor}
pessoa = {
    "nome":"Marco Aurélio",
    "idade":"34",
    "cidade": "Barueri"
    }

# Consulta de tipo.
print(type(pessoa))

# Consulta do valor do docionário
print(pessoa["nome"])
print(pessoa["cidade"])

# Consultar com método GET.
print(pessoa.get("altura"))