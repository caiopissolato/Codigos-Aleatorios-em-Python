n = int(input())
hr = int(input())
sal = float(input())

salario = round(sal, 2)
final = hr * salario
print("NUMBER =", n)
print("SALARY = U$ {:.2f}".format(final))