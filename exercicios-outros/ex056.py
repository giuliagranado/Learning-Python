def pessoas():
    soma = 0
    media = 0
    maiorIdadeHomem = 0
    totmulher20 = 0
    for p in range(6):
        print(f"----- {p+1} PESSOA ------")
        nome = str(input("Nome: ")).strip()
        idade = int(input("idade: "))
        sexo = str(input("Sexo [M/F]: ")).strip().upper()
        soma = soma + idade

        if p == 1 and sexo == "M":
            maiorIdadeHomem = idade
            nomeVelho = nome
        if sexo == "M" and idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomeVelho = nome
        if sexo == "F" and idade <20:
            totmulher20+=1

    media = soma / 5
    print(f"a media de idade dessas 5 pessoas é {media:.2f}")
    print(f"O homem mais velho se chama {nomeVelho} e tem {maiorIdadeHomem} anos")
    print(f"Ao todo são {totmulher20} mulheres com mais de 20 anos")
    