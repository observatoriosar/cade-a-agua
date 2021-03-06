"""
UNIVERSIDADE FEDERAL DE PERNAMBUCO (UFPE) (https://www.ufpe.br/)
CENTRO DE FILOSOFIA E CIENCIAS HUMANAS
Graduando em Ciencia Politica
IF968 - Programacao I

Autor(a): Claudio Luis Alves Monteiro
Email: claudiomonteirol.a@gmail.com
Data: 2018-05-21

Copyright(c) 2018 Claudio Luis Alves Monteiro
"""

#====================== PROCESSANDO AS INFOS =====================#

#======== criar dict dados usuarios =========#
def maniUserData(user_data):
    # remover "\n"
    user_data = removeCaracter(user_data, "\n")
    # criar lista das infos
    listaUser = []
    for info in user_data:
        usuarioInfo = ""
        for caracter in info:
            if caracter == ";":
                listaUser.append(usuarioInfo)
                usuarioInfo = ""
            else:
                usuarioInfo += caracter
    # criar dicionario das infos
    dict_user = {}
    cont = 7
    while cont < len(listaUser):
        dict_user[listaUser[cont]] = (listaUser[cont+1],listaUser[cont+2],listaUser[cont+3], listaUser[cont+4],listaUser[cont+5], int(listaUser[cont+6]))
        cont += 7
    return dict_user

#======== criar lista dados reclamacoes ========#
def maniReclamaData(reclamacoes):
    # remover "\n"
    reclamacoes = removeCaracter(reclamacoes, "\n") # remover \#
    # criar lista de reclamacoes
    cont = 0
    lista_reclama = []
    while cont < len(reclamacoes):
        lista_reclama.append([reclamacoes[cont], reclamacoes[cont+1], reclamacoes[cont+2], reclamacoes[cont+3]])
        cont += 4
    return lista_reclama

#====================== LOGIN ============================#
def loginUsuario(user_data):
    # verifica cpf
    quebra = False
    user_cpf = input("Olá! Digite seu CPF para entrar na sua conta: ")
    while quebra == False:
        if user_cpf in user_data:
            user_senha = input("Agora insira sua senha: ")
            quebra = True
        else:
            user_cpf = input("CPF não consta em nossa base :( digite novamente: ")
    quebraB = False
    while quebraB == False:
        if user_senha != user_data[user_cpf][0]:
            senhaUser = input("Senha incorreta. Digite novamente: ")
        else:
            quebraB = True
    return user_cpf

#======================= RECLAMACAO =====================#
def Reclamacao(reclamaCod, reclamaNew, user_cpf):
    print("Selecione o tipo de reclamação que você deseja fazer:\n1-Observei um vazamento de água na rua!\n2-Observei uma ligação clandestina (jacaré) na rede de abastecimento!\n3-Tá faltando água na minha casa!")
    reclama = input("Digite o número da reclamação: ")
    localiza = input("Insira o endereço em que você observou o problema (bairro, rua, número da casa à frente): ")
    codReclama = reclamaCod + 1 # codigo da ultima reclamacao registrada + 1
    rec = [codReclama, user_cpf, reclama, localiza]
    reclamaNew.append(rec)

#======================= CADASTRAR OBSERVADOR ===================#
def cadastroObservador(user_data, user_cpf):
    # input infos do usuario
    user_nome = input("Crie seu nome de usuário: ")
    user_email = input("Digite seu email: ")
    user_senha = input("Digite sua senha de acesso: ")
    user_senha2 = input("Repita a senha, por favor: ")
    # testar senhas
    fluxo = False
    while fluxo == False:
        if user_senha == user_senha2:
            fluxo = True
        else:
            print("Senhas não conferem")
            user_senha = input("Digite sua senha de acesso: ")
            user_senha2 = input("Repita a senha, por favor: ")
    # armazeanar infos
    user_data[user_cpf] = (user_senha, user_nome, user_email, "observador","", 0)


#============== Ferramentas Gerais ===============#

