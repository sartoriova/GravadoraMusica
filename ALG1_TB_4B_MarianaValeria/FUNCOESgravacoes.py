from FUNCOESmusicas import*
from FUNCOEScantores import*
from FUNCOESauxiliares import*

def existe_gravacao(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False


def incluir_gravacao(arm_musica,arm_cantor,arm_gravacao):
    print("Informe o título da música abaixo:")
    titulo = foiDigitado()
    
    if existe_musica(arm_musica,titulo):
        print()
        print("Informe o nome artístico do cantor abaixo:")
        nomeArt = foiDigitado()
        
        achou = existe_cantor(arm_cantor,nomeArt)
        if (achou):
             print()
             print("----Informe os dados da data de gravação:")
             print()
             data_music=data()
             print()

             chave=(titulo,nomeArt,data_music)
                            
             if existe_gravacao(arm_gravacao,chave):
                print("Esta gravação já existe!!!")
                            
             else:
                informacao=[]
                instrumento=[]

                print("Informe o nome do álbum abaixo:")
                album = foiDigitado()
                print()
                
                inst=input("Digite um instrumento musical ou tecle <enter> para encerrar a digitação de instrumentos:").strip().lower()
                
                while  inst != "" :
                    if inst not in instrumento:
                        instrumento.append(inst)
                    else:
                        print()
                        print("Este instrumento já está na lista!!!")
                              
                    inst=input("Digite um instrumento musical ou tecle <enter> para encerrar a digitação de instrumentos:").strip().lower()
                    
                informacao=[album,instrumento]
                    
                arm_gravacao[chave]=informacao

                print()
                print("Gravação inserida com sucesso!!!")
                
        else:
            print()
            print("Este nome artístico não existe!!!")

    else:
        print()
        print("Esta música não existe!!!")

def alterar_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,titulo,nomeArt,data_grav):
    
    chave=(titulo,nomeArt,data_grav)
    
    if existe_gravacao(arm_gravacao,chave):
        print()
        listar_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,titulo,nomeArt,data_grav) 

        menu_alterar_gravacao(arm_gravacao,chave)
        
    else:
        print()
        print("Esta gravação não existe!!!")

    
def menu_alterar_gravacao(arm_gravacao,chave):
    
    
    print()
    print("------------------------Gravações: Menu de Alterações----------------------------------------")
    print("1. Gostaria de alterar o nome do álbum")
    print("2. Gostaria de alterar os instrumentos")
    print("3. Voltar para o Submenu de Gravações")
    print("--------------------------------------------------------------------------------------------")

    print()
    opcao=int(input("Escolha uma opção do menu de alterações:"))
    
    while opcao!=3:
        if opcao ==1:
            print()
            print("Informe o novo nome do álbum abaixo:")
            album = foiDigitado()

            print()
            print("Tem certeza que deseja alterar o álbum?(S/N):")
            alterar = confirmacao()
            print()
            
            if alterar =="N":
                print("Alteração encerrada!!!")
            else:
                arm_gravacao[chave][0]= album
                print("Alteração feita com sucesso!!!")
                
        elif opcao==2:
            instrumento=[]
            print()
            print("Digite todos os instrumentos novamente!!")
            print()
            inst=input("Digite um instrumento musical ou tecle <enter> para encerrar a digitação de instrumentos:").strip().lower()
                
            while  inst != "" :
                if inst not in instrumento:
                    instrumento.append(inst)
                else:
                    print()
                    print("Este instrumento já está na lista!!!")
                              
                inst=input("Digite um instrumento musical ou tecle <enter> para encerrar a digitação de instrumentos:").strip().lower()

            print()
            print("Tem certeza que deseja alterar os instrumentos?(S/N):")
            alterar = confirmacao()
    
            if alterar =="N":
                print()
                print("Alteração encerrada!!!")
                
            else:
                arm_gravacao[chave][1]= instrumento
                print()
                print("Alteração feita com sucesso!!!")
        else:
            print()
            print("Opção inválida!!!")
            continua()
                
        print()
        print("------------------------Gravações: Menu de Alterações----------------------------------------")
        print("1. Gostaria de alterar o nome do álbum")
        print("2. Gostaria de alterar os instrumentos")
        print("3. Voltar para o Submenu de Gravações")
        print("--------------------------------------------------------------------------------------------")
        
        print()
        opcao=int(input("Escolha uma opção do menu de alterações:"))
    
def excluir_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,titulo,nomeArt,data_grav):
    
    chave=(titulo,nomeArt,data_grav)
    
    if existe_gravacao(arm_gravacao,chave):
        print()
        listar_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,titulo,nomeArt,data_grav)

        print()
        print("Tem certeza que deseja excluir esta gravação?(S/N):")
        alterar = confirmacao()
        print()
        
        if alterar =="N":
            print("Alteração encerrada!!!")
                
        else:
             del arm_gravacao[chave]
             print("Alteração feita com sucesso!!!")
             
    else:
        print()
        print("Esta gravação não existe!!!")


