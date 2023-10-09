from FUNCOESauxiliares import*

def existe_musica(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

def incluir_musica(armazenamento):

    print()
    print("Informe o nome da música que será incluída abaixo:")
    titulo = foiDigitado()
    
    if existe_musica(armazenamento,titulo):
        print()
        print("Esta música já está cadastrada!!!")
          
    else:
  
        informacoes=[] # irá ficar os itens correspondentes a uma chave

        print()
        print("----Informe os dados da data de registro desta música:")
        print()
        data_music = data()
        print()

        print("Informe o estilo da música abaixo:")
        estilo = foiDigitado()

        print()
        tempo=float(input("Digite o tempo de duração:"))

        print()
        print("Informe o nome do compositor abaixo:")
        compositor= foiDigitado()
        
        print()
        print(f"Você confirma a inclusão de {titulo} neste cadastro (S/N):")
        incluir = confirmacao()
        
        if incluir =="N":
            print()
            print("Inclusão Cancelada!!!")
        else:
            print()
            print(f"{titulo} foi incluída com sucesso!!!")
            informacoes=[data_music,estilo,tempo,compositor] #concatenando todos os itens da chave
            armazenamento[titulo]=informacoes #concatenando no banco de dados

def Menu_alterar_music(armazenamento):
    
    print("------------------------Músicas: Menu de Alterações----------------------------------------")
    print("1. Gostaria de alterar a data de registro de uma música")
    print("2. Gostaria de alterar o estilo musical de uma música")
    print("3. Gostaria de alterar o tempo de duração de uma música")
    print("4. Gostaria de alterar o compositor de uma música")
    print("5. Voltar para o Submenu de Músicas")
    print("--------------------------------------------------------------------------------------------")

    print()
    opcao=int(input("Escolha uma opção do menu de alterações:"))
       
    while opcao!=5:
        if opcao ==1:
            print()
            print("Informe o nome da música que terá seus dados alterados abaixo:")
            nome_mus = foiDigitado()
                
            achou = existe_musica(armazenamento, nome_mus)
            if(achou):
                print()
                print("----Informe os novos dados da data de registro desta música:")
                print()
                data_music=data()
                print()

                print("Data atual:", armazenamento[nome_mus][0])
                print("Nova data:", data_music)
                print()

                print("Tem certeza que deseja alterar a data de registro?(S/N):")
                alterar = confirmacao()
        
                if alterar =="N":
                    print()
                    print("Alteração encerrada!!!")
                else:
                    armazenamento[nome_mus][0]= data_music
                    print()
                    print("Alteração feita com sucesso!!!")
            else:
                print()
                print("Música não encontrada!!")

            continua()
                    
        elif opcao == 2:
            print()
            print("Informe o nome da música que terá seus dados alterados abaixo:")
            nome_mus = foiDigitado()
                
            achou = existe_musica(armazenamento, nome_mus)
            if(achou):
                print()
                print("Informe o novo estilo da música abaixo:")
                estilo= foiDigitado()

                print()
                print("Estilo atual:", armazenamento[nome_mus][1])
                print("Novo estilo:", estilo)
                print()
                
                print("Tem certeza que deseja alterar o estilo da música?(S/N):")
                alterar = confirmacao()
        
                if alterar =="N":
                    print()
                    print("Alteração encerrada!!!")
                else:
                    armazenamento[nome_mus][1]= estilo
                    print()
                    print("Alteração feita com sucesso!!!")
            else:
                print()
                print("Música não encontrada!!")

            continua()
            
                        
                     
        elif opcao == 3:
            print()
            print("Informe o nome da música que terá seus dados alterados abaixo:")
            nome_mus = foiDigitado()
                
            achou = existe_musica(armazenamento, nome_mus)
            if(achou):
                print()
                tempo=float(input("Digite o novo tempo da música:"))

                print()
                print("Tempo atual:", armazenamento[nome_mus][2])
                print("Novo tempo:", tempo)
                print()
                
                print("Tem certeza que deseja alterar o tempo?(S/N):")
                alterar = confirmacao()
        
                if alterar =="N":
                    print()
                    print("Alteração encerrada!!!")
                else:
                    armazenamento[nome_mus][2]= tempo
                    print()
                    print("Alteração feita com sucesso!!!")
            else:
                print()
                print("Música não encontrada!!")

            continua()
                        

        elif opcao == 4:
            print()
            print("Informe o nome da música que terá seus dados alterados abaixo:")
            nome_mus = foiDigitado()
                
            achou = existe_musica(armazenamento, nome_mus)
            if(achou):
                print()
                print("Informe o novo compositor da música abaixo:")
                compositor= foiDigitado()

                print()
                print("Compositor atual:", armazenamento[nome_mus][3])
                print("Novo compositor:", compositor)

                print()
                print("Tem certeza que deseja alterar o compositor?(S/N):")
                alterar = confirmacao()
        
                if alterar =="N":
                    print()
                    print("Alteração encerrada!!!")
                else:
                    armazenamento[nome_mus][3]= compositor
                    print()
                    print("Alteração feita com sucesso!!!")
            else:
                print()
                print("Música não encontrada!!")

            continua()
                        
        else:
            print()
            print("Opção inválida!!!")
            continua()
                    
        print("------------------------Músicas: Menu de Alterações----------------------------------------")
        print("1. Gostaria de alterar a data de produção da música")
        print("2. Gostaria de alterar o estilo musical")
        print("3. Gostaria de alterar o tempo de duração da música")
        print("4. Gostaria de alterar o compositor da música")
        print("5. Voltar para o Submenu de Músicas")
        print("--------------------------------------------------------------------------------------------")

        print()
        opcao=int(input("Escolha uma opção do menu de alterações:"))
                

def excluir_musica(armazenamento,titulo,meses_musica):
    
    if not existe_musica(armazenamento,titulo):
        print()
        print("Música não encontrada!!!")

    else:
        listar_musica(armazenamento,titulo,meses_musica)

        print()
        print("Tem certeza que deseja excluir esta música?(S/N):")
        alterar = confirmacao()

        if alterar =="N":
            print()
            print("Ação cancelada!!!")
            
        else:
            del(armazenamento[titulo])
            print()
            print(f"{titulo} foi excluída com sucesso!")  
           
def listar_musica(armazenamento,titulo,meses_musica):
    
    if not existe_musica(armazenamento,titulo):
        print()
        print("Música não encontrada!!!")    
        
    else:
        
        lista_data=armazenamento[titulo][0].split("/")
        int_data=[]
        for elem in lista_data:
            int_data.append(int(elem))

        dia = int_data[0]
        mes = int_data[1]
        ano = int_data[2]

        print(f"Data de produção: {dia} de {meses_musica[mes]} de {ano}")
        print(f"Estilo musical: {armazenamento[titulo][1]}")
        print(f"Tempo de duração: {armazenamento[titulo][2]}")
        print(f"Compositor: {armazenamento[titulo][3]}")   
                     
def listar_todas_musicas(armazenamento,meses_musica):

    if (armazenamento == {}):
        print("Ainda não há músicas cadastradas!!")
    else:
        print("------------------------ Músicas:------------------------")
        print()
    
        for musica in armazenamento:
             print(f"Título:{musica}")
             listar_musica(armazenamento,musica,meses_musica)
             print("=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-")

def grava_music(dic):

    # Abre o arquivo para gravação:
    arq = open("musica.txt", "w")

    for musica in dic:
        lista = dic[musica]
        
        #titulo data estilo tempo compositor

        linha = musica + ";" + lista[0] + ";" + lista[1] + ";" + str(lista[2]) + ";" + lista[3]+"\n"

        arq.write(linha)
        
    arq.close()

        
def recupera_music(dic):
    if existe_arquivo("musica.txt"):
        
        arq = open("musica.txt", "r")

        for linha_music in arq:

            # a linha é: titulo data estilo tempo compositor
            
            # tira\n :
            linha_music = linha_music[:len(linha_music)-1]

            # Vamos quebrar por ;
            lista = linha_music.split(";")

            # titulo esta em lista[0]
            # data está em lista[1]
            # estilo está em lista[2]
            # tempo está em lista[3]
            # compositor esta em lista[4]
            titulo = lista[0]
            data = lista[1]
            estilo = lista[2]
            tempo = float(lista[3])
            compositor = lista[4]

            # Colocando os dados no dicionario:
            dic[titulo] = [data,estilo,tempo,compositor]
         
def submenu_music(armazenamento,meses_musica):
    print("---------Submenu de Músicas:----------")
    print("1. Incluir música")
    print("2. Alterar dado(s) de uma música")
    print("3. Excluir uma música")
    print("4. Listar dados de uma música específico")
    print("5. Listar dados de todas as músicas")
    print("6. Voltar para o Menu Principal")
    print("---------------------------------------")

    print()
    SM=int(input("Escolha uma opção presente no menu:"))
    
    while SM!=6:
        if SM==1:
            incluir_musica(armazenamento)
            continua()
        
        elif SM==2:
            print()
            Menu_alterar_music(armazenamento)
            continua()
        
        elif SM==3:
            print()
            print("Informe o nome da música que será excluída abaixo:")
            nome_mus = foiDigitado()

            excluir_musica(armazenamento,nome_mus,meses_musica)
            continua()
        
        elif SM==4:
            print()
            print("Informe o nome da música que terá seus dados listados abaixo:")
            nome_mus = foiDigitado()
                
            listar_musica(armazenamento,nome_mus,meses_musica)
            continua()
        
        elif SM==5:
            print()
            listar_todas_musicas(armazenamento,meses_musica)
            continua()
            
        else:
            print()
            print("Número inválido!!!")
            continua()
            
        print("---------Submenu de Músicas:----------")
        print("1. Incluir música")
        print("2. Alterar dado(s) de uma música")
        print("3. Excluir uma música")
        print("4. Listar dados de uma música específica")
        print("5. Listar dados de todas as músicas")
        print("6. Voltar para o Menu Principal")
        print("---------------------------------------")
        print()
        SM=int(input("Escolha uma opção presente no menu:"))
        
    if SM == 6:
        grava_music(armazenamento)
        continua()
