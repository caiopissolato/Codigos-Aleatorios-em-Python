# Essa função retorna o número de letras em uma palavra excluindo as repetidas
def num_letras_diferentes(palavra):
    letras = []
    list_aux = []
    for i in palavra: # preenchendo o vetor com a palavra passada por parâmetro
        letras.append(i)

    for i in letras:
        if not list_aux.__contains__(i):
            list_aux.append(i)

    return len(list_aux)