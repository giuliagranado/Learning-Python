# ex032 - ano bissexto

def anoBissexto():
    ano = int(input("informe o ano para análise: "))
    if ano % 4 == 0 and ano%100!=0 or ano%400==0:
        print(f"o ano {ano} é bissexto!")
    else: 
        print(f"o ano {ano} não é bissexto")
anoBissexto()

# ex033 - maior e menor
def maiorMenor():
    n = int(input("quantos valores quer comparar? "))
    todos = []
    i = 0
    for i in range(n):
        num = int(input("informe o numero: "))
        todos.append(num)
        i =+ 1
    ordenado = sorted(todos)

    print("lista inteira de numeros: ", todos)
    print("lista inteira ordenada: ", ordenado)
    print("o maior: ", ordenado[-1] )
    print("o 2º maior: ", ordenado[-2])
    print("o 3º maior: ", ordenado[-3])
maiorMenor()
