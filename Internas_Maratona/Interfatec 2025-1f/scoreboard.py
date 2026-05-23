# problema b - scoreboard

def classificacao():
    sede = (input()).strip()   #unidade
    V, VeSvagas = map(int,input().split())
    NT= int(input()) # quant de times
    
    times = []
    for x in range(NT):
        nome, fatec, prob, tempo = input().split("|")
        times.append( {
            "nome": nome.strip(),
            "fatec": fatec.strip(),
            "problemas": int(prob),
            "tempo": int(tempo)
        } )

    #  separar desclasificados
    desclassificados = []
    candidatos = []
    for j in range(NT):
        if times[NT]["problemas"==0]:
            desclassificados.append(times[NT])
        else:
            candidatos.append(times[NT])

    # separar clasificados por sede
    sede_times = []


    print(sede)
   


    def chave_classificacao(time):
    # mais problemas resolvidos, depois menor tempo
    return (-time["problemas"], time["tempo"])

def resolver():
    sede = input().strip()
    V, VeS = map(int, input().split())
    NT = int(input())
    
    times = []
    for _ in range(NT):
        nome, fatec, prob, tempo = input().split("|")
        times.append({
            "nome": nome.strip(),
            "fatec": fatec.strip(),
            "problemas": int(prob),
            "tempo": int(tempo)
        })
    
    # separar desclassificados
    desclassificados = [t for t in times if t["problemas"] == 0]
    candidatos = [t for t in times if t["problemas"] > 0]
    
    classificados = []
    
    # Item 2: sede
    sede_times = [t for t in candidatos if t["fatec"] == sede]
    sede_times.sort(key=chave_classificacao)
    classificados.extend(sede_times[:VeS+1])
    
    # Item 3: melhor de cada Fatec
    fatecs = {}
    for t in candidatos:
        if t["fatec"] not in fatecs:
            fatecs[t["fatec"]] = t
        else:
            if chave_classificacao(t) < chave_classificacao(fatecs[t["fatec"]]):
                fatecs[t["fatec"]] = t
    for f in fatecs.values():
        if f not in classificados:
            classificados.append(f)
    
    # Item 4: vagas restantes
    restantes = V - len(classificados)
    if restantes > 0:
        candidatos.sort(key=chave_classificacao)
        for t in candidatos:
            if t not in classificados and restantes > 0:
                classificados.append(t)
                restantes -= 1
    
    # Lista de espera
    lista_espera = [t for t in candidatos if t not in classificados]
    lista_espera.sort(key=chave_classificacao)
    
    # Saída
    print("Classificados para a Final")
    for t in sorted(classificados, key=lambda x: x["nome"]):
        print(f"{t['nome']}- {t['fatec']} ({t['problemas']},{t['tempo']})")
    
    print()
    print("Lista de Espera")
    for t in lista_espera:
        print(f"{t['nome']}- {t['fatec']} ({t['problemas']},{t['tempo']})")
    
    print()
    print("Desclassificados")
    for t in sorted(desclassificados, key=lambda x: x["nome"]):
        print(f"{t['nome']}- {t['fatec']} ({t['problemas']},{t['tempo']})")
    
    print()
    print("Apuracao concluida!")