#problema c - agricultor

def agroDecisor():
    n = int(input()) # numero de entradas

    for x in range (n):
        temp, umid, prev = map(float,input().split())

        if prev == 1: 
            print(" NAO REGAR")
        elif temp > 30 and umid < 50:   #prev == 0
            print(" REGAR")
        else:
            print(" NAO REGAR")
agroDecisor()