# retorna uma lista de objetos, sem um determinado caracter
def removeCaracter(lista,caracter):
    listaFinal = []
    for objeto in lista:
        objetoMani = ""
        for caract in objeto:
            if caract != caracter:
                objetoMani += caract
        listaFinal.append(objetoMani)
    return listaFinal

# acrescenta texto ao fim de cada objeto numa lista
def plusText(lista):
    stringLista = ""
    for caso in lista:
        casoNovo = ""
        casoNovo = caso + "\n"
        stringLista += casoNovo
    return stringLista

# ATENCAO DESENVLVER PARA user_data
# acrescenta texto ao fim de cada objeto numa lista
def plusTextUser(lista):
    stringLista = ""
    for caso in lista:
        casoNovo = ""
        casoNovo = caso + "\n"
        stringLista += casoNovo
    return stringLista

#======================== FUNCIONALIDADES OBSERVADOR =======================#

#========== Visualizar Ranking =========#
def visuRanking(user_data):
    rankLista = []
    for usuario in user_data:
        rankLista.append([user_data[usuario][1], user_data[usuario][5]])
    # lista de contagem
    listaCont = []
    listaContB = []
    for caso in rankLista:
        listaCont.append(caso[1])
        listaContB.append(caso[1])
    # lista ordenada
    listaOrd = []
    while len(listaOrd) < len(rankLista):
        maximo = max(listaContB)
        listaOrd.append(rankLista[listaCont.index(maximo)])
        listaContB.remove(maximo)
    for usuario in listaOrd:
        print(usuario[0], ": ", usuario[1], "Contribuições")

#========== Visualizar Infos Pessoais =========#
def visuInfoUser(user_data, user_cpf):
    print("\n", "CPF: ", user_cpf, "\n" ,
    "Nome de Observador: ", user_data[user_cpf][1], "\n" ,
    "Nível de acesso: ",  user_data[user_cpf][3], "\n",
    "Email: ", user_data[user_cpf][2], "\n" ,
    "Número de contribuições realizadas: ",  user_data[user_cpf][5], "\n")

#========== Baixar Dados das Reclamacoes =========#
# formato CSV
#+++++++++++

#=============== Atualizar Infos ================#
def atualizaInfos(user_data, user_cpf):
    fluxo = True
    while fluxo == True:
        print("Qual das seguintes informações você deseja atualizar:\n1-Senha\n2-Nome de Observador\n3-Email\n4-Sair")
        atualiza = int(input("Digite o número da ação: "))
        # atualizar senha
        if atualiza == 1:
            senhaNova = input("Digite a nova senha: ")
            senhaNovaB = input("Repita a senha, por favor: ")
            # testar senhas
            qubra = False
            while quebra == False:
                if senhaNova == senhaNovaB:
                    qubra = True
                else:
                    print("Senhas não conferem")
                    user_senha = input("Digite sua senha de acesso: ")
                    user_senha2 = input("Repita a senha, por favor: ")
            user_data[user_cpf] = (senhaNova, user_data[user_cpf][1], user_data[user_cpf][2], user_data[user_cpf][3], user_data[user_cpf][4], user_data[user_cpf][5])
        # atualizar nome de usuario
        elif atualiza == 2:
            nomeNovo = input("Digite seu novo nome de observador: ")
            user_data[user_cpf] = (user_data[user_cpf][0], nomeNovo, user_data[user_cpf][2], user_data[user_cpf][3], user_data[user_cpf][4], user_data[user_cpf][5])
        # atualizar email
        elif atualiza == 3:
            emailNovo = input("Digite seu novo email: ")
            user_data[user_cpf] = (user_data[user_cpf][0], user_data[user_cpf][1], emailNovo, user_data[user_cpf][3], user_data[user_cpf][4], user_data[user_cpf][5])
        # sair
        elif atualiza == $:
            fluxo = False

