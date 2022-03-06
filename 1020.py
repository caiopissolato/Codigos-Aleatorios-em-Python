n = int(input())

a = n // 365
n = n - a * 365

m = n // 30
n = n - m * 30

d = n

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(a,m,d))