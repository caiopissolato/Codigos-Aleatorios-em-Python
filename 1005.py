nA = float(input())
nB = float(input())

notaA = round(nA, 1)
notaB = round(nB, 1)

MEDIA = ((3.5 * notaA) + (7.5 * notaB)) / (3.5 + 7.5)

print("MEDIA = {:.5f}".format(MEDIA))