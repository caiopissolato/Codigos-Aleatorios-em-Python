valor = int(input())

if 0 < valor < 1000000:
    print(valor)

    cedulas = [100, 50, 20, 10, 5, 2, 1]

    for i in cedulas:       
        qtd_cedulas = int(valor / i)

        print("{} nota(s) de R$ {},00".format(qtd_cedulas, i))
        valor -= qtd_cedulas * i
        #print(valor)