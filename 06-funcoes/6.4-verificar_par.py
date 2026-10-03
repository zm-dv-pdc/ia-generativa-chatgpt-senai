# Definindo a função completa que verifica se o número é par ou nao.
def e_par(numero):
     if numero % 2 == 0:
          return True
     else:
          False

# Usando o retorno da função em estritura IF e ELSE:
if e_par(6):
     print("O número é par.")
else:
     print("O número é ímpar.")