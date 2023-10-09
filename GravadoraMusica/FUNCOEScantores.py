from FUNCOESauxiliares import*

#########################################################################################################################
#Função: verificar se existe o cantor
def existe_cantor(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False
##########################################################################################################################
#Função:
#Exibi o Submenu de Cantores e a opção para o usuario digitar
def subCantores():
    print("---------Submenu de Cantores:----------")
    print("1. Incluir um cantor")
    print("2. Alterar dado(s) de um cantor")
    print("3. Excluir um cantor")
    print("4. Listar dados de um cantor específico")
    print("5. Listar dados de todos os cantores")
    print("6. Voltar para o Menu Principal")
    print("---------------------------------------")
    print()
    opcaoSM = int(input("Digite o número referente a opção que foi escolhida do Submenu de Cantores: "))
    print()
    return opcaoSM
#########################################################################################################################
#Função:
#Exibi o Cantores: Menu de Alterações e a opção para o usuario digitar
def menuAlteracoes():
    print("------------------------Cantores: Menu de Alterações----------------------------------------")
    print("1. Gostaria de alterar o nome real de algum cantor (O nome artístico não pode ser alterado!)")
    print("2. Gostaria de alterar a data de nascimento de algum cantor")
    print("3. Gostaria de alterar o email de algum cantor")
    print("4. Gostaria de alterar o telefone de algum cantor")
    print("5. Voltar para o Submenu de Cantores")
    print("--------------------------------------------------------------------------------------------")
    print()
    opcaoAltera = int(input("Digite o número referente a opção que foi escolhida do Cantores: Menu de Alterações: "))
    print()
    return opcaoAltera
###########################################################################################################################
#Função:
#Submenu de Cantores - Incluir um cantor
def incluiCantor (nomeArt, dic):
    achou = existe_cantor(dic, nomeArt)
    if (achou):
        print()
        print("----Impossível ter nomes artísticos iguais!")
        return "----Nome artístico já existente!"
    else:
        print()
        print("Informe o nome real deste cantor abaixo:")
        nomeReal = foiDigitado()
            
        print()
        print("----Informe os dados da data de nascimento deste cantor:")
        print()
        dataNas = data()
        print()

        print("Informe o email profissional deste cantor abaixo:")
        email = foiDigitado()
        print()
            
        fone = int(input("Digite o telefone profissional deste cantor (só números): "))
        print()
        print(f"Você confirma a inclusão de {nomeArt} neste cadastro (S/N):")
        confirma = confirmacao()
            
        if (confirma == "S"):
            lista = [nomeReal, dataNas, email, fone]
            dic [nomeArt] = lista
            print()
            return f"----{nomeArt} foi incluído(a) com sucesso!!!"
        else:
            print()
            return "----Operação cancelada pelo usuario!"
#############################################################################################################
#Função:
#Submenu de Cantores - Menu de alterações - Altera nome real
def alteraNomeCantor (nomeArt, dic):
    achou = existe_cantor(dic, nomeArt)
    if (achou):
        print()
        print("Informe o novo nome real deste cantor abaixo:")
        nomeReal = foiDigitado()

        print()
        print("Nome real atual:", dic[nomeArt][0])
        print("Novo nome real:", nomeReal)
            
        print()
        print(f"Você confirma a alteração do nome real de {nomeArt} neste cadastro (S/N):")
        confirma = confirmacao()

        if (confirma == "S"):
            dic[nomeArt][0] = nomeReal
            print()
            return f"----Nome real de {nomeArt} alterado com sucesso!!!"
        else:
            print()
            return "----Operação cancelada pelo usuario!"
    else:
        print()
        return "----Nome artístico não existente no cadastro!"
##############################################################################################################
#Função:
#Submenu de Cantores - Menu de alterações - Altera data de nascimento
def alteraDataCantor (nomeArt, dic):
    achou = existe_cantor(dic, nomeArt)
    if (achou):
        print()
        print("----Informe os novos dados da data de nascimento deste cantor:")
        print()
        dataNas = data()

        print()
        print("Data de nascimento atual:", dic[nomeArt][1])
        print("Nova data de nascimento:", dataNas)
        
        print()
        print(f"Você confirma a alteração da data de nascimento de {nomeArt} neste cadastro (S/N):")
        confirma = confirmacao()

        if (confirma == "S"):
            dic[nomeArt][1] = dataNas
            print()
            return f"----Data de nascimento de {nomeArt} alterada com sucesso!!!"
        else:
            print()
            return "----Operação cancelada pelo usuario!"
    else:
        print()
        return "----Nome artístico não existente no cadastro!"
###############################################################################################################
#Função:
#Submenu de Cantores - Menu de alterações - Altera email
def alteraEmailCantor (nomeArt, dic):
    achou = existe_cantor(dic, nomeArt)
    if (achou):
        print()
        print("Informe o novo email deste cantor abaixo:")
        email = foiDigitado()

        print()
        print("Email atual:", dic[nomeArt][2])
        print("Novo email:", email)
            
        print()
        print(f"Você confirma a alteração do email de {nomeArt} neste cadastro (S/N):")
        confirma = confirmacao()

        if (confirma == "S"):
            dic[nomeArt][2] = email
            print()
            return f"----Email de {nomeArt} alterado com sucesso!!!"
        else:
            print()
            return "----Operação cancelada pelo usuario!"
    else:
        print()
        return "----Nome artístico não existente no cadastro!"
##################################################################################################################
#Função:
#Submenu de Cantores - Menu de alterações - Altera telefone
def alteraFoneCantor (nomeArt, dic):
    achou = existe_cantor(dic, nomeArt)
    if (achou):
        print()
        fone = int(input("Digite o novo número de telefone deste cantor (só números): "))
        
        print()
        print("Número de telefone atual:", dic[nomeArt][3])
        print("Novo número de telefone:", fone)
        print()
        
        print(f"Você confirma a alteração do número de telefone de {nomeArt} neste cadastro (S/N):")
        confirma = confirmacao()

        if (confirma == "S"):
            dic[nomeArt][3] = fone
            print()
            return f"----Telefone de {nomeArt} alterado com sucesso!!!"
        else:
            print()
            return "----Operação cancelada pelo usuario!"
    else:
        print()
        return "----Nome artístico não existente no cadastro!"
###################################################################################################################
#Função:
#Submenu de Cantores - Excluir um cantor
def excluiCantor (nomeArt, dic, lista_meses):
    achou = existe_cantor(dic, nomeArt)
    if (achou):
        print()
        
        retorno = listaCantor (nomeArt, lista_meses, dic)
        if (retorno != "----Nome artístico não existente no cadastro!"):
            print("----Nome artístico:", retorno[0])
            print("----Nome real:", retorno[1])
            print("----Data de nascimento:", retorno[2])
            print("----Email:", retorno[3])
            print("----Telefone:", retorno[4])
        else:
            print(retorno)
            
        print()
        print(f"Você confirma a exclusão de {nomeArt} neste cadastro (S/N):")
        confirma = confirmacao()
        
        if (confirma == "S"):
            del(dic[nomeArt])
            print()
            return f"----{nomeArt} foi excluído(a) com sucesso!!!"
        else:
            print()
            return "----Operação cancelada pelo usuario!"
    else:
        print()
        return "----Nome artístico não existente no cadastro!"
###################################################################################################################
#Função:
#Submenu de Cantores - Listar um cantor
def listaCantor (nomeArt, lista, dic):
    achou = existe_cantor(dic, nomeArt)
    if (achou):
        lista_data = dic[nomeArt][1].split("/")
        indice = int(lista_data[1])
        
        data = lista_data[0] + " de " + lista[indice] + " de " + lista_data[2]
        
        return nomeArt, dic[nomeArt][0], data, dic[nomeArt][2], dic[nomeArt][3]
    else:
         return "----Nome artístico não existente no cadastro!"
###################################################################################################################
#Função:
#Submenu de Cantores - Listar todos os cantores
def listaTudoCantor (lista, dic):
    if (dic != {}):
        for chave in dic:
            print("="*54)
            lista_data = dic[chave][1].split("/")
            indice = int(lista_data[1])
            data = lista_data[0] + " de " + lista[indice] + " de " + lista_data[2]
            print("----Nome artístico:", chave)
            print("----Nome real:", dic[chave][0])
            print("----Data de nascimento:", data)
            print("----Email:", dic[chave][2])
            print("----Telefone:", dic[chave][3])
    else:
        return "----Ainda não há cantores cadastrados!"
####################################################################################################################
#Função:
#Abre o arquivo de cantores para gravação
def grava_cantor(dic):

    # Abre o arquivo para gravação:
    arq = open("cantor.txt", "w")

    for cantor in dic:
        lista = dic[cantor]
        
        #nomeart nomer data email telefone

        linha = cantor + ";" + lista[0] + ";" + lista[1] + ";" + lista[2] + ";" + str(lista[3])+"\n"

        arq.write(linha)
        
    arq.close()
####################################################################################################################
#Função:
#Abre o arquivo de cantores para leitura (recupera os dados)
def recupera_cantor(dic):
    if existe_arquivo("cantor.txt"):
        
        arq = open("cantor.txt", "r")

        for linha_cantor in arq:

            # a linha é:nomeart nomer data email telefone
            
            # tira\n :
            linha_cantor = linha_cantor[:len(linha_cantor)-1]

            # Vamos quebrar por ;
            lista = linha_cantor.split(";")

            # titulo esta em lista[0]
            # data está em lista[1]
            # estilo está em lista[2]
            # tempo está em lista[3]
            # compositor esta em lista[4]
            nomeArt = lista[0]
            nomeR = lista[1]
            data = lista[2]
            email = lista[3]
            telefone = int(lista[4])

            # Colocando os dados no dicionario:
            dic[nomeArt] = [nomeR,data,email,telefone]
#########################################################################################################################
