nome = input()
sal_fixo = float(input())
vend = float(input())

salario_fixo = round(sal_fixo, 2)
vendas = round(vend, 2)

TOTAL = vendas * 0.15

print("TOTAL = R$ {:.2f}".format(TOTAL + salario_fixo))