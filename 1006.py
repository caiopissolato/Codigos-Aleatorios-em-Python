A = float(input())
B = float(input())
C = float(input())

notaA = round(A, 1)
notaB = round(B, 1)
notaC = round(C, 1)

MEDIA = ((2 * notaA) + (3 * notaB) + (5 * notaC)) / (2+3+5)

print("MEDIA = {:.1f}".format(MEDIA))