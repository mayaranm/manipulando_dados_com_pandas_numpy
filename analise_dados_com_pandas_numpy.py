# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np

# Criando uma série de números usando o pandas
numeros = pd.Series([1, 2, 3, 4, 5])

# Exibindo a série original
print("Série original:")
print(numeros)

# Realizando uma operação matemática com numpy (multiplicando por 2)
numeros_dobrados = numeros * 2

# Exibindo o resultado da operação
print("\nSérie após multiplicação por 2:")
print(numeros_dobrados)

# Realizando outra operação com numpy (calculando a raiz quadrada dos números)
raiz_quadrada = np.sqrt(numeros)

# Exibindo o resultado da operação
print("\nRaiz quadrada dos números:")
print(raiz_quadrada)

# Realizando uma comparação lógica (verificando quais números são maiores que 3)
maiores_que_3 = numeros > 3

# Exibindo o resultado da comparação
print("\nNúmeros maiores que 3:")
print(maiores_que_3)
