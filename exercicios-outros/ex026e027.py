# 026 - quantas vezes aparece a letra A; em que posição aparece a 1º vez e a ultima vez.

def contarA(frase):
    frase = str(input("escreva uma frase: ")).lower().strip()
    print(f"a letra A aparece {frase.count('a')} vezes")
    print(f"a letra A aparece pela primeira vez na posição {frase.find('a')+1}")
    print(f"a letra A aparece pela última vez na posição {frase.rfind('a')+1}")
contarA("frase")


# 027 - leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome separadamente

def separarNome(nome):
    nome = str(input("informe seu nome completo: ")).strip()
    n = nome.split()
    print(f"primeiro nome: {n[0]}")
    print(f"último nome: {n[-1]}")

separarNome("nome")