# ex 054 - ano de nascimento 
def maioridade():
    from datetime import date
    totmenor = 0
    totmaior =0
    atual = date.today().year
    for i in range(7):
        nasc = int(input(f"Ano de nascimento da {i+1}º pessoa: "))
        idade = atual - nasc
        if idade >= 18:
            totmaior +=1
        else:
            totmenor +=1
        i +=1
    print(f"Ao todo tivemos {totmaior} pessoas maiores \n e {totmenor} pessoas menores de idade.")
maioridade()   

# ex 055 - ano de nascimento 
def pesagem():
    peso = []
    for i in range(6):
        p = int(input(f"qual peso da {i+1}º pessoa? "))
        peso.append(p)
        i += 1
    ordenado = [peso.sort()]
    print("O maior peso entre os listados foi: ", max(peso))
    print("O menor peso entre os listados foi: ", min(peso))
pesagem()



