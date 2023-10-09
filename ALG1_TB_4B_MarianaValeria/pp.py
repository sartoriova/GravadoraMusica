from FUNCOEScantores import*
from FUNCOESauxiliares import*
from FUNCOESmusicas import*
from FUNCOESgravacoes import*
from FUNCAOrelatorios import*
from datetime import*

bd_musicas={}
bd_cantores = {}
bd_grav={}
meses = [".", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

## recuperar dados
recupera_music(bd_musicas)
recupera_cantor(bd_cantores)
recupera_gravacao(bd_grav)

opcaoM = 0

while (opcaoM != 5):
    opcaoM = menuPrincipal()

    while (opcaoM < 1 or opcaoM > 5):
        print("----Opção inválida!")
        print("----Digite uma opção válida para este menu!")
        print()
        opcaoM = menuPrincipal()
        
    if opcaoM== 1:
        submenu_music(bd_musicas,meses)
        

    if (opcaoM == 2):
        opcaoSM = 0

        while (opcaoSM != 6):
            opcaoSM = subCantores()

            while (opcaoSM < 1 or opcaoSM > 6):
                print("----Opção inválida!")
                print("----Digite uma opção válida para este submenu!")
                print()
                opcaoSM = subCantores()
                
            if (opcaoSM == 1):
                print("Informe o nome artístico do cantor que será incluído abaixo:")
                nome = foiDigitado()
                
                print( incluiCantor(nome, bd_cantores) )
                continua()
                
            elif (opcaoSM == 2):
                opcaoAltera = 0

                while (opcaoAltera != 5):
                    opcaoAltera = menuAlteracoes()

                    while (opcaoAltera < 1 or opcaoAltera > 5):
                        print("----Opção inválida!")
                        print("----Digite uma opção válida para este menu!")
                        print()
                        opcaoAltera = menuAlteracoes()

                    if (opcaoAltera == 1):
                        print("Informe o nome artístico do cantor que terá seus dados alterados abaixo:")
                        nome = foiDigitado()
                            
                        print( alteraNomeCantor(nome, bd_cantores) )
                        continua()

                    elif (opcaoAltera == 2):
                        print("Informe o nome artístico do cantor que terá seus dados alterados abaixo:")
                        nome = foiDigitado()
                            
                        print( alteraDataCantor(nome,bd_cantores) )
                        continua()

                    elif (opcaoAltera == 3):
                        print("Informe o nome artístico do cantor que terá seus dados alterados abaixo:")
                        nome = foiDigitado()
                            
                        print( alteraEmailCantor(nome,bd_cantores) )
                        continua()

                    elif (opcaoAltera == 4):
                        print("Informe o nome artístico do cantor que terá seus dados alterados abaixo:")
                        nome = foiDigitado()
                            
                        print( alteraFoneCantor(nome,bd_cantores) )
                        continua()

            elif (opcaoSM == 3):
                print("Informe o nome artístico do cantor que será excluído abaixo:")
                nome = foiDigitado()
                
                print( excluiCantor(nome,bd_cantores, meses) )
                continua()

            elif (opcaoSM == 4):
                print("Informe o nome artístico do cantor que terá seus dados listado:")
                nome = foiDigitado()
                
                retorno = listaCantor(nome, meses,bd_cantores)
                if (retorno != "----Nome artístico não existente no cadastro!"):
                    print()
                    print("----Nome artístico:", retorno[0])
                    print("----Nome real:", retorno[1])
                    print("----Data de nascimento:", retorno[2])
                    print("----Email:", retorno[3])
                    print("----Telefone:", retorno[4])
                else:
                    print()
                    print(retorno)
                continua()

            elif (opcaoSM == 5): 
                retorno = listaTudoCantor(meses, bd_cantores)
                if (retorno != "----Ainda não há cantores cadastrados!"):
                    print("="*54)
                else:
                    print(retorno)
                continua()
                
        if (opcaoSM == 6):
            grava_cantor(bd_cantores)
                
    if (opcaoM == 3):
        menu_gravacao(bd_musicas,bd_cantores,bd_grav,meses)

    if (opcaoM == 4):
        datas_relatorios = valida_datas()
        
        dataInicial = datas_relatorios[0]
        dataFinal = datas_relatorios[1]

        print()
        exibe_relatorios(bd_musicas, bd_cantores, bd_grav, dataInicial, dataFinal, meses)
        print("="*54)
        continua()

print("----Programa encerrado pelo usuario!")
print("----Fim do programa, obrigado(a) =)")
