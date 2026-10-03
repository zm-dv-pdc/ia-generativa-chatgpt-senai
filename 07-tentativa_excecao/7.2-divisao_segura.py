def dividir_seguro(x,y):
     resultado = x/y
     return resultado

try:
     x = input("Digite o primeiro número: ")
     y = input("Digite o segundo número: ")
     valor_resultado = dividir_seguro  (x,y)
     print(valor_resultado)

except ValueError:
     print("Apenas valores numéricos inteiros são permitidos.")

except ZeroDivisionError:
     print("Divisões por zero não são possíveis.")

else:
     print("O valor da divisão é: ", valor_resultado)