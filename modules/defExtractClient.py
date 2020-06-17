#importar a biblioteca "os" para poder apagar o arquivo e manipular outras funções
import os
#importar a biblioteca para manipular as linhas dentro do arquvio
from io import StringIO

#definição da função Extrato(6ª opção)   
def Extrato():
    #solicitação para o usuário das variaveis necessárias 
    cpf = int(input("Digite o cpf: "))
    senha = input("Digite a senha do usuário: ")
    
    try:
        #tenta abrir o arquiv especificado, a partir do cpf do cliente
        arquivo = open(str(cpf) + ".txt", 'r+') 
    #caso não consiga a partir do cpf especificado
    except OSError:
        #mensagem para avisar ao usuário que o arquivo não foi encontrado
        print("Arquivo não encontrado")
        print("")
        main()
        
    #ler o arquivo e armazenar numa lista
    c = arquivo.readlines() 
    
    # variavel senha e tamanho da lista
    senhaL = c[4].rstrip(" \n")
    tamanho = len(c)
    
    #conferir se a senha está correta
    if senhaL ==  senha :
        #caso esteja exibe o nome, cpf, tipo de conta do cliente e todas as movimentações
        print("")
        print("Nome: ", c[0],"CPF: ", c[1], "Conta: ", c[2])
        #para exibir as movimentações ignora-se as linhas de senha e saldo
        for linha in c[5:len(c)]:
            print(linha)
        print("")
    else:
        #caso a senha não esteja correta, exibe a mensagem e volta-se ao menu 
        print("Senha incorreta")
        print("")
        
    #fecha-se o arquivo e salva
    arquivo.close()
    