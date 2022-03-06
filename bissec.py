# Este programa implementa o metodo da
# bisseccao em python

# definindo a funcao: no caso f(x) = x^3 - 27
def f(x):
    res = x**3 - 27.0
    return res

# solicianto o intervalo inicial e o erro ao usuario
print('Entre com o intervalo inicial: ')
xa = float(input())
xb = float(input())

print('Entre com o erro absoluto toleravel: ')
eps = float(input())

# estimativa inicial da raiz contida no intervalo
xm = (xa + xb)/2.0
erro = abs(xb - xa)

# enquanto o erro for maior do que o valor toleravel especificado
# devemos repetir o processo iterativo de aproximacao da raiz
while (abs(erro) > eps): 
    # teste para verificar qual o novo intervalo contendo a raiz
    if (f(xa)*f(xm))   < 0: 
        xb = xm
    elif (f(xa)*f(xm)) > 0:
        xa = xm
    else: # se entrar aqui eh porque encontrou a raiz
        break # interrompe o looping

    xm = (xa + xb)/2.0 # calcula a nova aproximacao
    erro = abs(xb - xa) # estipula a nova estimativa do erro absoluto

print('A raiz eh: '+str(xm)) # mostra o valor final da aproximacao