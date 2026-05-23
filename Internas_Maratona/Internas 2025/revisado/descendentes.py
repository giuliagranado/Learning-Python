# Problema D - Descendentes  -  não submetido

# erro principal: passagem errada de valores ´p função,
#                 retonar n re relações, inves da contagem acumulada

n = int(input())    #número de relações de paternidade
pai_filho = []      #lista para armazenar as relações de paternidade

for i in range(n):    
    pf = input().split()   #separa o input em pai e filho
    pai_filho.append(pf)   #add no array, ficando assim [['1', '2'], ['2', '3'], ['3', '5'], ['2', '4']]

R = int(input())   # o número de que se quer saber a quant de descendentes
h = 0

def contar_descendentes(pai_filho,R):
    descendentes = 0
    for pai,filho in pai_filho:
        if int(pai) == R:
            descendentes += 1
            # soma os descendentes do filho recursivamente
            descendentes += contar_descendentes(pai_filho, int(filho))
    return descendentes

print(contar_descendentes(pai_filho, R))
    