#========== menu observador ============#
def menuObservador(user_data, user_cpf, reclamaCod, reclamaNew):
    pare = False
    while pare == False:
        print("\nMenu do Observador da Água: \n1-Fazer uma reclamação\n2-Visualizar o ranking de observadores da Água\n3-Visualizar minhas informações pessoais\n4-Atualizar informações pessoais\n5-Sair")
        fazer = int(input("Digite o numero da ação: "))
        # opcoes
        if fazer == 1:
            Reclamacao(reclamaCod, reclamaNew, user_cpf)
        elif fazer == 2:
            visuRanking(user_data)
        elif fazer == 3:
            visuInfoUser(user_data, user_cpf)
        elif fazer == 4:
            atualizaInfos(user_data, user_cpf)
        elif fazer == 5:
            pare = True
        else:
            print("Código de ação inválido")

#======================== FUNCIONALIDADES DESENVOLVEDOR =======================#

#=============== Remover Observador da Base ================#
def removeObservador(user_data):
    remove_cpf = input("Digite o número de CPF do Observador a ser retirado: ")
    quebra = False
    while quebra == False:
        if remove_cpf in user_data:
            user_data.pop(remove_cpf, None)
            print("Observador removido com sucesso")
            quebra = True
        else:
            remove_cpf = input("CPF não consta na base. Digite novamente: ")

#=============== Transformar Observador em Desenvolvedor ================#
def transDesenvolvedor(user_data):
    desenvolve_cpf = input("Digite o número de CPF do Observador a ser transformado em Desenvolvedor: ")
    quebra = False
    while quebra == False:
        if desenvolve_cpf in user_data:
            user_data[desenvolve_cpf] = (user_data[desenvolve_cpf][0], user_data[desenvolve_cpf][1], user_data[desenvolve_cpf][2], "desenvolvedor" , user_data[desenvolve_cpf][4], user_data[desenvolve_cpf][5])
            print("Observador atualizado para Desenvolvedor")
            quebra = True
        else:
            desenvolve_cpf = input("CPF não consta na base. Digite novamente: ")

#====================== Menu Desenvolvedor ========================#
def menuDesenvolvedor(user_data):
    pare = False
    valido = True
    while pare == False:
        print("\nMenu Desenvolvimento: \n1-Remover Observador dos usuários\n2-Transformar Observador em Desenvolvedor\n3-Sair")
        if valido == True:
            fazer = int(input("Digite o numero da ação: "))
        # opcoes
        if fazer == 1:
            removeObservador(user_data)
        elif fazer == 2:
            transDesenvolvedor(user_data)
        elif fazer == 3:
            pare = True
        else:
            fazer = int(input("Digite um numero de ação válido: "))
            valido = False

#=========================== SALVAR INFOS ===========================#

#============== reclamacoes =============#
def saveReclamacoes(reclamaNew, lista_reclama):
    reclamaWrite = ""
    for reclama in reclamaNew:
        for info in reclama:
            reclamaWrite += str(info) + "\n"
    lista_reclama.write(reclamaWrite) # escrever as relcamacoes
    lista_reclama.close() # fechar arquivo

#=========  usuarios ==========#
def saveUsuarios(user_data, user_cpf, reclamaNew, lista_user_data):
    # atualizar user_data por reclamacoes
    if len(reclamaNew) > 0 and user_cpf in user_data:
        for reclama in reclamaNew:
            user_data[reclama[1]] = (user_data[reclama[1]][0], user_data[reclama[1]][1], user_data[reclama[1]][2],
            user_data[reclama[1]][3], str(user_data[reclama[1]][4]+ str(reclama[0])), str(user_data[reclama[1]][5]+1))
    # string write
    userDataWrite = ""
    for usuario in user_data:
        userDataWrite += usuario + ";" + user_data[usuario][0] + ";" +user_data[usuario][1] + ";" +user_data[usuario][2] + ";" +user_data[usuario][3] + ";" +user_data[usuario][4] + ";" + str(user_data[usuario][5])+";\n"
    # salvar arquivo
    lista_user_data.write(userDataWrite)
    lista_user_data.close()
