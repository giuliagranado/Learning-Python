# problema F - Suprimentos

def suprimentos():
    n = int(input())     # n de eventos
    supri = 0
    soma = 0

    for x in range(n):
        s = int(input())
        supri += s
        if s < 0:
           soma += -supri   # acumula o déficit
           supri = 0 
    print(soma)
suprimentos()