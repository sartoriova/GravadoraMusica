from FUNCOESmusicas import*
from FUNCOEScantores import*
from FUNCOESgravacoes import*
from FUNCOESauxiliares import*
from datetime import*

def valida_datas ():
    
        mes1 = int(input("Digite o número do mês da data inicial: "))
        mes1_str = str(mes1).zfill(2) #esta função (zfill) obriga a string a ter o tamanho que foi passado por parâmetro, nesse caso, 2!! Portanto, '2' = '02',
        #pois, ela preenche com zeros a esquerda!!
        while ( len(mes1_str) < 2) or ( len(mes1_str) > 2):
            print()
            print("----Formato inválido!")
            print("----Por favor, este número precisa conter de 1 a 2 dígitos!")
            mes1 = int(input("Digite o número do mês da data inicial: "))
            mes1_str = str(mes1).zfill(2)
        while (mes1 < 1 or mes1 > 12):
            print()
            print("----Mês inválido!")
            mes1 = int(input("Digite o número do mês da data inicial: "))
            
        dia1 = int(input("Digite o número do dia da data inicial: "))
        dia1_str = str(dia1).zfill(2)
        while ( len(dia1_str) < 2) or ( len(dia1_str) > 2):
            print()
            print("----Formato inválido!")
            print("----Por favor, este número precisa conter de 1 a 2 dígitos!")
            dia1 = int(input("Digite o número do dia da data inicial: "))
            dia1_str = str(dia1).zfill(2)
        if (mes1 == 2):
            while (dia1 < 1 or dia1 > 29):
                print()
                print("----Dia inválido para o mês de fevereiro!")
                dia1 = int(input("Digite o número do dia da data inicial: "))
        else:
            while (dia1 < 1 or dia1 > 31):
                print()
                print("----Dia inválido!")
                dia1 = int(input("Digite o número do dia da data inicial: "))
            
        ano1 = int(input("Digite o número do ano da data inicial: "))
        ano1_str = str(ano1)
        while ( len(ano1_str) < 4) or ( len(ano1_str) > 4):
            print()
            print("----Formato inválido!")
            print("----Por favor, este número precisa conter, exatamente, 4 dígitos!")
            ano1 = int(input("Digite o número do ano da data inicial: "))
            ano1_str = str(ano1)

        strData1 = dia1_str + "/" + mes1_str + "/" + ano1_str
        
        print()

        mes2 = int(input("Digite o número do mês da data final: "))
        mes2_str = str(mes2).zfill(2)
        while ( len(mes2_str) < 2) or ( len(mes2_str) > 2):
            print()
            print("----Formato inválido!")
            print("----Por favor, este número precisa conter de 1 a 2 dígitos!")
            mes2 = int(input("Digite o número do mês da data final: "))
            mes2_str = str(mes2).zfill(2)
        while (mes2 < 1 or mes2 > 12):
            print()
            print("----Mês inválido!")
            mes2 = int(input("Digite o número do mês da data final: "))
            
        dia2 = int(input("Digite o número do dia da data final: "))
        dia2_str = str(dia2).zfill(2)
        while ( len(dia2_str) < 2) or ( len(dia2_str) > 2):
            print()
            print("----Formato inválido!")
            print("----Por favor, este número precisa conter de 1 a 2 dígitos!")
            dia2 = int(input("Digite o número do dia da data final: "))
            dia2_str = str(dia2).zfill(2)
        if (mes2 == 2):
            while (dia2 < 1 or dia2 > 29):
                print()
                print("----Dia inválido para o mês de fevereiro!")
                dia2 = int(input("Digite o número do dia da data final: "))
        else:
            while (dia2 < 1 or dia2 > 31):
                print()
                print("----Dia inválido!")
                dia2 = int(input("Digite o número do dia da data final: "))
            
        ano2 = int(input("Digite o número do ano da data final: "))
        ano2_str = str(ano2)
        while ( len(ano2_str) < 4) or ( len(ano2_str) > 4):
            print()
            print("----Formato inválido!")
            print("----Por favor, este número precisa conter, exatamente, 4 dígitos!")
            ano2 = int(input("Digite o número do ano da data final: "))
            ano2_str = str(ano2)

        strData2 = dia2_str + "/" + mes2_str + "/" + ano2_str

        dataInicial = datetime.strptime(strData1, '%d/%m/%Y')
        dataFinal = datetime.strptime(strData2, '%d/%m/%Y')

        return (dataInicial, dataFinal)

def exibe_relatorios (dic_musicas, dic_cantores, dic_gravacoes, dataX, dataY, lista_meses):
    achou = False
    for chave in dic_gravacoes:
        data_chave = datetime.strptime(chave[2], '%d/%m/%Y')
        if (data_chave >= dataX) and (data_chave <= dataY):
            achou = True
            titulo_musica = chave[0]
            nomeArt_cantor = chave[1]
            data_gravacao = chave[2]

            print("="*54)
            listar_gravacao(dic_musicas, dic_cantores, dic_gravacoes, lista_meses, titulo_musica, nomeArt_cantor, data_gravacao)
    if (not achou):
        print("="*54)
        print("----Ainda não há gravações cadastradas entre essas datas =(")
