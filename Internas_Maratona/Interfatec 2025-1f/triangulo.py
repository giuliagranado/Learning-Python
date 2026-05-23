# problema E - Triangulo

def triangulo():
    pi = 3.14159265358979323846
    while True:
        a, b, angulo = map(float,input().split())
        if a == 0 and b == 0 and angulo== 0 :
            break
        else:
            sin = angulo * pi/180 #conversao p radiano
            s = sin - (sin**3)/6 + (sin**5)/120 -(sin**7)/5040  #calculando seno
            area = 0.5 * a *b * s    
            print(f"{area:.4f}")
triangulo()


