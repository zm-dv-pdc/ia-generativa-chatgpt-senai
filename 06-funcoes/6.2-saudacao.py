# Definindo a função.
# saudar = nome da função.
# nome = nome do parâmetro.
# Quando criamos a necessidade de usar a variável em usado, precisamos adicionar o 'f' na frente.

# A função recebe um nome(parâmetro) para personalizar a mensagem.
def saudar(nome):
     print(f"Olá, {nome})! Seja bem-vindo(a) ao sistema.")
     # Como ela já tem um PRINT, não precisamos usar "return", ela faz o PRINT diretamente.

# Chamando a função e passando valores diferentes.
saudar("Roberto Carlos")
# Ele usará um novo parâmetro.
fulano = input ("Digite eu nome: ")
saudar (fulano)