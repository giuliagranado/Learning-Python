# problema K - Fonte

def fonte():
    t = int(input())*2
    vale = int(input())
    colina = int(input())
    topo = int(input())

    custo_vale = (t*0) *vale + colina*(t* 1) + topo *(t*2)
    custo_colina = vale*(t* 1) + colina*t*0 + topo*(t* 1)
    custo_topo = vale*(t* 2) + colina*(t* 1) + topo*(t*0)
        

    print(min(custo_vale, custo_colina, custo_topo))
fonte()