# exercicio aula 20.02.26 - matrizes

import random
import time

# Decorador para medir tempo 
def medir_tempo(func): 
  def wrapper(*args, **kwargs): 
    inicio = time.perf_counter()
    resultado = func(*args, **kwargs) 
    fim = time.perf_counter()
    tempo = fim - inicio
    return resultado, tempo  # retorna o resultado e o tempo gasto
  return wrapper

def gerar_duas_matrizes():
  m = random.randint(1, 5)   # desse jeito gera um numero aleatorio para quantidade
  n = random.randint(1, 5)   # de linhas e colunas, sendo no max 5
  matriz1 = [[random.randint(0, 10) for j in range(n)] for i in range(m)]
  matriz2 = [[random.randint(0, 10) for j in range(n)] for i in range(m)]
  return matriz1, matriz2

@medir_tempo
def soma_matriz(matriz1, matriz2):
  """ por utilizar m e n na criação das duas matrizes, elas sempre terão as mesmas dimensoes. entretanto é importante colocar um condicional para averiguar em outros casos"""
  if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
    print("Erro: dimensões incompatíveis, não é possível somar as matrizes")
    return None
  else:
    soma = []
    for i in range(len(matriz1)):
      linha = []
      for j in range(len(matriz1[0])):
        linha.append(matriz1[i][j] + matriz2[i][j])
      soma.append(linha)
    return soma

@medir_tempo
def multiplicacao_matriz_por2(matriz1, matriz2):
    matriz1_2x = []
    matriz2_2x = []
    for i in range (len(matriz1)):   # multiplicando cada elemento da matriz 1 por 2
        linha = []
        for j  in range(len(matriz1[0])):
            linha.append(matriz1[i][j] *2 )
        matriz1_2x.append(linha)
    for i in range (len(matriz2)):   # multiplicando cada elemento da matriz 2 por 2
        linha = []
        for j  in range(len(matriz2[0])):
            linha.append(matriz2[i][j] *2 )
        matriz2_2x.append(linha)

    return matriz1_2x, matriz2_2x

#chamando funções
matriz1, matriz2 = gerar_duas_matrizes()
print("Matriz 1:")
for linha in matriz1:
  print(linha)
print("\n")
print("Matriz 2:")
for linha in matriz2:
  print(linha)
print("\n")

#soma
soma, tempo_soma = soma_matriz(matriz1, matriz2)
if soma is not None:
  print("Soma das matrizes:")
  for linha in soma:  
    print(linha)
print(f"Tempo gasto na soma: {tempo_soma:.6f} segundos")
print("\n")

#multiplicação
(matriz1_2x, matriz2_2x), tempo_multiplicacao = multiplicacao_matriz_por2(matriz1, matriz2)
print("Multiplicando as matrizes por 2:")
for linha in matriz1_2x:
  print(linha)
print("\n")
for linha in matriz2_2x:
  print(linha)
print(f"Tempo gasto na multiplicacao: {tempo_multiplicacao:.6f} segundos")
print("\n")

#soma das matrizes multiplicadas por 2
soma2, tempo_soma_multiplica = soma_matriz(matriz1_2x, matriz2_2x)
if soma2 is not None:
  print("Soma das matrizes Multiplcadas:")
  for linha in soma2:
    print(linha)
print(f"Tempo gasto na soma das matrizes multiplicadas por 2: {tempo_soma_multiplica:.6f} segundos")

print("\n")
print("A razao entre os dois tempos: ", tempo_soma / tempo_soma_multiplica)
