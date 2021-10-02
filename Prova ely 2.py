# Controle Financeiro
menu = 1
valores = []

while menu != 0:
    usuario = str (input(" Digite o usuario: "))
    senha = int (input(" Digite a senha"))
    if usuario != "a" or senha != 123:
        print("Senha ou Usuario inválido")
    else:
        print("Bem vindo ao nosso sistema")
        menu = 0

dolar = float(input("Qual é o valor do Dólar?  "))


def opcao():
    print("1 - Inserir despesas em reais")
    print("2 - Inserir despesas em dólar")
    print("3 - Inserir receitas em reais")
    print("4 - Inserir receitas em dólar")
    print("5 - Extrato")
    print("6 - Maior Despesa")
    print("7 - Maior Receita")
    print("8 - Soma total e média das receitas e despesas")
    print("9 - Sair")
    menu = int(input("O que deseja fazer?  "))
    if menu == 1:
        gastosReais()
    elif menu == 2:
        gastosDolar()
    elif menu == 3:
        ganhosReais()
    elif menu == 4:
        ganhosDolar()
    elif menu == 5:
        extrato()
    elif menu == 6:
        gastoMaior()
    elif menu == 7:
        ganhoMaior()
    elif menu == 8:
        somaMedia()
    elif menu == 9:
        sair()


def menuzinho():
    print("1 - Voltar ao menu principal")
    print("2 - Sair")
    menu = int(input("O que deseja fazer?  "))
    if menu == 1:
        opcao()
    elif menu == 2:
        sair()


def gastosReais():
    valor = 1
    print("Digite seus gastos.")
    print("Quando não houver mais gastos, digite 0.")
    while valor != 0:
        valor = float(input("Digite seus gastos:  "))
        if valor > 0:
            valores.append(valor * -1)
        elif valor < 0:
            valores.append(valor)
    menuzinho()


def gastosDolar():
    valor = 1
    print("Digite seus gastos.")
    print("Quando não houver mais gastos, digite 0.")
    while valor != 0:
        valor = float(input("Digite seus gastos:  "))
        if valor > 0:
            valor = valor * dolar
            valores.append(valor * -1)
        elif valor < 0:
            valor = valor * dolar
            valores.append(valor)
    menuzinho()


def ganhosReais():
    valor = 1
    print("Digite seus ganhos.")
    print("Quando não houver mais ganhos, digite 0.")
    while valor != 0:
        valor = float(input("Digite seus ganhos:  "))
        if valor > 0:
            valores.append(valor)
    menuzinho()


def ganhosDolar():
    valor = 1
    print("Digite seus ganhos.")
    print("Quando não houver mais ganhos, digite 0.")
    while valor != 0:
        valor = float(input("Digite seus ganhos:  "))
        if valor > 0:
            valor = valor * dolar
            valores.append(valor)
    menuzinho()


def extrato():
    print("Imprimindo Extrato")
    print(valores)
    menuzinho()


def gastoMaior():
    maior = 0
    for i in valores:
        if i < maior:
            maior = i
    print("Imprimindo o maior gasto.")
    print(maior)
    menuzinho()


def ganhoMaior():
    maior = 0
    for i in valores:
        if i > maior:
            maior = i
    print("Imprimindo o maior ganho.")
    print(maior)
    menuzinho()


def somaMedia():
    somaGastos = 0
    somadorGastos = 0
    somaGanhos = 0
    somadorGanhos = 0
    for i in valores:
        if i > 0:
            somaGanhos = somaGanhos + i
            somadorGanhos = somadorGanhos + 1
        elif i < 0:
            somaGastos = somaGastos + i
            somadorGastos = somadorGastos + 1
    mediaGanhos = somaGanhos / somadorGanhos
    mediaGastos = somaGastos / somadorGastos
    print("------------------------------------------")
    print("Soma dos ganhos:  ", somaGanhos)
    print("------------------------------------------")
    print("Média dos ganhos:  ", mediaGanhos)
    print("------------------------------------------")
    print("Soma dos gastos:  ", somaGastos)
    print("------------------------------------------")
    print("Média dos gastos:  ", mediaGastos)
    print("------------------------------------------")
    menuzinho()


def sair():
    print("Obrigado por utilizar nossos serviços")


opcao()