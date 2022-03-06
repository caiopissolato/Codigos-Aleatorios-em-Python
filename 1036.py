import math

a, b, c = input().split(" ")

b_float = float(b)

if(((float(b) * float(b)) - 4 * float(a) * float(c)) < 0 or float(a) == 0):
    print("Impossivel calcular")
else:
    d = math.sqrt((float(b) * float(b)) - 4 * float(a) * float(c))
    print("R1 = {:.5f}\nR2 = {:.5f}".format((-b_float + d) / (2 * float(a)), (-b_float -d) / ( 2 * float(a))))