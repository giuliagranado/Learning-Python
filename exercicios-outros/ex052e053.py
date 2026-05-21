# ex052 - primos
def primos():
    n = int(input("digite um numero: "))

    
    if n % 2 == 0 and n!=2:
        print(f"o numero {n} não é primo.")
    elif n % 3 == 0 and n!=3:
        print(f"o numero {n} não é primo.")
    elif n % 5 == 0 and n!=5:
        print(f"o numero {n} não é primo.")
    elif n % 7 == 0 and n!=7:
        print(f"o numero {n} não é primo.")
    elif n % 11 == 0 and n!=11:
        print(f"o numero {n} não é primo.")
    else:
        print(f"o numero {n} é primo.")
        
    
primos()

# ex053 - palindromo
def palindromo(): #le de tras p frente igual de frente p tras
    # exemplos: apos a sopa; a sacada da casa; a torre da derrota
    frase = input("digite a frase: ").strip().upper()
    palavras = frase.split()
    print("você digitou: ", palavras)
    junto = ''.join(palavras)
    inverso = junto[::-1]
    if inverso == junto:
        print("Temos um Palindromo!")
    else:
        print("Não é um Palindromo")
    
palindromo()

