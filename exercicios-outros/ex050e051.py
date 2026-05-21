#ex050 - soma pares
def soma():
    soma = 0
    for i in range(6):
        n = int(input("digite o numero: "))
        if n %2==0:
            print(f"-> {soma} + {n}")
            soma = soma + n
            i +=1
    print ("soma total entre pares deu: ", soma)
soma()


# ex051 - progresssão aritmetica
def PA():
    primeiro = int(input("primeiro termo: "))
    razao = int(input("razão: "))
    decimo = primeiro + (10-1)*razao
    for i in range(primeiro, decimo + razao , razao):
        print(i)
        i +=1 
    print("acabou.")
PA()