# p. q leia numeros de 0 a 9999 e mostre cada um dos digitos separados

def separarDigitos(n):
    num = int(input("informe um numero: "))
    u = num // 1% 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    print(f"unidade: {u}")
    print(f"dezena: {d}")
    print(f"centena: {c}")
    print(f"milhar: {m}")

    #n = list(str(num))
    #print(f"dezena: {n[-2]}")
    #print(f"centena: {n[-3]}")
    #print(f"milhar: {n[-4]}")

separarDigitos(0)



