# ex038 - aprovando empréstimo
def comparacao_valores():
    num1 = int(input("qual o primeiro numero: "))
    num2 = int(input("qual o segundo numero: "))
    if num1 > num2:
        print(f"numero {num1} é maior que {num2}")
    elif num1 < num2:
        print(f"numero {num2} é maior que {num1}")
    else: # num1 ==num2
        print("os dois numeros são iguais")
comparacao_valores()

# ex039 - aprovando empréstimo
from datetime import date
def alistamento():
    atual = date.today().year
    nasc = int(input("Ano de nascimento: "))
    idade = atual - nasc
    print (f"Quem nasceu em {nasc}, tem {idade} anos em {atual}.")
    if idade == 18: 
        print("Hora de se alistar!")
    elif idade < 18:
        print(f"Ainda não está na hora de se alistar. \n Falta {18 - idade} anos.")
        print(f"Seu alistamento será em {nasc+18}")
    else:
        print(f"Você deveria ter se alistado a {idade - 18}. Confira sua situação.")
        print(f"Seu alistamento foi em {nasc+18}")
alistamento()