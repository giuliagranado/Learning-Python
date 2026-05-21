# ex030 - par ou impar

def imparPar():
    n = int(input("digite um numero: "))
    if (n % 2) == 0:
        print(n," é par")
    else:  #se o resto for diferente de 0
        print(n," é impar")
imparPar()


# ex031 - custo da viagem
def viagem():
    km = float(input("qual a distancia em km da sua viagem? "))
    passagem = 0.0
    if km <= 200:
        passagem = (km * 0.5)
        print(f"A passagem vai custar R$ {passagem:.2f}")
    else: # se for mais de 200km
        passagem = (km * 0.45)
        print(f"A passagem vai custar R$ {passagem:.2f}")
viagem()