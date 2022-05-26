def mensagem1():
    print("Ola!")
#mensagem1()

#def main():
    #mensagem1()
    #mensagem2('Lucas')
'''
def main():
    mensagem2('Lucas')

def mensagem2(nome):
    print("Olá!",nome)

def mensagem3(nome):
    return mensagem1,mensagem2
'''

def mensagem3(nome):
    return 'Olá',nome
def main():
    a = mensagem3('Lucas')
    print(a)
main()


