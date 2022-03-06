A, B, C = input().split(" ")
pi = 3.14159

triangulo = (float(A) * float(C)) / 2
circulo = pi * (float(C) * float(C))
trapezio = (((float(A) + float(B)) * float(C)) / 2)
quadrado = float(B) * float(B)
retangulo = float(A) * float(B)

print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(triangulo, circulo, trapezio, quadrado, retangulo))