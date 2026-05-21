# ex048 - soma
def somaImpares():
    soma = 0
    for i in range (1,500,2):
        if i % 3 == 0:
            soma = soma + i
            i +=1
    print("a soma de todos os impares divisiveis por 3, entre 1 e 500 = ",soma)
somaImpares()

# ex049 - tabuada com laço for
def tabuada():
    n = int(input("digite um numero: "))
    for i in range(1,11):
        result = n * i
        print(f"{n} x {i} = {result}")
        i +=1
tabuada()