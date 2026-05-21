# ex036 - aprovando empréstimo
def emprestimo():
    casa = float(input("qual valor da casa? "))
    salario = float(input("qual o salario do comprador? R$ "))
    anos = int(input("serão quantos anos de financiamento? "))
    meses = anos*12
    prestacao = casa / meses
    minimo = salario * 30/100

    print(f"para pagar uma casa de R$ {casa} em {anos} anos, ou seja {meses}, a prestação será R$ {prestacao:.2f}")

    if prestacao > minimo:
        print("Empréstimo negado. A prestação é maior que 30% do seu salário. ")
    else: 
        print("Empréstimo Aprovado!")

emprestimo()


# ex037 - conversor de bases numericas
def conversor_baseNumerica():
    entrada = int(input("digite um numero: "))
    opcao = int(input("qual será a conversao?  \n 1 - binario ; \n 2 - octal ; \n 3-  hexadecimal. \n digite: "))
    if opcao == 1:
        print(f" o numero {entrada} convertido para binario fica {bin(entrada)[2:]}")
    elif opcao == 2:
        print(f" o numero {entrada} convertido para octal fica {oct(entrada)[2:]}")
    elif opcao == 3:
       # return entrada
        print(f" o numero {entrada} convertido para hexadecimal fica {hex(entrada)[2:]}")
    else:
        print("entrada invalida, tente novamente.")

conversor_baseNumerica()