# ex028 - jogo da adivinhação  v.1.0
from random import randint

def adivinhacao():
    num = int(input("adivinhe o número que estou pensando! qual seu chute? entre 0 e 10 : "))

    numSorteado = randint(0,10)

    while num != numSorteado:
        if num < numSorteado:
            num = int(input("Errou! Tente um número maior: " ))
        else:   # se num > numSorteado
            num = int(input("Errou! tente um número menor: "))
    if numSorteado == num:
        print("Parabéns! Você acertou o número que eu estava pensando!")
adivinhacao()


# ex029 - radar eletronico 
def radarEletronico():
    radar = 80.00
    velocidade = float(input("qual a velocidade do carro? "))
    multa = 0.00

    if velocidade > radar:
        print("MULTADO! Você ultrapassou o limite de velocidade de 80km/h")
        multa = (velocidade - radar) * 7 # 7,00 reais por cada km acima do limite
        print(f"Você deve pagar uma multa de R$ {multa:.2f}")
    else:  # se  velocidade <= radar
        print("Parabéns! Sem multas para você hoje.")

radarEletronico()