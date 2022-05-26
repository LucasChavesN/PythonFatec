def lerLista():
    lista = [0]*4
    for i in range(len(lista)):
        lista[i]=int(input("Digite um valor: "))
    return lista

def media(b):
    s=0
    for i in range(len(b)):
        s = s + b[i]
    return s/len(b)

def mostrarMaiores(lista, media):
    for i in range(len(lista)):
        if lista[i]>media:
            print(lista[i])

def main():
    print("Elementos da 1a. Lista")
    x = lerLista()
    print("Elementos da 2a. Lista")
    y = lerLista()
    m = media(x)
    print("Média dos Elementos da 1a. Lista = %d"%m)
    m = media(y)
    print("Média dos Elementos da 2a. Lista = %d"%m)
    p = media(x)
    print("Elementos da 1a. Lista Acima da Média")
    mostrarMaiores(x,m)
    print("Elementos da 2a. Lista Acima da Média")
    mostrarMaiores(y,p)
main()