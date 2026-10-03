# Previne contra erros de execução.
entrada_usuario = "abc"

try:
     numero_convertido = int(entrada_usuario)
     print("Conversão realizada com sucesso!", numero_convertido)

except:
     print("Conversão inválida! Digite apenas números!")