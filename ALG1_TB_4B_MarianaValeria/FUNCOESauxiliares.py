def continua():
    print()
    input("- Tecle <enter> para continuar -")
    print()

def existe_arquivo (nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

def foiDigitado():
    digitado=input().upper().strip()
    while (digitado == ""):
        print()
        print("Nada foi digitado :/")
        print("Por favor, digite o que se pede para prosseguir!!")
        digitado=input().upper().strip()

    return digitado

def confirmacao():
    confirma = input().upper()
    while ( (confirma != "S") and (confirma != "N") ):
        print()
        print("----Erro na confirmação :/")
        print("Por favor, digite o que se pede para prosseguir!!")
        confirma = input().upper()

    return confirma
    

def menuPrincipal():
    print("------Menu Principal:-------")
    print("1. Submenu de Músicas")
    print("2. Submenu de Cantores")
    print("3. Submenu de Gravações")
    print("4. Submenu Relatórios")
    print("5. Encerrar o programa")
    print("----------------------------")
    print()
    opcaoM = int(input("Digite o número referente a opção que foi escolhida do Menu Principal: "))
    print()
    return opcaoM
       
def data():
    mes = int(input("Digite o número do mês: "))
    mes_str = str(mes).zfill(2) #esta função (zfill) obriga a string a ter o tamanho que foi passado por parâmetro, nesse caso, 2!! Portanto, '2' = '02',
    #pois, ela preenche com zeros a esquerda!!
    while ( len(mes_str) < 2) or ( len(mes_str) > 2):
        print()
        print("----Formato inválido!")
        print("----Por favor, este número precisa conter de 1 a 2 dígitos!")
        mes = int(input("Digite o número do mês: "))
        mes_str = str(mes).zfill(2)
    while (mes < 1 or mes > 12):
        print()
        print("----Mês inválido!")
        mes = int(input("Digite o número do mês: "))
        mes_str = str(mes).zfill(2)
            
    dia = int(input("Digite o número do dia: "))
    dia_str = str(dia).zfill(2)
    while ( len(dia_str) < 2) or ( len(dia_str) > 2):
        print()
        print("----Formato inválido!")
        print("----Por favor, este número precisa conter de 1 a 2 dígitos!")
        dia = int(input("Digite o número do dia: "))
        dia_str = str(dia).zfill(2) 
    if (mes == 2):
        while (dia < 1 or dia > 29):
            print()
            print("----Dia inválido para o mês de fevereiro!")
            dia = int(input("Digite o número do dia: "))
    else:
        while (dia < 1 or dia > 31):
            print()
            print("----Dia inválido!")
            dia = int(input("Digite o número do dia: "))
            
    ano = int(input("Digite o número do ano: "))
    ano_str = str(ano)
    while ( len(ano_str) < 4) or ( len(ano_str) > 4):
        print()
        print("----Formato inválido!")
        print("----Por favor, este número precisa conter, exatamente, 4 dígitos!")
        ano = int(input("Digite o número do ano: "))
        ano_str = str(ano)

    data = dia_str + "/" + mes_str + "/" + ano_str
    return data