def listar_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,titulo,nomeArt,data_grav):

    chave=(titulo,nomeArt,data_grav)

    if existe_gravacao(arm_gravacao,chave):
        
        # Mostrando os dados da musica:
        print("Música:")
        print(f"Título:{chave[0]}")
        listar_musica(arm_musica,titulo,meses_gravacao)
        print()

        # Mostrando os dados do cantor:
        print("Cantor:")
        retorno = listaCantor(nomeArt, meses_gravacao, arm_cantor)
        if (retorno != "----Nome artístico não existente no cadastro!"):
            print("Nome artístico:", retorno[0])
            print("Nome real:", retorno[1])
            print("Data de nascimento:", retorno[2])
            print("Email:", retorno[3])
            print("Telefone:", retorno[4])
            
        else:
                print()
                print(retorno)
                
        # Mostrando os dados da gravação:
        print()
        print("Gravação:")
        
        lista_data=chave[2].split("/")
        int_data=[]
        for elem in lista_data:
            int_data.append(int(elem))
   
        print(f"Data de gravação: {int_data[0]} de {meses_gravacao[int_data[1]]} de {int_data[2]}")
        print(f"Nome do album: {arm_gravacao[chave][0]}")
        print(f"Instrumentos:")
        for instrumento in arm_gravacao[chave][1]:
            print(instrumento)
    else:
        print()
        print("Esta gravação não existe")
  
def listar_todas_grav(arm_musica,arm_cantor,arm_gravacao,meses_gravacao):

    if (arm_gravacao == {}):
        print()
        print("Ainda não há gravações cadastradas!!")
    else:
        print()
        print("------------------------Dados das gravações:------------------------")

        for chave in arm_gravacao:
            titulo=chave[0]
            nomeArt=chave[1]
            data_grav=chave[2]
            listar_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,titulo,nomeArt,data_grav)
            print('=-'*50)
        
def grava_gravacao(dic):

    # Abre o arquivo para gravação:
    arq = open("gravacao.txt", "w")

    for gravacao in dic:
        lista = dic[gravacao]
        
        instrumentos = "#".join(lista[1])
        
        #titulo nomeArt data album instrumentos

        linha = gravacao[0] + ";" + gravacao[1] + ";" + gravacao[2] + ";" + lista[0] + ";" + instrumentos + "\n"

        arq.write(linha)
        
    arq.close()

        
def recupera_gravacao(dic):
    
    if existe_arquivo("gravacao.txt"):
        
        arq = open("gravacao.txt", "r")

        for linha_grav in arq:

            # a linha é: titulo nomeArt data album instrumentos
            
            # tira\n :
            linha_grav = linha_grav[:len(linha_grav)-1]

            lista = linha_grav.split(";")

            titulo = lista[0]
            nomeArt = lista[1]
            data = lista[2]
            album = lista[3]
            instrumentos = lista[4]

            lista_inst = instrumentos.split("#") #os instrumentos

            chave =(titulo,nomeArt,data)

            dic[chave] = [album, lista_inst]

        arq.close()

 
def menu_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao):
    print("---------Submenu de Gravações:----------")
    print("1. Incluir uma gravação")
    print("2. Alterar dado(s) de uma gravação")
    print("3. Excluir uma gravação")
    print("4. Listar dados de uma gravação específica")
    print("5. Listar dados de todas as gravações")
    print("6. Voltar ao menu principal")
    print("---------------------------------------")

    print()
    opc = int( input("Digite uma opção: ") )
    
    while ( opc != 6 ):
        
        if opc == 1:
            print()
            incluir_gravacao(arm_musica,arm_cantor,arm_gravacao)
            continua()
            
        elif opc == 2:
            print()
            print("Informe o título da música abaixo:")
            nome_mus = foiDigitado()
            print()

            print("Informe o nome artístico do cantor abaixo:")
            art = foiDigitado()
            #art=input("Digite o nome artístico do cantor:").strip().upper()
            print()
            print("----Informe os dados da data de gravação:")
            print()
            data_grav= data()
            alterar_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,nome_mus,art,data_grav)
            continua()
       
            
        elif opc == 3:
            print()
            print("Informe o título da música abaixo:")
            nome_mus = foiDigitado()
            print()
           
            print("Informe o nome artístico do cantor abaixo:")
            art = foiDigitado()
           
            print()
            print("----Informe os dados da data de gravação:")
            print()
            data_grav= data()
            excluir_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,nome_mus,art,data_grav)
            continua()
            
        elif opc == 4:
             print()
             print("Informe o título da música abaixo:")
             nome_mus = foiDigitado()
             print()
             
             print("Informe o nome artístico do cantor abaixo:")
             art = foiDigitado()
             
             print()
             print("----Informe os dados da data de gravação:")
             print()
             data_grav= data()
             print()
             listar_gravacao(arm_musica,arm_cantor,arm_gravacao,meses_gravacao,nome_mus,art,data_grav)
             continua()
            
        elif opc == 5:
            listar_todas_grav(arm_musica,arm_cantor,arm_gravacao,meses_gravacao)
            continua()
            
            
        else:
            print()
            print("Número inválido!!!")
            continua()
            
        print("---------Submenu de Gravações:----------")
        print("1. Incluir uma gravação")
        print("2. Alterar dado(s) de uma gravação")
        print("3. Excluir uma gravação")
        print("4. Listar dados de uma gravação específica")
        print("5. Listar dados de todas as gravações")
        print("6. Voltar ao menu principal")
        print("---------------------------------------")

        print()
        opc = int( input("Digite uma opção: ") )
        
    if opc == 6:
        grava_gravacao(arm_gravacao)
        continua()
