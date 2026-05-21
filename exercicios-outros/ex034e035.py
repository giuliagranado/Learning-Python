# ex034 - aumento multiplicos
def salario():
    sal = float(input("qual seu salário? "))
    if sal > 1250:
        aumento = sal*10/100
        sal = sal+aumento
        print(f"seu aumento foi de R${aumento:.2f}")
        print(f"seu novo salario é R${sal:.2f}")
    else: # sal =< 1250
         aumento = sal*10/100
         sal = sal+aumento
         print(f"seu aumento foi de R${aumento:.2f}")
         print(f"seu novo salario é R${sal:.2f}")
salario()



# ex035 - analiando triangulo v1.0
def triangulo():
    reta1 = float(input("qual tamanho da reta 1?"))
    reta2 = float(input("qual tamanho da reta 2?"))
    reta3 = float(input("qual tamanho da reta 3?"))
    print("verificando se as 3 retas formam um triangulo..")
    if reta1<reta2+reta3 and reta3<reta2+reta1 and reta2<reta1+reta3:
        print(f"as 3 retas de tamanho: {reta1}{reta2}{reta3} , formam um triangulo.")
triangulo()
