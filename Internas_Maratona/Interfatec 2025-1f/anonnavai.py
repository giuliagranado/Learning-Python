 #problema i - nonna

def nonna():
    quant = int(input())  # entre 2 e 1000 - q. de pare

    for x in range(quant):
        B1 = int(input())
        B2 = int(input())  # entre 1 e 30 
        soma = B1 + B2

        if B1 > B2 and soma >= 40:
            print("DOROTHY DECIDE E A NONNA VAI")
        elif B1 > B2: 
            print("DOROTHY DECIDE")
        elif B1 < B2 and soma >= 40:
             print("DAGMAR DECIDE E A NONNA VAI")
        else: # B1 < B2 
            print("DAGMAR DECIDE")
nonna()
